"""Public report check; fixtures and this file are read-only trial inputs."""
from pathlib import Path
import json

root = Path(__file__).resolve().parent
latest = {}
for row in json.loads((root / "records.json").read_text()):
    if row["id"] not in latest or row["revision"] > latest[row["id"]]["revision"]:
        latest[row["id"]] = row
active = [row for row in latest.values() if row["state"] == "active"]
expected = {"total": sum(row["amount"] for row in active), "ids": sorted(row["id"] for row in active)}
actual = json.loads((root / "output/report.json").read_text())
assert actual == expected, (actual, expected)
print("report_contents: passed")
