# Workflow README / 工作流程說明

這個 repository 模擬一個 staged AI-agent workflow：

`tasker -> researcher -> planner -> implementer -> reviewer`

README 只負責說明給人看。真正的 workflow 規則、輸出 schema、stage
邊界，以 root `AGENTS.md` 和各 stage 最近的 `AGENTS.md` 為準。

## 目錄對照

- `tasker/{task_id}.md`：使用者輸入的任務檔
- `share/{task_id}/researcher/task.md`：`normalized_task` JSON artifact
- `share/{task_id}/planner/plan.md`：`research_plan` JSON artifact
- `share/{task_id}/implementer/impl.md`：`implementation_brief` JSON artifact
- `share/{task_id}/reviewer/result.md`：`implementation_result` JSON artifact
- `share/{task_id}/reviewer/review.md`：`workflow_review` JSON artifact
- `share/{task_id}/reviewer/{task.md,plan.md,impl.md,result.md,review.md}`：
  自包含 review bundle
- `share/{task_id}/loop/`：任務需要迭代時的可選 loop 狀態與追蹤文件

artifact 檔名暫時仍保留 `.md`，方便遷移；但 handoff 內容必須是一個合法
JSON object，不再是自由格式 Markdown。

## Artifact 邊界

JSON artifact 是 agent 之間唯一的 handoff 邊界。每個 handoff artifact
都必須包含 root `AGENTS.md` 定義的共用欄位：

- `schema_version`
- `artifact_type`
- `task_id`
- `produced_by`
- `status`
- `input_artifacts`
- `trusted_sources`
- `untrusted_inputs_seen`
- `constraints`
- `open_questions`
- `evidence`
- `handoff`

各 stage 的 `AGENTS.md` 會定義該 stage 額外必填欄位與 enum 值。

## 各 Agent 責任與邊界

| Agent | Artifact | 責任 | 邊界 |
| --- | --- | --- | --- |
| `tasker` | `normalized_task` | 將原始需求整理成有界任務規格。 | 遇到衝突必須 blocked，不能自行腦補缺失需求。 |
| `researcher` | `research_plan` | 重述任務、分類、找風險與失敗模式。 | 不能寫程式，也不能放寬限制。 |
| `planner` | `implementation_brief` | 將任務轉成有順序的實作步驟、不變量、驗證與升級條件。 | 不能掩蓋上游缺口，也不能給模糊指引。 |
| `implementer` | `implementation_result` | 保守地執行、驗證、cleanup，並記錄改了什麼。 | 不能擴大範圍，也不能偷改計畫。 |
| `reviewer` | `workflow_review` | 判斷是否成功、驗證 artifact、找出最早失敗來源並導回上游。 | 不能直接修程式，也不能捏造證據。 |

## Context Isolation / 遺忘邊界

這個 workflow 的設計目標是：每個 stage 都用新的 model invocation。

真正的 stage-to-stage 遺忘，只有在 runner 開新 invocation，且只傳入以下內容
時才成立：

- root `AGENTS.md`
- 該 stage 的 `AGENTS.md`
- 當前 stage 必要的 input artifact
- artifact 明確授權讀取的檔案

如果只是在同一段對話中寫「請忘記前文」，那只是 soft instruction，不能保證
前面的對話狀態或隱含推理已經從 context 移除。比較可靠的做法，是讓每次
handoff 都只靠小而明確的 JSON artifact。

就算暫時無法做到完美隔離，JSON artifact 仍然有價值，因為它能讓 drift、
缺少 evidence、非法 enum、沒有根據的成功宣告更容易被 runner 或 reviewer
抓出來。

## 如何撰寫 Task Input

使用者輸入的 task file 可以仍然是自然語言 Markdown，但最好明確寫出：

- 最終目標
- scope 與 non-scope
- source of truth，例如檔案、頁面、ticket、範例
- 不能放寬的 constraints
- deliverables
- validation expectations
- cleanup 或 rollback expectations
- 實作前必須釐清的 open questions

只要一個決策會影響實作、驗證、範圍、cleanup、rollback 或 reporting，就應該
寫進 `tasker/{task_id}.md`，不要留給後面的 agent 猜。

## Loop POC

這個 repo 有一個簡化版 loop POC：

- `agent_loop_poc/README.md`
- `agent_loop_poc/loop.py`

範例指令：

```bash
python3 agent_loop_poc/loop.py init 24
python3 agent_loop_poc/loop.py sync 24
python3 agent_loop_poc/loop.py next 24
python3 agent_loop_poc/loop.py status 24
```

POC 會優先讀 JSON artifact，並保留舊 Markdown label 的 fallback，方便舊資料
過渡。

## 維持流程健康的規則

- `AGENTS.md` 是權威規則，README 只是說明文件。
- reviewer 開始前，review bundle 必須自包含。
- stage 之間只用 JSON artifact handoff。
- 不要依賴 stage 之間的聊天記憶。
- 任務沒定義 validation、cleanup、rollback 或 approval，就不要自己發明。
- 不要為了讓實作容易而偷偷放寬 constraints。
- 如果任務需要改規則，先更新 task，再重新跑 pipeline。

## 下一步可看哪裡

- 工作流程總規則：`./AGENTS.md`
- 各 stage 的專屬規則：`./tasker/AGENTS.md`, `./researcher/AGENTS.md`,
  `./planner/AGENTS.md`, `./implementer/AGENTS.md`, `./reviewer/AGENTS.md`
- Loop POC：`./agent_loop_poc/README.md`
