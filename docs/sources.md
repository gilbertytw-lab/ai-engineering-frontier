# 來源紀錄

這份文件只登錄實際使用或引用的外部資料。每筆來源都要說明用途；只讀過但沒有影響實作的資料，不直接改寫成文章內容。

## 登錄格式

```text
### SXXX：來源名稱
- URL：
- 存取日期：
- 用途：
- 使用範圍：
- 是否包含程式碼、文字或圖片：否／是（說明授權）
```

## Day 1

### S001：speak-human-tw

- URL：https://github.com/Raymondhou0917/speak-human-tw
- 使用的公開文件：README、`SKILL.md`、`references/patterns.md`、`references/humanize.md`、`references/taiwan-localization.md`
- 存取日期：2026-08-27
- 用途：整理本專案的繁體中文文章自查方向，降低公式化、空泛和翻譯腔。
- 使用範圍：只參考「先保事實、再處理語氣」的工作原則與台灣用語檢查方向；Day 1 文章由本專案重新撰寫。
- 是否包含程式碼、文字或圖片：否

Day 1 沒有把外部文章、程式碼、圖片或範例資料放入 Repository。後續若使用模型官方文件、套件文件或研究論文，會在實際使用前補登錄 URL、日期與用途。

### S002：Python 官方版本與支援狀態

- URL：https://devguide.python.org/versions/
- 存取日期：2026-08-27
- 用途：確認 Python 3.9 已結束支援，以及 3.12、3.13、3.14 的維護狀態。
- 使用範圍：只作為本專案版本策略的依據，不複製頁面內容。
- 是否包含程式碼、文字或圖片：否

### S003：MLX-LM 套件資訊

- URL：https://pypi.org/project/mlx-lm/
- 存取日期：2026-08-27
- 用途：確認 Apple Silicon 本地模型 runtime 的 Python 需求與安裝前提。
- 使用範圍：只作為 Day 2 runtime smoke test 的參考，不預先假設所有依賴都相容。
- 是否包含程式碼、文字或圖片：否

### S004：MLX-LM server 文件

- URL：https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/SERVER.md
- 存取日期：2026-08-27
- 用途：確認本地 HTTP server 的啟動方式、模型參數與 OpenAI-compatible endpoint。
- 使用範圍：依文件重新組合 Day 2 的啟動命令與呼叫流程；沒有複製文章或專案結構。
- 是否包含程式碼、文字或圖片：否

### S005：uv 安裝文件

- URL：https://docs.astral.sh/uv/getting-started/installation/
- 存取日期：2026-08-27
- 用途：確認 uv 的安裝方式與 Python 環境管理命令。
- 使用範圍：只作為本機工具安裝與環境建立的參考；文章命令依本專案目錄與版本重新整理。
- 是否包含程式碼、文字或圖片：否

### S006：Qwen3.8-27B 官方模型卡

- URL：https://huggingface.co/Qwen/Qwen3.8-27B
- 存取日期：2026-09-15
- 用途：確認 Qwen3.8-27B 的 target model 名稱、參數規模與原生 context 長度。
- 使用範圍：Day 1 用來說明模型規格與本機 runtime context 限制的差異；沒有複製模型卡內容。
- 是否包含程式碼、文字或圖片：否

### S007：Qwen3.8 官方 GitHub

- URL：https://github.com/QwenLM/Qwen3.8
- 存取日期：2026-09-15
- 用途：確認官方部署文件提供的 context 設定範例。
- 使用範圍：只作為模型 context 設定的補充參考；文章依本專案的 32 GB Mac 環境重新整理。
- 是否包含程式碼、文字或圖片：否

## Day 4

### S008：MLX-LM server 文件
- URL：https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/SERVER.md
- 存取日期：2026-09-17
- 用途：確認 Day 4 延續使用的本地 chat-completions server 入口。
- 使用範圍：核對 `messages` payload 與本地 server 的呼叫邊界；Day 4 的 system message 內容由本專案自行設計。
- 是否包含程式碼、文字或圖片：否

### S009：MLX-LM server 實作
- URL：https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/server.py
- 存取日期：2026-09-17
- 用途：確認 `system`、`user` message 會交給模型 tokenizer 的 chat template 處理。
- 使用範圍：只用來核對本機已安裝 `mlx-lm 0.31.3` 的實作行為，不複製程式碼。
- 是否包含程式碼、文字或圖片：否

## Day 5

### S010：Python 3.13 json 官方文件
- URL：https://docs.python.org/3.13/library/json.html
- 存取日期：2026-09-19
- 用途：核對 `json.loads()`、JSON 與 Python 型別對應、`object_pairs_hook`、`parse_constant`，以及重複欄位與 NaN 的預設行為。
- 使用範圍：Day 5 的兩層解析解說與本專案自訂回答驗證器；程式與例子自行撰寫。
- 是否包含程式碼、文字或圖片：否

### S011：MLX-LM server 官方文件
- URL：https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/SERVER.md
- 存取日期：2026-09-19
- 用途：確認 chat endpoint、messages 與啟動參數；避免從 API 外形推定格式保證。
- 使用範圍：Day 5 沿用 server 入口；線上 main 文件與本機 0.31.3 分開標示，功能結論以本機測試為準。
- 是否包含程式碼、文字或圖片：否

## Day 8 來源轉換

### S012：pypdf 文字抽取文件
- URL：https://pypdf.readthedocs.io/en/6.18.1/user/extract-text.html
- 存取日期：2026-09-22
- 用途：確認 `PdfReader` 與 page-level `extract_text()` 的使用方式，以及掃描型 PDF 可能沒有可抽取文字的限制。
- 使用範圍：`source-to-raw-md` 使用 `pypdf` 抽取有文字層的 PDF；本專案自行撰寫程式，沒有複製文件內容或程式碼。
- 是否包含程式碼、文字或圖片：否

### S013：LibreOffice 文件轉換 filters
- URL：https://help.libreoffice.org/latest/ast/text/shared/guide/convertfilters.html
- 存取日期：2026-09-22
- 用途：確認舊版 DOC 可透過 LibreOffice 的 command-line conversion workflow 轉成可再抽取的文件格式。
- 使用範圍：曾用於文件轉換草稿的 `.doc` 路徑；草稿已保存於專案工作備份，未納入 Day 8 交付。沒有納入 LibreOffice 程式碼或文件內容。
- 是否包含程式碼、文字或圖片：否

### S014：Example Domain
- URL：https://example.com
- 存取日期：2026-09-22
- 用途：以公開靜態網頁測試網址下載、HTML 文字與連結抽取，再由程式轉成 Markdown。
- 使用範圍：Day 8 的網頁路徑 smoke test；網頁快照與轉換結果保存在本機驗證工作區，沒有併入 `harbor-api` 示範資料。
- 是否包含程式碼、文字或圖片：只用於測試；沒有複製原文至 Repository 文章。

## Day 10 SQLite lexical retrieval

### S015：SQLite FTS5 Extension
- URL：https://sqlite.org/fts5.html
- 存取日期：2026-09-24
- 用途：核對 FTS5 virtual table、MATCH 查詢與 `bm25()` ranking function 的介面與排序行為。
- 使用範圍：`knowledge/retrieve.py` 以 Python `sqlite3` 重新組合本專案的 chunk index、查詢和來源欄位；沒有複製文件程式碼或文章內容。
- 是否包含程式碼、文字或圖片：否

## Day 14 本地 RAG

### S016：Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

- URL：https://arxiv.org/abs/2005.11401
- 存取日期：2026-09-28
- 用途：核對 RAG 結合外部檢索與語言生成的研究出處。
- 使用範圍：文章以自己的文字簡短說明概念；本專案採 FTS5 與本地 Qwen 的問答流程，沒有複製論文的 dense retriever、模型訓練、程式碼或數據。
- 是否包含程式碼、文字或圖片：否；只有連結與概念改述。

### S017：MLX-LM server 官方文件

- URL：https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/SERVER.md
- 存取日期：2026-09-28
- 用途：核對 `/v1/chat/completions`、messages、max_tokens、`finish_reason=stop|length` 與 usage 欄位。
- 使用範圍：只用官方文件核對介面；本地測試使用 0.31.3，數字與模型行為由實測確認，不將線上 main 的全部功能推定為本機版本支援。
- 是否包含程式碼、文字或圖片：否；請求程式與文章獨立撰寫。
