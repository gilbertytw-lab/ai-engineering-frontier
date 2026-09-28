# Day 14 驗證與編輯紀錄

查證日期：2026-09-28（Asia/Taipei）。本文件保留實作、單次 checkpoint 輸出與驗收界線。

## 實作與環境

`knowledge/rag.py` 從 manifest 重建 FTS5 索引，用 Day 13 的 context builder 選擇證據，再呼叫本地 chat-completions endpoint。回覆必須包含 `answer`、`citations`、`no_answer`，引用只能是本次實際選入的 chunk ID。來源檔名、raw 路徑與行號由 chunk metadata 查回。有答案時至少引用一個 chunk；拒答時引用陣列為空，但看過的證據仍保存於 context 紀錄。

沒有選入證據時直接拒答；有證據但缺少答案時由模型判斷。`finish_reason` 必須為 `stop`，其他結果保存為失敗；沒有自動重試或格式修補。JSONL 以 append 方式保存問題、messages、選入與淘汰證據、完整模型回覆、token 數、耗時與錯誤，位於已排除 Git 的 `runs/`。

`knowledge/ingest.py` 的 `Tokenizer` 補上可選的 `chat_template_kwargs`，既有呼叫保留原本設定。`knowledge/retrieve.py` 補上 SQLite connection 明確關閉，修正本次重複呼叫時發現的 `ResourceWarning`。

- Python 3.13.15、`mlx-lm 0.31.3`、`transformers 5.16.1`。
- 模型與 tokenizer：`mlx-community/Qwen3.8-27B-4bit`，使用現有本機快取。
- endpoint：`http://127.0.0.1:8081/v1/chat/completions`。
- 設定：`context_window=2048`、`output_reserve=512`、`limit=8`、`temperature=0`。
- token 計算與 request 都使用 `enable_thinking=false`。

2,048 是本次 request cap；512 是 JSON 回答上限，不代表模型最大 context 或實際生成量。以 system「你是工程知識助理。」、user「測試」的簡短 messages 做 template 比較，`tokenize=True`、`add_generation_prompt=True` 下的 `input_ids` 長度為：預設 59，`enable_thinking=False` 為 23。

## 可重建索引

在 Python 暫存目錄執行 `build_manifest()`，讀取本專案 raw，指定 `max_tokens=160`、`overlap_tokens=24`。新 manifest 與既有完整 JSON 一致：5 份文件、11 個 chunks。

從該 manifest 建立暫存 SQLite，查詢 `production`、`limit=8`；刪掉暫存 SQLite 並重建後，8 個候選的完整 dict、文字、來源位置與排序完全一致。正式 raw、manifest 與原件未被修改。RAG CLI 每次啟動會直接重建正式衍生索引，適用於目前的小型資料集。

## Dry run

```bash
HF_HUB_OFFLINE=1 uv run python knowledge/rag.py \
  --query production \
  --question 'production 的 HARBOR_WORKER_COUNT 是多少？production 錯誤率持續多久、高於多少時要停止放量並回滾？請分別引用設定文件與部署文件。' \
  --dry-run \
  --log runs/day14-dry-run.jsonl
```

輸出：

```text
重建 FTS5：5 份文件、11 個 chunks
Dry run：選入 5 個 chunks，input tokens=1062
執行紀錄：runs/day14-dry-run.jsonl
```

沒有發出模型 request。

## 真實 Qwen checkpoint

啟動 server：

```bash
HF_HUB_OFFLINE=1 uv run mlx_lm.server \
  --model mlx-community/Qwen3.8-27B-4bit \
  --port 8081
```

執行：

```bash
HF_HUB_OFFLINE=1 uv run python knowledge/rag.py \
  --checkpoint \
  --model mlx-community/Qwen3.8-27B-4bit \
  --log runs/day14-checkpoint.jsonl
```

實際輸出：

```text
重建 FTS5：5 份文件、11 個 chunks
Checkpoint cross_document：PASS
production 的 HARBOR_WORKER_COUNT 預設值為 8。當 production 錯誤率連續 5 分鐘高於 2% 時，需停止放量並回滾到上一個 stable release。
來源：service-config.md，raw 第 23–34 行（doc-3317e1a5be5eb33f-chunk-0002）
來源：deployment-guide.md，raw 第 25–33 行（doc-891dc9cf617077c2-chunk-0002）
status=ok，model_called=True，input tokens=1062，runtime prompt tokens=1062，model elapsed_ms=29083.1
Checkpoint missing_fact：PASS
不知道，提供的證據明確指出 release-policy.md 沒有定義 log retention，且未提供 harbor-api 相關的其他文件資訊。
status=no_answer，model_called=True，input tokens=303，runtime prompt tokens=303，model elapsed_ms=9620.9
Checkpoint no_hits：PASS
不知道。本次查詢沒有選入可用證據，無法根據文件回答。
status=no_answer，model_called=False，input tokens=171，runtime prompt tokens=n/a，model elapsed_ms=0.0
執行紀錄：runs/day14-checkpoint.jsonl
Day 14 checkpoint：PASS
```

| case_id | 候選／選入 | base input | final input | runtime output | 模型請求耗時 | 總耗時 |
|---|---|---:|---:|---:|---:|---:|
| `cross_document` | 8／5 | 200 | 1,062 | 128 | 29,083.1 ms | 29,098.2 ms |
| `missing_fact` | 1／1 | 173 | 303 | 51 | 9,620.9 ms | 9,623.0 ms |
| `no_hits` | 0／0 | 171 | 171 | 未呼叫 | 0.0 ms | 1.8 ms |

兩筆模型回應都是 `finish_reason=stop`，runtime prompt tokens 與本機計數相同。第一筆 `cached_tokens=0`，第二筆 `cached_tokens=139`；未重複量測，不作效能比較或平均延遲結論。tokenizer 初始化、啟動前索引重建與 server process 啟動不包含在 `run_query()` 的總耗時。

跨文件案例選入 5 個 chunks，3 個因同一文件行號重疊被拒絕；其中 `doc-3317e1a5be5eb33f-chunk-0003` 的原因是 `overlapping_lines_with:doc-3317e1a5be5eb33f-chunk-0002`。預算為 `1062+512=1574`，低於 2,048。

`missing_fact` 查詢 `log retention`，選入 `release-policy.md` raw 第 26–34 行，該處明確寫著沒有定義此政策；模型回覆 `no_answer=true`、`citations=[]`。`no_hits` 查詢 `orbital archive quota`，由程式直接拒答。

## 來源核對與驗收界線

- raw `doc-3317e1a5be5eb33f.md` 第 30 行是 `HARBOR_WORKER_COUNT=8`；raw `doc-891dc9cf617077c2.md` 第 29 行是連續 5 分鐘高於 2% 的門檻。後者另有 migration 處理條件，這題只問門檻，回答不當成完整回滾 SOP。
- 自動 checkpoint 核對必要字串 `8`、`5`、`2%`、兩個來源、`no_answer` 與 `model_called`。字串命中及 citation membership 不足以證明逐句語意正確，本次另行回看 raw。
- 三個固定案例不是整體 citation correctness／no-answer 準確率；零命中案例不計作模型拒答能力。
- 拒答題有明確的「未定義」文字；未測部分缺漏、版本衝突或完整提示注入攻擊集。
- FTS5 仍採 lexical AND 查詢，使用者要指定 `query`；未加入同義詞搜尋或自動 query 改寫。

## 自動化驗證

```bash
uv run python -m unittest tests.test_day14_rag -v
uv run python -m unittest discover -s tests -v
git diff --check
```

Day 14 的 11 個測試方法通過；全專案 49 個測試方法通過。stub completion 與 fake tokenizer 只用來驗證資料契約，不當成實際模型結果。

涵蓋 citation 格式與 allowlist、零命中不呼叫模型、送出完整 messages、來源位置由 index 查回、可解析 JSON 但 `finish_reason=length` 仍失敗、模型拒答、固定 prompt 與 runtime 回報的預算超限、dry run、HTTP payload／token counter 使用相同 template 選項，以及索引刪除後重建一致性。

## 標題與副標備選

1. 如何組出有來源的本地 RAG｜把 FTS5、context budget 與 Qwen 接成可重跑的問答流程（SEO）。
2. 回答了 8，來源也要查得到 8｜Day 14 用兩份工程文件驗收 Qwen 的跨文件回答（社群）。
3. Day 14：把文件接上 Qwen，做出有來源的 RAG｜從證據組裝走到引用檢查與兩種拒答（鐵人賽／電子報）。
4. 找到文件，為什麼還要回答不知道？｜本地知識助理如何分辨零命中與缺少答案（SEO／社群）。

## 風格配方紀錄

教學實作型｜Simon 實證筆記風味｜標準｜單稿。依使用者要求精簡正文，保留回顧接棒、操作命令、代表性回答與能力界線；第一人稱只描述本次實際核對與選擇。

`blog-writing-zh` 技術檢查：操作型主體交代環境、模型快取、兩個終端機、索引重建、dry run、預期輸出與 JSONL 副作用；概念層區分 citation membership 與語意支持、兩種拒答、output reserve 與實際生成量、本機計數與 runtime usage。

系列評估：維持單篇，單一主張是「把有預算的證據接成能回查來源與拒答的本地問答」。細節由深文篇幅與本驗證文件承接。

`speak-human-tw` detect-first 語感檢查：0 處需提出改寫。先鎖定模型原話、命令、來源 ID、行號、測試數量與實測數字，再逐類檢查套話、假經歷、過度修辭、台灣用語與標點。保留必要的限制說明、具體判斷與少量單句段落。

pipeline：`speak-human-tw(detect-first, voice=technical, context=technical-blog)` 通過。本環境未找到 `humanizer-zh`，依使用者本次指定以 `speak-human-tw` 執行語感檢查，沒有記錄成未執行的 rewrite。

自評：直接性 9／節奏 9／信任度 10／真實性 9／精煉度 8，共 45／50。這是編輯自評，沒有外部評分。

Markdown 區塊與相對連結檢查通過；正文保留的兩筆模型原話與原始紀錄逐字一致，完整三筆回答留在本紀錄。本機 input tokens 與兩筆 runtime 回報相同；`git diff --check` 通過。本次實測啟動的 server 已在測量後關閉。

## 正文精簡紀錄

2026-09-28 依使用者要求，將全文限制在 4,000 字內，移除正文中的測試命令、checkpoint 詳細步驟、耗時表格、快取數字、template 計數比較與索引重建比對過程。上述驗證資料保留於本文件，正文只連回本紀錄。

精簡後完整 Markdown 為 3,487 字元，計入英文、程式碼、URL、標記與換行。保留使用者調整後的文章標題、RAG 資料流、操作命令、跨文件回答、拒答示例與引用檢查的限制。語感檢查沒有額外需提出改寫的項目。
