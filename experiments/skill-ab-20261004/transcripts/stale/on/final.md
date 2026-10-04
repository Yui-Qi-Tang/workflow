終態：`completed`，無阻塞問題。已載入凍結 skill body，採 `same_invocation`，不具獨立階段隔離。

- [報表](/Users/yuki/workspace/workflow/experiments/skill-ab-20261004/runs/stale/on/output/report.json)：`{"total":18,"ids":["a","c","d","f"]}`
- [Review](/Users/yuki/workspace/workflow/experiments/skill-ab-20261004/runs/stale/on/share/case/reviewer/review.md)：五階段重新產生並驗證，全部 exit 0；mirrors 完全一致。
- `report_contents`、欄位與金額核對均通過。
- [完成證據](/Users/yuki/workspace/workflow/experiments/skill-ab-20261004/runs/stale/on/evidence/completion.json)：保留驗證紀錄與自動 audit；未建立 scratch。