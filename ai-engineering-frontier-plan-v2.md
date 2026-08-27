# AI Engineering 研究前線：30 天讀懂一週一週長出來的技術脈絡

## 執行版 V2：Local Engineering Knowledge Assistant

> 參賽標題已固定，本文件調整的是專案內容、難度與執行方式，不修改報名標題。

## 1. 專案定位

這是一個給「用過 ChatGPT、Claude、Gemini 等網頁對話式 AI，但想自己架設本地 AI 系統」的初學者之 30 天實作系列。

讀者不需要先懂 Machine Learning、Transformer、向量資料庫或 Agent framework。每天只引入一個必要概念，跟著文章、程式碼與 Git commit 前進，最後完成一個可以在自己電腦上執行的：

> **Local Engineering Knowledge Assistant**

它可以：

1. 在本地執行 LLM。
2. 讀取讀者自己的 Markdown 或文字文件。
3. 找出與問題相關的內容。
4. 產生附來源的回答。
5. 在沒有答案時明確表示不知道。
6. 使用一個受限制的本地工具完成簡單任務。
7. 以受限制的任務流程串起查詢、工具與驗證。

30 天結束時，讀者拿到的不只是文章，而是一套可以替換資料、Prompt、工具與模型的最小本地 AI 架構。

## 2. 給讀者的學習承諾

每篇文章都要讓讀者完成一個看得見的進度。文章結尾固定回答四件事：

```text
今天增加了什麼？
它解決了什麼問題？
讀者可以執行哪一個命令？
下一步為什麼需要新的能力？
```

讀者的預期進度：

| 時間點 | 讀者能拿到的成果 |
|---|---|
| Day 2 | 在本機成功呼叫模型 |
| Day 3 | 擁有可重複執行的最小 Chat Runner |
| Day 7 | 擁有可重複使用的本地聊天程式 |
| Day 14 | 能用自己的文件建立第一版知識庫問答 |
| Day 21 | 能讓 AI 呼叫一個安全的本地工具 |
| Day 27 | 擁有有步數限制、錯誤處理與驗證的 Agent |
| Day 30 | 完整架構、benchmark、結果與可延伸 Repo |

## 3. 範圍控制

### 必須完成

```text
Local LLM
    ↓
可重複呼叫的 Chat Runner
    ↓
knowledge/raw：原始文件
    ↓
deterministic ingest：metadata、hash、chunk
    ↓
knowledge/wiki：可讀的 source、concept、howto
    ↓
可重建的 FTS／Embedding index
    ↓
budget-aware retrieval / context builder
    ↓
一個 Read-only Tool
    ↓
受限制的任務流程
    ↓
Evaluation 與完整 README
```

### 延伸內容，不影響完賽

以下內容只在核心系統穩定後加入：

- Reranker
- MCP
- 向量資料庫服務化
- 長期外部記憶
- 多 Agent
- DFlash2 / speculative decoding
- 完整 Observability Dashboard

不要讓延伸內容阻塞 Day 30 的最小可用系統。

## 4. 知識保存層 + RAG 架構

本專案從「原始資料、可讀整理、可重建索引」這個一般性的資料工程需求出發，設計簡化的知識保存層與 RAG。它可以與個人的 Miracle Vault 互通，但不複製任何既有專案的命名、目錄、程式或文章敘事，也不把完整 Obsidian Vault 或完整 LLM 編譯流程當成必要依賴。

### 三層責任

```text
Knowledge Layer
  raw/       原始證據，保留原貌
  wiki/      人類可讀的整理與壓縮

Retrieval Layer
  manifest   文件版本、hash、metadata
  index      FTS/BM25/embedding，可刪除後重建

Context Layer
  選擇少量證據、去重、排序、截斷
  送入 Local LLM 產生附來源回答
```

資料保存的優先順序是：

```text
raw 是 source of truth
wiki 是 curated knowledge layer
index 是 derived artifact
```

`index.md`、`overview.md` 與 `log.md` 是人類和 LLM 的導航層，不取代機器搜尋索引。查詢時不把完整的 index、overview 或 log 送進模型，而是從索引找回少量、有來源定位的 chunks。

### 查詢流程

```text
使用者問題
    ↓
metadata filter
    ↓
keyword / FTS + embedding retrieval
    ↓
候選 chunks 去重與排序
    ↓
context budget 檢查
    ↓
evidence pack
    ↓
Local LLM
    ↓
回答、引用、log
```

可用 context 預算應明確計算：

```text
retrieval_budget =
  context_window
  - system_prompt
  - tool_schemas
  - conversation_history
  - output_reserve
```

wiki 摘要與 raw chunk 不應重複大量放入同一次請求。wiki 用來幫助導覽與提供背景，raw chunk 用來提供最終證據。

### Miracle-lite 的必要頁型

第一版只需要四種頁型：

- `source`：單一文件或來源的摘要與 provenance
- `concept`：跨來源的可重用概念
- `howto`：讀者可以照做的操作流程
- `derived`：查詢、比較或實驗產出的分析

`entity`、GraphRAG、複雜 backlink graph 都先列為延伸內容。

### 外部 Vault 使用規則

`/Users/gilbert/Miracle/AI/` 可以作為進階 dogfood corpus，但必須以唯讀外部路徑使用，不要寫死在程式中，也不要把個人 Vault 或大型 raw assets 提交到參賽 Repo。初學者第一版使用專案內的 `knowledge/raw/` 範例文件。

## 5. 系統故事：從聊天到知識助理

整個系列只使用一個持續演進的案例：

```text
使用者：部署服務前要檢查哪些設定？

Day 3：模型直接回答
Day 7：模型遵守固定回答格式
Day 14：模型先從整理後的知識層找證據，再用 RAG 回答
Day 21：模型可以查詢文件目錄與檢查設定
Day 27：模型會判斷是否需要工具，且最多執行 3 步
Day 30：系統有來源、評估、日誌與安全限制
```

建議使用一組自己撰寫、可公開的虛構工程文件，例如：

```text
knowledge/raw/sample_docs/
├── deployment-guide.md
├── api-spec.md
├── incident-runbook.md
├── service-config.md
└── release-policy.md
```

文件可以刻意放入只有資料集才知道的版本號、服務名稱與設定值，避免模型憑既有知識猜答案。資料集必須包含：

- 有明確答案的題目
- 需要跨文件查找的題目
- 文件中沒有答案的題目
- 可能受到 Prompt Injection 影響的文件內容
- 至少一組工具任務

## 6. 建議實驗環境

### 主要模型

計劃書原本指定的 `Qwen3.8-27B-DFlash2` 需要修正。DFlash2 是搭配 target model 使用的 draft model，不是可獨立執行的 27B 語言模型。

建議記錄為：

```text
Target model: Qwen/Qwen3.8-27B
Apple Silicon artifact: mlx-community/Qwen3.8-27B-4bit
Optional draft model: incoai/Qwen3.8-27B-DFlash2
```

參考：

- [Qwen/Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)
- [MLX 4-bit 版本](https://huggingface.co/mlx-community/Qwen3.8-27B-4bit)
- [DFlash2 模型說明](https://huggingface.co/incoai/Qwen3.8-27B-DFlash2)

32GB Mac 應以 4-bit 版本作為起點。模型是否能穩定支援 8K 或 16K context，必須以實測結果為準；32K 只列為挑戰項目。

### Runtime 原則

第一週只選一個主要 runtime，避免讀者同時安裝太多框架。優先採用能在 Apple Silicon 上穩定執行、並提供 OpenAI-compatible API 的本地 runtime。

### Python 版本策略

不要把目前電腦上的 `python3` 版本直接當成專案基線。Python 3.9 已結束官方支援；本專案以 Python 3.13.x 作為主要教學與測試版本，Python 3.12 作為保守相容版本，Python 3.14 則在主要依賴完成 smoke test 後再列入相容性測試。`pyproject.toml` 應在 Day 2 建立後明確寫出版本範圍，避免讀者不小心使用系統 Python。

後續程式碼盡量透過統一的 `LLMClient` 呼叫模型：

```python
client.chat(messages, tools=None, response_format=None)
```

如此讀者日後換模型或 runtime 時，不需要重寫 RAG 與 Agent。

### 降級路徑

如果 27B 模型在實際 Mac 上無法穩定執行，降級順序如下：

1. 維持同一個 target model，改用較小 context。
2. 改用同一系列較小的 MLX 模型完成教學。
3. 保留 27B 作為效能與品質附錄。

降級時不要改變後續 API、資料格式與架構，讓讀者仍然能完成整個系列。

## 7. 30 天文章與 Git 產出

每一天都要有一個可執行 commit。文章可以記錄失敗，但不能只有概念介紹。

### Week 1：從網頁聊天走到本地模型

| Day | 文章主題 | 當日可見成果 | Git 產出 |
|---:|---|---|---|
| 1 | 這 30 天要做什麼？ | 專案規則、環境檢查表 | `day01: add project scope` |
| 2 | 第一次在本機呼叫模型 | 一個最小 `frontier_knowledge.py` | `day02: call local model` |
| 3 | 建立 Baseline Chat Runner | 可重複執行的 CLI | `day03: add baseline runner` |
| 4 | Prompt 到底改變了什麼？ | 基本 system prompt | `day04: add system prompt` |
| 5 | 讓回答固定格式 | JSON 或 Markdown answer schema | `day05: add answer schema` |
| 6 | Context 與對話記憶 | Session history | `day06: add session context` |
| 7 | 第一週回顧：本地聊天系統 | 可獨立執行的 checkpoint | `day07: checkpoint-chat` |

第一週不介紹 RAG、Agent 或 MCP。目標只有一個：讓第一次接觸本地 AI 的讀者確定自己能跑起來。

### Week 2：建立知識保存層與 RAG

| Day | 文章主題 | 當日可見成果 | Git 產出 |
|---:|---|---|---|
| 8 | 準備自己的工程文件 | `knowledge/raw` 與文件格式 | `day08: add raw documents` |
| 9 | Ingest 不只是複製檔案 | metadata、hash、chunk manifest | `day09: add deterministic ingest` |
| 10 | 先不用向量資料庫：關鍵字搜尋 | SQLite FTS/BM25 retriever | `day10: add lexical retrieval` |
| 11 | 如何整理可維護的知識頁？ | 第一個 source 與 howto 頁面 | `day11: add wiki knowledge layer` |
| 12 | 三種證據路徑怎麼比較？ | raw、wiki、hierarchical 三組比較 | `day12: compare retrieval paths` |
| 13 | 讓有限 context 用在刀口上 | context budget、去重、排序 | `day13: add context builder` |
| 14 | 組出有來源的 RAG | citation、no-answer、可重建索引 | `day14: checkpoint-rag` |

`index.md` 是人類可讀的導航；SQLite FTS／embedding index 是機器查詢層，兩者要分開。先用 SQLite 或 JSON 建立最小索引，不要求讀者一開始就安裝獨立 Vector Database。向量資料庫服務化放在延伸文章中。

### Week 3：讓 AI 開始做安全的小事

| Day | 文章主題 | 當日可見成果 | Git 產出 |
|---:|---|---|---|
| 15 | 知道答案與執行動作的差別 | Tool schema 概念 | `day15: add tool schema` |
| 16 | 第一個工具：文件目錄查詢 | 唯讀、無副作用工具 | `day16: add document catalog tool` |
| 17 | 第二個工具：設定檢查 | 只讀取允許資料與回傳檢查結果 | `day17: add config check tool` |
| 18 | AI 如何選擇工具？ | tool router | `day18: add tool routing` |
| 19 | 工具叫錯怎麼辦？ | argument validation 與錯誤訊息 | `day19: validate tool calls` |
| 20 | MCP 解決了什麼問題？ | 直接工具與 MCP 的小比較 | `day20: optional mcp adapter` |
| 21 | 第三週回顧：安全工具層 | 可重複執行的 tool checkpoint | `day21: checkpoint-tools` |

Day 20 的 MCP 是 optional。即使跳過，讀者仍然能完成後續 Agent 與最終系統。

### Week 4：從工具呼叫走到受限制的任務流程

| Day | 文章主題 | 當日可見成果 | Git 產出 |
|---:|---|---|---|
| 22 | 工具呼叫和任務流程的差別 | 最小規劃 → 執行 → 驗證流程 | `day22: add task workflow` |
| 23 | Agent 為什麼會失控？ | max steps、timeout、allowlist | `day23: add agent limits` |
| 24 | 失敗後要不要重試？ | bounded retry | `day24: add bounded retry` |
| 25 | Verifier 能不能檢查答案？ | generator → verifier | `day25: add verifier` |
| 26 | 記憶先從 Session State 開始 | 可重設的短期記憶 | `day26: add session state` |
| 27 | Prompt Injection 與安全邊界 | 不信任文件、工具與輸入 | `day27: add safety checks` |

這一週不做多 Agent、不開放 shell、不讓模型自行修改檔案。Agent 的預設工具必須是唯讀，最多 3 步，並且每一步都留下 log。

### Week 5：評估、包裝與交付

| Day | 文章主題 | 當日可見成果 | Git 產出 |
|---:|---|---|---|
| 28 | 「感覺比較好」不算評估 | 固定 benchmark dataset | `day28: add evaluation set` |
| 29 | 把系統交給讀者 | README、啟動指令、簡易本地 UI 或 API | `day29: improve onboarding` |
| 30 | 30 天後系統變強多少？ | 完整結果、架構圖、限制與 roadmap | `day30: release v1.0` |

## 8. 每日文章與寫作規範

每篇參賽文章都使用 Markdown，儲存在 `articles/dayNN.md`。文章要讓初學者跟得上，但不使用完全相同的段落模板；每一天的內容依實際做過的實驗安排。

文章至少交代：

- 今天實際處理的問題，以及昨天的版本卡在哪裡。
- 今天新增或移除的程式、資料或設定。
- 讀者可以執行的命令、看到的結果，或目前還沒成功的地方。
- 一個具體取捨，說明為什麼現在選這個做法。
- 當天的 Git commit，以及下一步要驗證的問題。

不要為了湊齊格式而虛構成功畫面、個人故事或漂亮結論。真的沒有結果，就把「尚未完成」寫清楚；技術細節需要較正式的語氣時，也不必硬改成口語。

完整的台灣繁體中文、Markdown 與去公式化寫作規範放在 [`docs/article-style.md`](docs/article-style.md)。

每篇文章提供三個難度標籤：

```text
Level 1：照著做，成功跑起來
Level 2：修改自己的文件或設定
Level 3：修改程式，加入自己的工具
```

主文只要求 Level 1；Level 2、Level 3 放在延伸閱讀，避免初學者被額外細節卡住。

## 9. Benchmark 設計

不要等到 Day 28 才第一次評估。Day 3 先建立最小版本，之後逐步增加題目。

建議第一版包含 30 題：

```text
10 題：文件中有明確答案
5 題：需要跨兩份文件
5 題：文件中沒有答案，應該拒答
5 題：會誘導模型忽略來源的文件內容
5 題：需要工具完成的任務
```

### Miracle-lite 消融實驗

固定同一模型、文件、問題、生成參數與 context budget，至少比較三條路徑：

```text
A. Direct RAG
   raw documents → chunks → retrieval → answer

B. Miracle RAG
   wiki pages → retrieval → answer

C. Hierarchical RAG
   metadata/source/concept → raw evidence chunks → answer
```

C 是本專案預期的主架構，但不能先假設它一定最好。必須用資料證明它是否在相近 token 預算下帶來更好的回答品質、引用正確率或檢索命中率。

主要指標：

| 類別 | 指標 |
|---|---|
| 回答品質 | answer accuracy、citation correctness、abstention accuracy |
| Retrieval | Recall@K、命中正確 chunk 的比例 |
| Tool | tool selection、argument validity、task success |
| Agent | completion rate、step count、retry count |
| Context | input tokens、retrieval tokens、context utilization、重複內容比例 |
| 效能 | TTFT、總延遲、output tokens/s |
| 資源 | peak memory、模型載入時間、索引大小 |

每次實驗固定保存：

```text
model_id
model_revision
runtime_version
hardware
prompt_config
retrieval_config
generation_config
raw_output
metrics
timestamp
```

品質與效能分開報告，不使用一個沒有明確意義的總分掩蓋取捨。

### Context 組裝規則

Context builder 的最低要求：

1. 固定 system prompt、工具 schema 與 output reserve。
2. 先做 metadata filter，再做 lexical／embedding retrieval。
3. 對相同文件或相鄰 chunks 去重。
4. 優先保留有標題、來源與行號的證據。
5. 超過 retrieval budget 時，截斷候選，不直接擴大 context。
6. 保存「被選入」與「被淘汰」的候選，方便日後診斷 retrieval 失敗。

## 10. Git 日更規則

### 每天至少完成

- 一篇文章草稿或正式文章
- 一個可執行的程式或資料變更
- 一次 `git push`
- 一個結果或失敗紀錄

### Commit 命名

```text
day01: add project scope
day02: call local model
day13: add rag pipeline
day30: release v1.0
```

### Tag 建議

```text
day07-chat
day14-rag
day21-tools
day27-agent
v1.0
```

### 不應提交的內容

- 模型權重
- API key
- 個人文件
- `.env`
- 可能包含個資的原始對話
- 沒有授權的網路文章全文

## 11. 原創性與參賽合規

本專案不以 KeSi 或其他參賽作品作為程式、架構或文章的模板。外部作品最多只能用來辨識常見工程風險；本專案的需求、設計決策、程式碼、範例資料與文章均由本專案獨立產生。

### 明確排除的相似性

- 不使用其他作品的專案名稱、主程式名稱、類別名稱或命令名稱。
- 不沿用其他作品的目錄配置、模組切分、工具清單、示範案例或文章順序。
- 不複製程式碼、段落、標題、圖表、畫面、Prompt、commit 訊息或具有辨識度的敘事句型。
- 不把「逐日增加一個 coding agent 能力」當成本文系列的主軸；本系列主軸是文件資料如何經過保存、整理、檢索、上下文控制與驗證，形成知識助理。

### 建立自己的來源與設計證據

在開始正式連載前建立以下文件，並隨 Git 歷史逐日更新：

```text
docs/
├── design-decisions.md   # 本專案為何採用這個資料流與邊界
├── sources.md            # 外部文件、套件與概念的來源
└── originality-check.md  # 發文前的原創性與授權檢查
```

每篇文章只寫自己的實驗、自己的失敗紀錄與自己的取捨；引用外部概念時以連結或參考資料清楚標示，不把參考內容改寫成自己的經歷。發表前逐篇檢查文字、程式、圖片、資料集與套件授權，並保留本地相似度檢查紀錄。

### 專案命名與程式入口

為避免與任何參考作品產生名稱聯想，本計畫的工作程式名稱採用從本專案名稱衍生的 `frontier_knowledge.py`，Python 套件採用 `frontier_knowledge/`。若日後改名，必須在 `design-decisions.md` 記錄命名理由，且不得採用參考作品的近似名稱。

## 12. Repository 結構

```text
ai-engineering-frontier/
├── README.md
├── pyproject.toml
├── uv.lock
├── .env.example
├── .gitignore
├── articles/
│   ├── day01.md
│   └── ...
├── src/
│   └── frontier_knowledge/
│       ├── llm_client.py
│       ├── document_manifest.py
│       ├── document_loader.py
│       ├── knowledge_builder.py
│       ├── retrieval.py
│       ├── context_budget.py
│       ├── evidence_pipeline.py
│       ├── readonly_actions.py
│       ├── task_flow.py
│       ├── evaluation.py
│       └── knowledge_checks.py
├── scripts/
│   ├── run_chat.py
│   ├── build_knowledge.py
│   ├── evaluate_system.py
│   └── inspect_environment.py
├── data/
│   └── benchmark.jsonl
├── knowledge/
│   ├── raw/
│   │   └── sample_docs/
│   └── wiki/
│       ├── sources/
│       ├── concepts/
│       ├── howto/
│       ├── derived/
│       ├── index.md
│       ├── overview.md
│       └── log.md
├── indexes/
│   ├── catalog.sqlite
│   └── retrieval.sqlite
├── configs/
│   ├── baseline.yaml
│   ├── rag.yaml
│   └── agent.yaml
├── runs/
│   └── .gitkeep
└── docs/
    ├── architecture.md
    ├── safety.md
    └── troubleshooting.md
```

`runs/` 可以只提交結果摘要，不必提交全部大型原始輸出。若要保留完整結果，使用小型 JSONL 並設定檔案大小上限。

`knowledge/raw/` 與 `knowledge/wiki/` 是可讀、可備份的內容層；`indexes/` 是 derived artifact，可以刪除後由 `ingest` 重新建立。

## 13. Day 30 的完成定義

以下項目全部完成，才算完成核心專案：

- 新讀者可以依 README 在本地啟動模型。
- 新讀者可以把自己的 Markdown 文件放入指定資料夾。
- 系統可以建立、更新，並從 raw/wiki 重新建立本地索引。
- raw、wiki 與 runtime index 的責任邊界在 README 中說明清楚。
- 問題回答會顯示來源文件與 chunk。
- 找不到資料時不會硬猜。
- Context builder 會在固定 token budget 內選擇證據。
- 完成 Direct RAG、Miracle RAG、Hierarchical RAG 的比較結果。
- 至少有一個唯讀工具。
- Agent 有步數上限、timeout 與錯誤處理。
- benchmark 可一個命令重新執行。
- 結果同時包含品質、效能與資源使用量。
- Repo 不含模型權重、秘密或未授權資料。

## 14. 延伸 Roadmap

核心 v1.0 完成後，再考慮：

1. Reranker：比較 retrieval precision 的改善。
2. MCP：比較工具重用性與整合成本。
3. 向量資料庫：比較索引規模與維運成本。
4. 外部長期記憶：加入使用者可管理的記憶生命週期。
5. DFlash2：單獨研究推論速度，不與品質提升混為一談。
6. Observability：加入 trace、token budget 與錯誤分類。
7. 更換模型：研究同一架構如何支援不同本地 LLM。

## 最終主張

這個系列不是要讓初學者在 30 天內學會所有 AI Engineering 名詞，而是讓他們完成一次可理解、可重現、可延伸的本地 AI 系統建置：

> **先讓模型在本地回答，再讓它讀自己的文件，接著讓它安全地做一件事，最後用數據知道它到底有沒有變好。**
