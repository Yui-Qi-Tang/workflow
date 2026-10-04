# workflow-orchestrator skill 對照試跑 — 2026-10-04

本輪有 skill 與無 skill 都通過 3/3 案例，沒有觀察到成功率增益。三個案例各只跑一次；耗時與操作次數有增有減，不能據此宣稱 skill 穩定提高效率，也不能據此判定 skill 無效。

| 案例 | 無 skill 正文 | 有 skill 正文 | 實際結果 |
|---|---:|---:|---|
| 全新任務 | 通過，379.533 秒 | 通過，319.439 秒 | 均完成五階段，報表 total=18、ids=[a,c,d,f] |
| 舊流程成功但原始需求已變更 | 通過，295.765 秒 | 通過，310.361 秒 | 均重新產生五個 revision 與下游鏈，將舊 total=36 改為 18 |
| 業務規則尚待 owner 決定 | 通過，88.323 秒 | 通過，74.520 秒 | 均保留 blocked tasker，停在 waiting_user，沒有報表或下游輸出 |

blocked 案例的「通過」表示正確停止。這是刻意保留的模擬決策缺口，不是需要使用者現在回答的真實阻塞。兩組均重新驗證既有 blocked artifact，驗證 exit 0 後仍遵從 wait；沒有把 schema 合法誤判為可執行。

| 可觀察操作 | 無 skill | 有 skill |
|---|---:|---:|
| 成功案例 / 固定分母 | 3/3 | 3/3 |
| 完成可見工具範圍與 exposure 稽核的通過案例 | 3/3 | 3/3 |
| saved-file validation 失敗 | 0 | 0 |
| saved-file validation 呼叫 | 11 | 15 |
| controller CLI 呼叫 | 40 | 42 |
| shell exec_command 呼叫 | 54 | 56 |
| 三次 elapsed 相加 | 763.621 秒 | 704.320 秒 |

skill 組在 fresh 的 reviewer 階段額外重新驗證四個輸入，所以 validation 呼叫較多。兩组各自選擇不同的工具批次方式，不能用外層工具封裝次數代替實際 shell 或 CLI 呼叫數。總 elapsed 較短約 7.8% 僅描述本輪觀察；各次包含模型、工具與排程時間，配對之間只有單次樣本，不能當成可重複的加速比例。

六個受測子代理均為 fresh invocation、`fork_turns=none`，未指定模型或推理覆寫；實際 session metadata 全部是 **gpt-6-astra / ultra**。這一輪沒有比較 Luna low/high。每個受測代理在自己的目錄內依序操作五階段，使用明示的 `same_invocation` fallback，因此角色之間沒有獨立上下文隔離。主代理設計、凍結、評分與下結論；沒有替受測代理修補檔案、提示答案或另開重試。每格限時 600 秒，六格均在期限內完成。

兩組共有相同現行 AGENTS、README、controller 0.3.0、資料、任務與透明 CLI recorder。唯一預定介入是有無凍結 skill 正文，以及明確要求載入與使用它的開關；每對的初始共同檔案完全一致，派送文字正規化路徑與開關後也相同。skill 組先透過 `load_skill.py` 載入正文；對照組未讀取任何 skill 正文。現行 AGENTS/README 已包含大部分相關操作規則，因此本輪測的是這個基線上的額外效果。

成功標準在派送前固定：[protocol.json](protocol.json)、[evaluate.py](evaluate.py)、[manifest.json](manifest.json)。評分同時檢查：獨立報表 oracle 或預期阻塞、實際終態、schema 與 lineage、每份最終產物對應的 saved-byte validate digest 及交接前時序、保護檔案完整性。stale 額外要求全部五個 seed revision 被替換。完整分母保持六格，沒有排除失敗或未知樣本；本輪沒有 timeout、驗證失敗或資格未知格。最終數據見 [scores.json](scores.json)、[metrics.json](metrics.json)。

範圍與 treatment 稽核以完整可見工具呼叫、工具回應、CLI receipts 和 loader receipts 為依據。主代理逐一閱讀了全部 79 個外層工具呼叫的內容，其中含 110 次 shell exec_command；未觀察到越界讀寫、對照組讀取正文、繞過 recorder、修改 audit 或與其他代理溝通。各次工具呼叫均有對應回應，沒有不完整 JSONL 行。詳細判定在 `compliance/`，公開工具與最終回覆在 `transcripts/`，原始產物及 CLI bytes 在 `runs/*/*/audit/`。既有 synthetic fixtures 另存於 `fixtures/`，不視為受測代理表現。

這個稽核仍有界線：目錄限制是指令限制，沒有另建 OS sandbox；工具紀錄能確認載入與操作，不能證明模型內部採用了哪一條 skill 規則。runtime 將 NEW_TASK/spawn 訊息加密保存，無法拿保存的密文與正文做位元組比對；主代理實際提交的凍結明文另存於 `dispatch/`。[dispatch-index.json](dispatch-index.json) 對應 frozen prompt hash、派送紀錄與 child thread ID；六個 child 收到的密文 hash 都與 parent 保存的 spawn 參數一致，但這仍不是獨立的明文相等證明。沒有匯出私人推理、加密內容或帳號資訊。

雙方可能都看到相同 skill 名稱、描述及 optional link。本輪排除的是對照組讀取正文，不是對 skill 完全不知情；測試包含「閱讀、注意與使用正文」這整個介入，沒有等長 generic prompt 對照，也沒有測自動觸發。sampling seed、temperature 與 provider snapshot 不可指定或核對。累計 token 紀錄保存在 metrics，包含重複及快取 input，不代表唯一 prompt 長度，也沒有推算金額。

檔案完整性檢查見 [integrity.json](integrity.json)：100 份凍結檔未變、452 份既有專案檔未變。新資料僅為本次實驗與主代理行政五階段紀錄；沒有修改 skill 或產品程式來迎合結果。setup 初次在任何受測派送前遇到 `KINDS` import 錯誤，修正後才完成凍結；這是準備階段問題，沒有計入受測格重試。凍結後未修改 scorer、fixtures 或評分標準。所有六格原始產物、失敗紀錄（若有）、工具紀錄與評分均保留。

我建議保留 skill 作為集中操作入口；這是導航與文件組織上的維護選擇，不是本次實驗證實的操作負擔或可靠性收益。兩組全數通過，也可能表示這三個案例在目前模型設定下不足以區分兩種處置；結果沒有證明兩組等效。若要接續評估，應另立新 protocol，固定模型後增加每個案例的重複次數，並加入更長、較容易漏掉交接細節的案例；若要研究 Luna，另用相同 Luna 設定做 skill on/off，避免同時改變推理強度。
