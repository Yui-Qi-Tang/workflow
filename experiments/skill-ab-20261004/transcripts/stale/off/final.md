終態：`completed`，路由 `done`，無阻塞問題。

- [報告](/Users/yuki/workspace/workflow/experiments/skill-ab-20261004/runs/stale/off/output/report.json)：`{"total":18,"ids":["a","c","d","f"]}`
- [完整 review](/Users/yuki/workspace/workflow/experiments/skill-ab-20261004/runs/stale/off/share/case/reviewer/review.md)
- 五階段 saved-file validation 全部 exit 0；`report_contents`、`report_schema` 通過；review mirrors byte-identical。
- [最終狀態證據](/Users/yuki/workspace/workflow/experiments/skill-ab-20261004/runs/stale/off/evidence/final-status.txt)
- skill body 未載入。五階段採 `same_invocation`，保留上下文，非獨立隔離審查。