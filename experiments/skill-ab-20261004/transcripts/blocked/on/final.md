終態：`waiting_user`，停在 tasker；未產生 report 或後續階段。

- 已載入凍結 skill；採 `same_invocation`，不具獨立階段隔離。
- 既有 tasker artifact 的 `validate` exit 0；SHA-256：`15269cb044077b725a45ba7f0af96d8473a72b11b508b38a40e3ef342e0eb7bf`。
- 再查路由仍為 `wait`；`public_check.py` 未執行。
- 觀察紀錄：[terminal-observation.json](/Users/yuki/workspace/workflow/experiments/skill-ab-20261004/runs/blocked/on/evidence/terminal-observation.json)。
- 阻擋問題：owner 尚未選擇「全部 active rows」或「每個 id 先取最新 revision，再篩 active」。