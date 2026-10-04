"""Parent-only evidence export; excludes private reasoning and account metadata.

This collector is not part of the frozen scorer and never touches trial roots.
It preserves visible calls/results; scope qualification is a separate manual audit.
"""
from pathlib import Path
import hashlib
import json

BASE = Path(__file__).resolve().parent
PARENT = "01a1010e-6f38-7981-9e24-def8eadbf7ff"
SESSIONS = Path("/Users/yuki/.codex/sessions/2026/10/04")
TOOLS = {"function_call", "function_call_output", "custom_tool_call", "custom_tool_call_output"}


def main():
    cells = json.loads((BASE / "protocol.json").read_text())["cells"]
    targets = {f'/root/skill_ab_{c["case"]}_{c["arm"]}': c for c in cells}
    skill = (BASE / "frozen/skill.raw").read_text()
    sentinel = "Do not mix its metadata with a separate `inputs`"
    for path in SESSIONS.glob("*.jsonl"):
        with path.open() as handle:
            first = json.loads(next(handle))
        meta = first.get("payload", {})
        name = meta.get("agent_path")
        if meta.get("parent_thread_id") != PARENT or name not in targets:
            continue
        cell = targets[name]
        records = []
        incomplete_lines = 0
        for line in path.read_text().splitlines():
            try:
                records.append(json.loads(line))
            except ValueError:
                incomplete_lines += 1
        dest = BASE / "transcripts" / cell["case"] / cell["arm"]
        dest.mkdir(parents=True, exist_ok=True)
        public = []
        settings = []
        tokens = None
        started = finished = None
        inbound = []
        encrypted_items = 0
        final = []
        for record in records:
            payload = record.get("payload", {})
            kind = record.get("type")
            subtype = payload.get("type")
            if kind == "turn_context":
                settings.append({k: payload.get(k) for k in ("model", "effort", "reasoning_effort")})
            if kind == "event_msg":
                if subtype == "task_started":
                    started = record.get("timestamp")
                if subtype in ("task_complete", "task_completed", "turn_aborted"):
                    finished = {"timestamp": record.get("timestamp"), "type": subtype}
                if subtype == "token_count":
                    tokens = payload.get("info", {}).get("total_token_usage")
            if kind != "response_item":
                continue
            if subtype == "message" and payload.get("role") in ("user", "developer", "system"):
                texts = [part.get("text", "") for part in payload.get("content", [])]
                text = "\n".join(texts)
                inbound.append({"role": payload.get("role"), "sha256": hashlib.sha256(text.encode()).hexdigest(),
                                "full_skill_body_present": skill in text, "skill_sentinel_present": sentinel in text})
            encrypted_items += sum(part.get("type") == "encrypted_content" for part in payload.get("content", []) if isinstance(part, dict))
            if subtype in TOOLS or (subtype == "message" and payload.get("role") == "assistant"):
                clean = {k: v for k, v in payload.items() if k != "internal_chat_message_metadata_passthrough"}
                public.append({"timestamp": record.get("timestamp"), "payload": clean})
                if subtype == "message" and payload.get("phase") == "final_answer":
                    final.extend(part.get("text", "") for part in payload.get("content", []))
        calls = [r for r in public if r["payload"]["type"] in ("function_call", "custom_tool_call")]
        outputs = [r for r in public if r["payload"]["type"] in ("function_call_output", "custom_tool_call_output")]
        call_ids = {r["payload"].get("call_id") for r in calls}
        result_ids = {r["payload"].get("call_id") for r in outputs}
        metadata = {"agent_path": name, "thread_id": meta.get("id"), "source_rollout": str(path),
                    "source_sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "settings": settings,
                    "started": started, "finished": finished, "calls": len(calls), "outputs": len(outputs),
                    "unmatched_call_ids": sorted(call_ids - result_ids), "incomplete_jsonl_lines": incomplete_lines,
                    "logged_cumulative_tokens": tokens, "inbound_context_body_checks": inbound,
                    "encrypted_content_items_not_exported": encrypted_items,
                    "excluded": "Private reasoning, hidden system/developer bodies, account metadata and encrypted content are not exported.",
                    "scope_audit": "Pending parent manual examination; call completeness is not an OS sandbox guarantee."}
        (dest / "tool-and-public-messages.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in public))
        (dest / "metadata.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n")
        (dest / "calls.txt").write_text("\n\n".join(
            f'{r["timestamp"]} {r["payload"].get("name")} {r["payload"].get("call_id")}\n'
            + str(r["payload"].get("input", r["payload"].get("arguments"))) for r in calls) + "\n")
        if final:
            (dest / "final.md").write_text("\n".join(final))
        print(json.dumps({k: metadata[k] for k in ("agent_path", "thread_id", "settings", "finished", "calls", "unmatched_call_ids")}))


if __name__ == "__main__":
    main()
