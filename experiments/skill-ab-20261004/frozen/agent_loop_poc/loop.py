"""Transparent trial-only CLI recorder. The frozen controller is unchanged."""
from pathlib import Path
import contextlib, hashlib, io, json, sys, time, uuid

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent / "core"))
import loop as controller

def snapshot():
    result = {}
    for path in sorted((ROOT / "share/case").rglob("*.md")):
        raw = path.read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        blob = ROOT / "audit/blobs" / digest
        blob.parent.mkdir(parents=True, exist_ok=True)
        if not blob.exists():
            blob.write_bytes(raw)
        result[str(path.relative_to(ROOT))] = {"sha256": digest, "mtime_ns": path.stat().st_mtime_ns}
    return result

def main():
    args = sys.argv[1:]
    if "--root" in args and Path(args[args.index("--root") + 1]).resolve() != ROOT:
        raise ValueError("This trial recorder may only operate on its own root")
    start = time.time_ns()
    before = snapshot()
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        try:
            code = controller.main(["--root", str(ROOT), *args])
        except SystemExit as exc:
            code = exc.code or 0
    receipt = {"start_ns": start, "end_ns": time.time_ns(), "argv": args,
               "exit_code": code, "stdout": out.getvalue(), "stderr": err.getvalue(),
               "artifacts_before": before, "artifacts_after": snapshot()}
    folder = ROOT / "audit/cli"
    folder.mkdir(parents=True, exist_ok=True)
    (folder / f"{start}-{uuid.uuid4().hex}.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(out.getvalue(), end="")
    print(err.getvalue(), end="", file=sys.stderr)
    return code

if __name__ == "__main__":
    raise SystemExit(main())
