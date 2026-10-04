"""Parent-side preservation and paired-input audit; never changes trial outputs."""
from pathlib import Path
import hashlib
import json

BASE = Path(__file__).resolve().parent
REPO = BASE.parent.parent


def read(path):
    return json.loads(path.read_text())


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None


def main():
    manifest = read(BASE / "manifest.json")
    changed_frozen = [p for p, h in manifest.items() if digest(BASE / p) != h]
    baseline = read(REPO / "share/skill-ab-20261004/evidence/baseline.json")
    changed_baseline = [p for p, h in baseline.items() if digest(REPO / p) != h]
    pairs = []
    for case in ("fresh", "stale", "blocked"):
        off = read(BASE / "initial-inventories" / case / "off.json")
        on = read(BASE / "initial-inventories" / case / "on.json")
        supplied = on.pop("guidance/skills/workflow-orchestrator/SKILL.md")
        prompts = []
        for arm in ("off", "on"):
            text = (BASE / "dispatch" / case / arm / "prompt.txt").read_text()
            prompts.append(text.replace(f"runs/{case}/{arm}", f"runs/{case}/ARM")
                           .replace(f"Skill-body condition: {arm}.", "Skill-body condition: ARM."))
        pairs.append({"case": case, "identical_common_files": off == on,
                      "skill_matches_frozen_body": supplied == digest(BASE / "frozen/skill.raw"),
                      "identical_normalized_prompts": prompts[0] == prompts[1]})
    result = {"frozen_file_count": len(manifest), "changed_frozen": changed_frozen,
              "preexisting_file_count": len(baseline), "changed_preexisting": changed_baseline,
              "pairs": pairs}
    result["passed"] = not changed_frozen and not changed_baseline and all(
        all(v for k, v in pair.items() if k != "case") for pair in pairs)
    (BASE / "integrity.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
