# Local Engineering Knowledge Assistant

這是「AI Engineering 研究前線」30 天實作專案的工作 Repository。報名標題維持不變；本專案的實作目標是讓只使用過網頁對話式 AI 的讀者，逐步建立一套可以在自己電腦上執行的本地工程知識助理。

目前進度：**Day 2／第一次在本機呼叫模型**

## 專案目標

讀者最後可以：

- 在本地呼叫一個 LLM。
- 匯入自己的 Markdown 或文字文件。
- 由原始文件建立可重建的知識索引。
- 在有限 context 預算內挑選少量證據。
- 產生附來源的回答，找不到證據時明確拒答。
- 使用受限制的唯讀功能完成簡單知識任務。
- 透過固定 benchmark 觀察品質、token 與效能變化。

## 核心資料流

```text
knowledge/raw
    ↓
文件 metadata、hash、chunk
    ↓
可讀的知識頁（選用）
    ↓
FTS／embedding retrieval
    ↓
context budget 與證據組裝
    ↓
Local LLM
    ↓
附來源回答、拒答與執行紀錄
```

`raw` 是可追溯的原始資料；知識頁是人類可維護的整理層；索引與執行結果都是可以刪除後重建的衍生物。這個邊界是本專案依照「本地模型 context 珍貴」與「初學者可跟做」兩項需求做出的設計決定。

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

Day 2 已建立 Python 3.13 的隔離環境、安裝 `mlx-lm`，並用 `frontier_knowledge.py` 呼叫本地模型。完整操作與實際輸出請看 [Day 2 文章](articles/day02.md)。

在 Apple Silicon 上可依序執行：

```bash
uv venv --python 3.13
uv sync
```

終端機一：

```bash
uv run mlx_lm.server \
  --model mlx-community/Llama-3.2-3B-Instruct-4bit \
  --port 8080
```

終端機二：

```bash
uv run python frontier_knowledge.py \
  "請用一句話說明本地模型和網頁聊天 AI 的差別。"
```

## Day 1 之後

Day 3 會在這個最小呼叫上建立可重複使用的 Chat Runner。RAG、Agent 和 MCP 仍然不會在第一週一開始就加入。
