# Local Engineering Knowledge Assistant

這是「AI Engineering 研究前線」30 天實作專案的工作 Repository。報名標題維持不變；本專案的實作目標是讓只使用過網頁對話式 AI 的讀者，逐步建立一套可以在自己電腦上執行的本地工程知識助理。

目前進度：**Day 24／完成 Kubernetes 索引規模與查詢效能量測**

## 專案目標

讀者最後可以：

- 在本地呼叫一個 LLM。
- 將自己的 Markdown、文字檔、有文字層的 PDF 或靜態網頁轉成帶來源欄位的 Markdown。
- 由原始文件建立可重建的知識索引。
- 在有限 context 預算內挑選少量證據。
- 產生附來源的回答，找不到證據時明確拒答。
- 使用受限制的工具查詢知識，並在明確選擇後匯入新來源。
- 透過固定 benchmark 觀察品質、token 與效能變化。

## 核心資料流

```text
原始檔案或網頁快照：knowledge/inbox
    ↓
source-to-raw-md：程式抽出完整文字、保留 PDF 頁碼並補上來源欄位
    ↓
固定格式的 Markdown：knowledge/raw
    ↓
後續 ingest：文件版本與 chunk manifest
    ↓
可讀的知識頁（由 raw 自動建立 source catalog）
    ↓
FTS／embedding retrieval
    ↓
context budget 與證據組裝
    ↓
Local LLM
    ↓
附來源回答、拒答與執行紀錄
```

`inbox` 保存原始檔案或網頁快照；`raw` 保存轉換後、帶來源欄位的 Markdown。Day 11 的 `knowledge/wiki.py` 會從 raw 自動建立可回查的 source catalog；使用者不需要手動替來源文件建立頁面或分類。chunk manifest、索引與執行結果由後續步驟建立。Chat Runner 尚未檢索或讀取這些文件。

## 明確不做的事

本系列不以訓練模型、建立多 Agent 系統、開放 shell、讓模型任意修改檔案或部署多人服務為完賽條件。這些內容即使有價值，也不應阻塞 30 天的核心成果。

## 30 天執行方式

每天包含：

1. 一篇以當日實驗為主的文章。
2. 一個可執行或可驗證的變更。
3. 一筆清楚的 Git commit。
4. 一項成功或失敗的紀錄。

目前的完整計劃請看 [ai-engineering-frontier-plan-v2.md](ai-engineering-frontier-plan-v2.md)；原始草案 [ai-engineering-frontier-plan.md](ai-engineering-frontier-plan.md) 保留作為規劃歷史。

## 原創性界線

本 Repository 的名稱、目錄、模組切分、範例資料、文章、程式碼與 commit 敘事均獨立設計與撰寫。外部資料只作為需要標示來源的技術參考，不作為本專案的模板。

相關紀錄：

- [Day 1 範圍與環境](docs/day01-scope-and-environment.md)
- [設計決策](docs/design-decisions.md)
- [來源紀錄](docs/sources.md)
- [原創性檢查](docs/originality-check.md)
- [文章寫作規範](docs/article-style.md)

## Day 2

Day 2 已建立 Python 3.13 的隔離環境，並用 `frontier_knowledge.py` 呼叫本地模型。完整操作與實際輸出請看 [Day 2 文章](articles/day02.md)。

在 macOS Apple Silicon 上：

```bash
uv python install 3.13
uv python pin 3.13
uv venv --python 3.13
uv sync
```

終端機一（macOS）：

```bash
uv run mlx_lm.server \
  --model mlx-community/Llama-3.2-3B-Instruct-4bit \
  --port 8081
```

終端機二：

```bash
uv run python frontier_knowledge.py \
  "請用一句話說明本地模型和網頁聊天 AI 的差別。"
```

## Day 3

Day 3 在既有的單次呼叫上加入互動式 Chat Runner。省略 prompt 或加上 `--interactive` 後，程式會持續等待問題；輸入 `exit`、`quit` 或 `:q` 可以結束。完整操作與限制請看 [Day 3 文章](articles/day03.md)。

```bash
uv run python frontier_knowledge.py --interactive
```

單次 prompt 的 Day 2 命令仍然可以使用。Day 3 每次請求只送出目前輸入，尚未保存對話歷史。

## Day 4

Day 4 在每次請求的 `messages` 前面加入預設的 `system` message，讓模型收到固定的回答規則。需要比較加入規則前後的差異時，可以使用 `--no-system-prompt`。

```bash
uv run python frontier_knowledge.py \
  "請說明今天的測試重點。"

uv run python frontier_knowledge.py \
  --no-system-prompt \
  "請說明今天的測試重點。"
```

完整操作與限制請看 [Day 4 文章](articles/day04.md)。

## Day 5

加入 `--json-answer` 後，模型會收到 JSON 格式要求，程式會檢查 `answer` 與 `limitations` 兩個欄位。格式不合時回報錯誤；省略選項則保留文字模式。

```bash
uv run python frontier_knowledge.py \
  --model mlx-community/Qwen3.8-27B-4bit \
  --max-tokens 1024 --json-answer \
  "請用一句話說明本地模型。"

uv run python -m unittest discover -s tests -v
```

完整教學見 [Day 5 文章](articles/day05.md)，驗證範圍見 [Day 5 驗證紀錄](docs/day05-verification.md)。格式通過不代表內容正確。

## Day 6

互動模式現在會把同一次執行中已成功完成的 `user`／`assistant` 回合附到下一次 request，讓模型能回答依賴前文的追問。這份 Session history 只放在記憶體中；離開程式後就會清空。

```bash
uv run python frontier_knowledge.py \
  --model mlx-community/Qwen3.8-27B-4bit \
  --max-tokens 1024 \
  --interactive
```

需要和 Day 5 的獨立請求行為比較時，加上 `--no-history`：

```bash
uv run python frontier_knowledge.py \
  --model mlx-community/Qwen3.8-27B-4bit \
  --max-tokens 1024 \
  --interactive --no-history
```

完整教學見 [Day 6 文章](articles/day06.md)，驗證範圍見 [Day 6 驗證紀錄](docs/day06-verification.md)。

## Day 7

第一週 checkpoint 會對真實的本地 runtime 發出兩個 request。第一輪驗證固定 JSON 回答，第二輪從 Session history 找回第一輪的代號；兩輪都通過才輸出 `PASS`。

```bash
uv run python frontier_knowledge.py \
  --checkpoint \
  --model mlx-community/Qwen3.8-27B-4bit \
  --max-tokens 1024
```

本次實測輸出：

```text
Checkpoint 1/2：單次 JSON 回答通過（answer=收到）
Checkpoint 2/2：Session history 回答通過（answer=港口 17）
Day 7 checkpoint：PASS
```

完整教學見 [Day 7 文章](articles/day07.md)，驗證範圍見 [Day 7 驗證紀錄](docs/day07-verification.md)。

## Day 8

第二週先建立來源轉換工作流。讀者把檔案放進 `knowledge/inbox/`，在終端機執行 `knowledge/convert.py`；程式逐份轉換、驗證，成功後把原檔移到 `knowledge/inbox/processed/`，將帶來源欄位的 Markdown 寫入 `knowledge/raw/`。五份虛構的 `harbor-api` 文件已按此流程處理。這一步不需要 Qwen 呼叫 skill；chunk manifest 與搜尋留待後續實作。PDF 的圖表、公式與雙欄順序仍要對照原檔。

```bash
uv run --with pypdf --with fonttools python knowledge/convert.py
```

完整教學見 [Day 8 文章](articles/day08.md)，驗證範圍見 [Day 8 驗證紀錄](docs/day08-verification.md)；轉換工具已另行發布於 [source-to-raw-md](https://github.com/gilbertytw-lab/source-to-raw-md)。

## Day 9

Day 9 將 `knowledge/raw/` 的 Markdown 以 Qwen tokenizer 分成帶來源位置的 chunks，建立可重建的 `knowledge/index/manifest.json`。目前設定每個 chunk 最多 160 tokens、重疊 24 tokens；本次五份示範文件產生 11 個 chunks。manifest 只保存衍生索引，raw 與 `inbox/processed/` 仍是可回查的來源。

```bash
HF_HUB_OFFLINE=1 uv run python knowledge/ingest.py \
  --max-tokens 160 --overlap-tokens 24

HF_HUB_OFFLINE=1 uv run python knowledge/measure.py \
  --dry-run --evidence-tokens 160 320 640
```

要做真實延遲量測，先啟動 Day 2 的本地 runtime，再執行同一個 `knowledge/measure.py`，命令會記錄 Qwen 的 input tokens、證據 tokens、回答 token 估計值與耗時。固定 benchmark 只代表這台機器與這次模型快取的結果，不把單次數字當成通用效能保證。完整教學見 [Day 9 文章](articles/day09.md)，驗證範圍見 [Day 9 驗證紀錄](docs/day09-verification.md)。

## Day 10

Day 10 在 Day 9 的 chunk manifest 上加入第一條關鍵字檢索路徑。`knowledge/retrieve.py` 使用 Python 內建的 SQLite FTS5 建立可重建的 `knowledge/index/retrieval.sqlite`，以 BM25 排序候選 chunks，並保留來源檔名與 raw 行號。索引是衍生物，刪掉後可從 manifest 重建；今天沒有啟動 Qwen。

```bash
HF_HUB_OFFLINE=1 uv run python knowledge/ingest.py \
  --max-tokens 160 --overlap-tokens 24

uv run python knowledge/retrieve.py \
  --query "release owner" --limit 5
```

完整教學見 [Day 10 文章](articles/day10.md)，驗證範圍見 [Day 10 驗證紀錄](docs/day10-verification.md)。

## Day 11

Day 11 新增 `knowledge/wiki.py`，從 `knowledge/raw/*.md` 自動建立 `knowledge/wiki/index.md` 和 5 個 source pages。每頁保留 `document_id`、來源檔名、raw 路徑、source snapshot、hash 與 converter 資訊，並連回原始 raw 文件。這一版不呼叫 Qwen、不複製 raw 正文，也不要求使用者手動分類文件。

```bash
uv run python knowledge/wiki.py

uv run python -m unittest tests.test_day11_wiki -v
```

完整教學見 [Day 11 文章](articles/day11.md)，驗證範圍見 [Day 11 驗證紀錄](docs/day11-verification.md)。

## Day 12

Day 12 比較 raw、wiki 和 hierarchical 三條證據路徑，確認 source catalog 適合導覽，最終回答仍需要回到 raw chunks。完整教學見 [Day 12 文章](articles/day12.md)。

## Day 13

Day 13 新增 `knowledge/context.py`，把 FTS5 候選依 BM25 排序，在固定的 context window 和 output reserve 內組裝 messages。同一份文件重疊行號的 chunks 只保留較前者，被淘汰的候選會保存原因；本日不呼叫 Qwen。

```bash
HF_HUB_OFFLINE=1 uv run python knowledge/context.py \
  --query 'production release' \
  --limit 5 \
  --context-window 1024 \
  --output-reserve 128

uv run python -m unittest tests.test_day13_context -v
```

完整教學見 [Day 13 文章](articles/day13.md)，驗證範圍見 [Day 13 驗證紀錄](docs/day13-verification.md)。

## Day 14

Day 14 新增 `knowledge/rag.py`，從 manifest 重建 FTS5 索引，將 Day 13 的 bounded messages 交給本地 Qwen，檢查 `answer`、`citations` 和 `no_answer`。引用必須來自本次實際選入的 chunks，來源檔名與 raw 行號由程式查回；零命中直接拒答，有證據卻缺少答案時由模型回覆 `no_answer`。每次執行會在 `runs/` 附加 JSONL 紀錄。

先啟動本地 runtime，再執行：

```bash
HF_HUB_OFFLINE=1 uv run python knowledge/rag.py \
  --checkpoint \
  --model mlx-community/Qwen3.8-27B-4bit \
  --log runs/day14-checkpoint.jsonl

uv run python -m unittest tests.test_day14_rag -v
```

本次三個固定案例通過，全專案 49 個測試通過；兩筆模型 request 的 input tokens 為 1,062 與 303。這份 checkpoint 只驗收少量固定案例，citation membership 檢查尚未保證逐句語意正確。完整教學見 [Day 14 文章](articles/day14.md)，實測數字與限制見 [Day 14 驗證紀錄](docs/day14-verification.md)。

## Day 15

`knowledge/tools.py` 把 `list_sources` schema 傳給本地 Qwen。模型需要列來源時會提出工具呼叫；Python 只接受允許清單內的唯讀函式，驗證 `name_contains` 後讀固定 manifest，再把來源名稱與 document ID 交回模型。每回合最多執行一個工具和發出兩次模型 request。

先啟動 Day 14 使用的本地 runtime，再執行：

```bash
HF_HUB_OFFLINE=1 uv run python knowledge/tools.py --checkpoint
uv run python -m unittest tests.test_day15_tools -v
```

真實 Qwen 的「需要查工具」與「不需工具」兩個案例通過；Day 15 的 11 個單元測試及全專案 60 個測試通過。完整操作、輸出與限制見 [Day 15 文章](articles/day15.md)和[驗證紀錄](docs/day15-verification.md)。

## Day 16

`knowledge/tools.py` 新增 `get_document_chunks`。Python 只依 `document_id` 從固定的 `knowledge/index/manifest.json` 取回內容，不接受路徑；每次最多回傳 3 個 chunks，並附上來源名稱、chunk ID 與 raw 行號。文件超過上限時，結果會標記 `truncated`。

先啟動本地 runtime，再執行：

```bash
HF_HUB_OFFLINE=1 uv run python knowledge/tools.py --checkpoint
uv run python -m unittest tests.test_day16_tools -v
```

本地 Qwen 的來源清單、文件片段查詢與不需工具三個案例都通過；Day 16 的 7 個單元測試及全專案 67 個測試通過。單回合仍最多執行一個工具，因此列來源與讀取內容要分成兩次操作。完整內容與限制見 [Day 16 文章](articles/day16.md)和[驗證紀錄](docs/day16-verification.md)。

## Day 17

Day 17 新增 `web_search` 與 `import_web_source`。本地資料不足時，模型可以用 `web_search` 搜尋最多 5 筆候選來源；搜尋只回傳標題、網址和摘要，不會下載或匯入。使用者在下一輪明確選定來源 ID（例如 `web-2`）後，模型才會呼叫 `import_web_source`：程式保存網頁快照到 `knowledge/inbox/`，呼叫既有轉換器寫入 `knowledge/raw/`，再重建 chunk manifest 和 FTS5 索引。

匯入工具只接受最近一次搜尋的來源 ID，不接受任意 URL 或路徑。程式會拒絕未明確選取的匯入呼叫、限制回傳筆數和下載大小，並拒絕解析到本機或內部 IP 的網址。來源頁面可能包含提示注入文字，模型只把它當資料處理。搜尋服務若要求人工驗證，工具會回報沒有取得結果，不會猜測來源。

啟動本地 runtime 後執行工具 checkpoint：

```bash
HF_HUB_OFFLINE=1 uv run python knowledge/tools.py --checkpoint
uv run python -m unittest tests.test_day17_tools -v
```

完整流程見 [Day 17 文章](articles/day17.md)，測試範圍與服務限制見 [Day 17 驗證紀錄](docs/day17-verification.md)。

## Day 18

Day 18 用 10 題固定案例量測 Qwen 的首次工具選擇。評估器只讀取模型選擇的工具名稱或直接回答，不執行搜尋、文件讀取或匯入。這次 10 題全數符合預期；結果只代表這組人工案例，不是一般化準確率。

```bash
HF_HUB_OFFLINE=1 uv run python knowledge/evaluate_routing.py
```

案例、完整文章與評估限制見 [Day 18 文章](articles/day18.md)及[驗證紀錄](docs/day18-verification.md)。

## Day 19

Day 19 在工具 dispatcher 加上嚴格的 `arguments` 驗證：要求 JSON object、拒絕重複欄位和額外參數，並檢查型別、空值與長度。網頁來源匯入還要通過目前回合的使用者選取檢查。相關拒絕路徑可用下列單元測試重跑：

```bash
uv run python -m unittest tests.test_day15_tools tests.test_day16_tools tests.test_day17_tools -v
```

完整說明見 [Day 19 文章](articles/day19.md)。

## Day 20

Day 20 比較應用程式直接呼叫 Python 工具函式，與透過 MCP client/server 探索和執行工具的差異。目前專案只有一個本地 AI 助理；MCP adapter 仍是選配，文章依現有程式與官方文件整理架構比較，沒有新增 MCP client 或 server。

完整說明與官方來源見 [Day 20 文章](articles/day20.md)。

## Day 21～22

Day 21 整理第三週工具 checkpoint，Day 22 固定 Kubernetes 官方英文 Markdown 的來源 commit，盤點 1,720 份文件並整理十題起始題集。完整內容見 [Day 21](articles/day21.md)、[Day 22](articles/day22.md)和[語料紀錄](docs/day22-verification.md)。

## Day 23

`knowledge/import_corpus.py` 以固定 checksum 核對 Markdown 語料，保留相對來源路徑與固定版本網址，再用既有 converter 匯入指定工作區，保存逐檔成功、沿用與失敗紀錄。Kubernetes 語料首輪有 1 份 CRLF 文件驗證失敗；修正讀取 raw 時的換行轉換後，1,720 份全部通過，再次執行全數沿用並驗證。

固定版本的 1,720 份來源 Markdown、轉換後 raw 與逐檔報告都收在專案的 [Day 23 語料資料夾](data/day23/README.md)，可隨 GitHub Repository 下載。完整量測摘要見 [結果摘要](data/day23-import-summary.json)；匯入命令、數據與限制見 [Day 23 文章](articles/day23.md)和[驗證紀錄](docs/day23-verification.md)。

## Day 24

`knowledge/benchmark_scale.py` 將同一批 raw 依檔名排序，取 100、500、1,720 份文件，分別在新子程序中量測 chunk manifest、FTS5 建置、檔案大小、程序峰值 RSS 與固定查詢延遲。全量產生 36,807 個 chunks；本次切塊與 manifest 花 18.685 秒，FTS5 建置花 0.575 秒，240 筆暖身後查詢的 p50／p95 為 0.357／5.861 毫秒。這些是固定詞組與單機量測，品質評分另行處理。

```bash
HF_HUB_OFFLINE=1 uv run python knowledge/benchmark_scale.py \
  --workspace-root data/day24/reproduction \
  --sizes 100 500 1720 --rounds 20 --limit 5
```

工作區已存在時，改用 `data/day24/reproduction-2` 等新名稱。完整文章見 [Day 24](articles/day24.md)，量測邊界與檢查結果見 [驗證紀錄](docs/day24-verification.md)；固定查詢詞、逐筆耗時與索引 audit 分別保存在 [queries](data/day24-queries.json)、[summary](data/day24-scale-summary.json)和[audit](data/day24-index-audit.json)。
