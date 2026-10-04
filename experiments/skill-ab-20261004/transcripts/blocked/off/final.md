終止狀態：`waiting_user`，停在 tasker。

- 未載入 skill body；採 `same_invocation`，沒有獨立隔離執行。
- 既有 blocked artifact 驗證退出碼 `0`；SHA-256：`15269cb044077b725a45ba7f0af96d8473a72b11b508b38a40e3ef342e0eb7bf`。
- 驗證後 `next` 仍為 `wait`。未產生報表或下游階段，`report_contents` 未執行。
- 已保存[觀測紀錄](/Users/yuki/workspace/workflow/experiments/skill-ab-20261004/runs/blocked/off/evidence/terminal_observation.json)，保留原 blocked artifact 與自動 audit。

阻塞問題：應計入所有 active rows，還是先取每個 id 的最新 revision，再篩選 active？原任務明確表示 owner 尚未決定。