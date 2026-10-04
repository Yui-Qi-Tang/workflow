"""Post-run evidence recount; does not dispatch models or change frozen scoring."""
from pathlib import Path
import hashlib,json,sys
from datetime import datetime
BASE=Path(__file__).resolve().parent
sys.path.insert(0,str(BASE/'frozen/controller'))
import loop
from contracts import parse_artifact,validate_artifact,validate_lineage,ContractError
scores=json.loads((BASE/'scores.json').read_text())
audit=dict(cells=[],calls=0,raw_artifacts=0,valid_artifacts=0,invalid_artifacts=[],raw_unchanged=True,input_snapshots_unchanged=True,paired_initial_inputs=True,product_and_rules_unchanged=True)
manifest=json.loads((BASE/'manifest.json').read_text())
audit['frozen_inputs_ok']=all(hashlib.sha256((BASE/p).read_bytes()).hexdigest()==h for p,h in manifest['files'].items())
for case in ('aggregation','conflict','tickets'):
    for source in (BASE/'fixtures'/case).iterdir():
        rel=f'tasker/{case}.md' if source.name=='task.md' else source.name
        expected=hashlib.sha256(source.read_bytes()).hexdigest()
        for effort in ('low','high'):
            inv=json.loads((BASE/'runs'/case/effort/'initial_inventory.json').read_text())
            audit['paired_initial_inputs'] &= inv[rel]==expected
for cell in scores['scores']:
    case,effort=cell['case'],cell['effort'];run=BASE/'runs'/case/effort
    starts=[];ends=[];stages=[]
    for stage in loop.STAGES:
        ev=run/'evidence'/stage
        if not (ev/'dispatch.json').is_file():continue
        d=json.loads((ev/'dispatch.json').read_text());audit['calls']+=1
        starts.append(datetime.fromisoformat(d['prepared_at']));ends.append(datetime.fromisoformat(d['finished_at']))
        assert (ev/'spawn_request.json').is_file()
        assert (ev/'final.txt').is_file(),str(ev/'final.txt')
        out=run/d['output'];record=dict(stage=stage,artifact_exists=out.exists())
        if out.exists():
            audit['raw_artifacts']+=1;audit['raw_unchanged'] &= out.read_bytes()==(ev/'artifact.raw').read_bytes()
            try:
                parsed=parse_artifact(out.read_text());errors=validate_artifact(parsed,stage,case)+validate_lineage(parsed)
            except ContractError as exc:errors=[str(exc)]
            record['validation_errors']=errors
            if errors:audit['invalid_artifacts'].append(dict(case=case,effort=effort,stage=stage,errors=errors))
            else:audit['valid_artifacts']+=1
        else:record['validation_errors']=['not_produced']
        for relative,digest in d['lineage']['input_fingerprints'].items():
            audit['input_snapshots_unchanged'] &= hashlib.sha256((ev/'input_snapshot'/relative).read_bytes()).hexdigest()==digest
        stages.append(record)
    terminal=json.loads((run/'evidence/terminal.json').read_text()) if (run/'evidence/terminal.json').exists() else dict(kind=cell['reason_code'],stage=cell['stopped_stage'])
    audit['cells'].append(dict(case=case,effort=effort,primary_success=cell['primary_success'],elapsed_seconds=round((max(ends)-min(starts)).total_seconds(),2),sum_stage_wall_seconds=round(sum((datetime.fromisoformat(d['finished_at'])-datetime.fromisoformat(d['prepared_at'])).total_seconds() for d in cell['dispatches']),2),terminal=terminal,invocations=stages))
audit['cached_directories']=[str(p.relative_to(BASE)) for p in BASE.rglob('__pycache__')]
for stage in ('',*loop.STAGES):
    audit['product_and_rules_unchanged'] &= (BASE/'frozen/rules'/stage/'AGENTS.md').read_bytes()==(BASE.parent.parent/stage/'AGENTS.md').read_bytes()
for name in ('loop.py','contracts.py'):
    audit['product_and_rules_unchanged'] &= (BASE/'frozen/controller'/name).read_bytes()==(BASE.parent.parent/'agent_loop_poc'/name).read_bytes()
(BASE/'audit.json').write_text(json.dumps(audit,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(audit,ensure_ascii=False))
