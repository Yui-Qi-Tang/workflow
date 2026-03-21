# Workflow README / 工作流程說明

這個 repository 模擬一個 staged AI-agent workflow：

`tasker -> researcher -> planner -> implementer -> reviewer`

workflow 規則仍以各層級的 `AGENTS.md` 為準。
這份文件是給人看的中文版本，方便你介紹流程、撰寫任務，並引導 agent 安全切任務。

## 目錄對照

- `tasker/{task_id}.md`：使用者輸入的任務檔
- `share/{task_id}/researcher/task.md`：正規化後的任務規格
- `share/{task_id}/planner/plan.md`：高層執行計畫
- `share/{task_id}/implementer/impl.md`：實作交接文件
- `share/{task_id}/reviewer/{task.md,plan.md,impl.md,result.md,review.md}`：自包含的審查 bundle
- `share/{task_id}/loop/`：任務需要迭代時的可選 loop 狀態與追蹤文件

## 如何撰寫 `task.md`

最好的 `task.md` 會明確寫出要做什麼、不能做什麼，以及怎麼驗收。

本 workflow 必填欄位是：

- `task_id`
- `goal`
- `scope`
- `constraints`
- `deliverables`
- `acceptance_criteria`
- `open_questions`

好的任務通常也會包含：

- `source_of_truth`
- `validation`
- `rollback / cleanup`
- `notes`

你可以直接套用下面這個模板：

```md
# Goal
- 你希望最後得到什麼結果？

# Scope
- 哪些檔案、系統或文件在範圍內？

# Source Of Truth
- 哪些檔案、頁面、票據或範例是權威來源？

# Constraints
- 哪些內容不能改？
- 哪些內容必須保留？
- 哪些內容不能自行推測或補齊？

# Deliverables
- 最後要產出什麼？
- 要用什麼格式？

# Validation
- 需要通過哪些檢查？

# Acceptance Criteria
- 成功的樣子是什麼？

# Rollback / Cleanup
- 哪些暫存檔、測試輸出或 scratch artifact 要清掉？
- 哪些要保留？

# Open Questions
- 哪些內容在實作前一定要先確認？
```

實務上請記住這條規則：

- 只要一個決策會影響實作、驗證、範圍或清理，就應該寫進 `task.md`，
  不要留給後面的 agent 猜。

## 各 Agent 責任與邊界

| Agent | 責任 | 邊界 |
| --- | --- | --- |
| `tasker` | 將原始需求整理成有界任務規格。 | 遇到衝突必須停止，不能自行腦補缺失需求。 |
| `researcher` | 重述任務、分類、找風險與失敗模式。 | 不能寫程式，也不能放寬限制。 |
| `planner` | 將任務轉成有順序的實作步驟、不變量、驗證與升級條件。 | 不能掩蓋上游缺口，也不能給模糊指引。 |
| `implementer` | 保守地執行、驗證，並記錄改了什麼。 | 不能擴大範圍，也不能偷改計畫。 |
| `reviewer` | 判斷是否成功、找出最早的失敗來源，並正確導回上游。 | 不能直接修程式，也不能捏造證據。 |

## 如何引導我自行切割任務

如果你想把大任務切成小任務，請明確告訴我：

- 最終想要的結果
- 我應該信任哪些來源
- 哪些部分可以並行
- 哪些部分必須依序做
- 你在意哪些驗證

你可以這樣下指令：

```text
先幫我把這個需求切成可並行的 subtask。
請標出哪些部分會互相撞檔案、哪些可以獨立做。
如果你發現 validation、cleanup、rollback 不完整，請先提出 task update。
```

更好的做法，是先叫我把 task 檔整理出來：

```text
請先把這個需求整理成 task.md，包含 goal / scope / constraints /
deliverables / acceptance_criteria / open_questions。
如果有衝突，先停下來列出衝突點，不要自己補。
```

這樣做的好處是：

- 我可以把任務切成彼此獨立的執行單元。
- 我可以很早提醒你哪裡的需求還不夠明確。
- 我可以在實作前先提議最乾淨的 loop 邊界。

## Agent Loop 範例

基本流程是：

`tasker -> researcher -> planner -> implementer -> reviewer`

具體跑法如下：

1. 你先描述需求，我把它整理成 `tasker/{task_id}.md`。
2. `tasker` 會把需求正規化成 `share/{task_id}/researcher/task.md`。
3. `researcher` 會保留原意、找出風險、重述任務。
4. `planner` 會把重述後的任務轉成實作計畫。
5. `implementer` 會依計畫執行並寫出結果。
6. `reviewer` 會判斷 workflow 是否成功。
7. 如果失敗，reviewer 會指出最早的失敗來源。

這個 repo 也有一個簡化版 loop POC：

- `agent_loop_poc/README.md`

範例指令：

```bash
python3 agent_loop_poc/loop.py init 24
python3 agent_loop_poc/loop.py sync 24
python3 agent_loop_poc/loop.py next 24
python3 agent_loop_poc/loop.py status 24
```

好的 loop 行為應該是：

- 上游定義有問題時要提早停下
- 回到真正造成 mismatch 的最早 stage
- 讓 review bundle 自給自足
- 在修正執行路徑時，保留原始任務意圖

## 好的 Task Loop 長什麼樣子

我們已經在兩種很實用的情境中用過這個 workflow：

- contract mismatch 任務：在實作前就必須先停下來，先修定義。
- source synthesis 任務：從多個頁面抽事實，把直接發現與支援訊號分開，並清楚標示推論。

這些例子代表我們想要的風格：

- 來源依據要明講
- 下游 agent 要窄、要有邊界
- 不要讓實作去猜任務真正意思
- 讓 reviewer 能說明失敗來源，而不只是說失敗了

## [Review] 這個 workflow 還沒完全發揮的用法

下面這些都是合法而且實用的用法，但你可能還沒完全用到。
我先標成 `[Review]`，方便你逐條 review。

- `[Review]` 先讓我根據一個粗略想法加上幾份來源文件，幫你起草 `task.md`，如果需求有衝突或不夠明確就先停下來。
- `[Review]` 在實作前先讓我把一個大任務切成多個小任務，並且標出明確的檔案 ownership。
- `[Review]` 當我發現缺少 validation、cleanup、rollback 或 reporting 要求時，先幫你提出 task update 建議。
- `[Review]` 先讓我寫 loop 邊界與升級條件，再只在那個邊界內實作。
- `[Review]` 讓我扮演 contract reviewer，比對兩份 artifact，找出最早失去原始意圖的上游 stage。
- `[Review]` 讓我產出自包含的 review bundle，而不是只給最終答案，讓下一階段直接讀檔。
- `[Review]` 當任務需要重複迭代時，讓我建立可重用的 loop-state artifact。

## 維持流程健康的規則

- 以 `tasker/{task_id}.md` 作為任務內容的權威來源。
- 在 reviewer 開始前，review bundle 必須自包含。
- 不要依賴 stage 之間的聊天記憶。
- 任務沒定義驗證方式，就不要自己發明。
- 不要為了讓實作容易而偷偷放寬限制。
- 如果任務需要改規則，先更新 task，再重新跑 pipeline。

## 下一步可看哪裡

- 工作流程總規則：`./AGENTS.md`
- 各 stage 的專屬規則：`./tasker/AGENTS.md`, `./researcher/AGENTS.md`, `./planner/AGENTS.md`, `./implementer/AGENTS.md`, `./reviewer/AGENTS.md`
- Loop POC：`./agent_loop_poc/README.md`

