"""Record delivery of the frozen skill body; not proof of model comprehension."""
from pathlib import Path
import hashlib, json, time

root = Path(__file__).resolve().parent
path = root / "guidance/skills/workflow-orchestrator/SKILL.md"
raw = path.read_bytes()
audit = root / "audit"
audit.mkdir(exist_ok=True)
with (audit / "skill_reads.jsonl").open("a") as handle:
    handle.write(json.dumps({"time_ns": time.time_ns(), "path": str(path.relative_to(root)),
                             "sha256": hashlib.sha256(raw).hexdigest()}) + "\n")
print(raw.decode(), end="")
