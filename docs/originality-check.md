# 原創性與參賽合規檢查

本清單是每篇文章、每個 release 前的必要檢查，不是用來取代賽事正式規範。若正式規範要求更嚴格，以正式規範為準。

## Day 1 已完成

- [x] 專案名稱與程式入口由本專案需求獨立命名。
- [x] 架構由目標讀者、context 限制、可追溯性與安全邊界推導。
- [x] 範例資料規劃為自行撰寫的虛構工程文件。
- [x] Repository 不包含外部專案的程式碼、圖片或文章段落。
- [x] 建立設計決策與外部來源紀錄。

## Day 2 已完成

- [x] `frontier_knowledge.py`、檔名與命令由本專案依「最小本地模型呼叫」重新設計。
- [x] Day 2 文章只記錄本次實際執行的環境、命令、模型與輸出。
- [x] 使用的 runtime 文件與套件文件已加入 `docs/sources.md`。
- [x] 沒有納入外部專案的程式碼、圖片、文章段落或目錄結構。

## Day 3 已完成

- [x] 互動式 runner、退出命令與錯誤後繼續流程由本專案自行設計。
- [x] `articles/day03.md` 記錄實際完成的靜態檢查、stub smoke test、Metal device 限制與後續真實模型驗證。
- [x] 沒有複製外部 CLI、Prompt、文章段落或程式碼。

## Day 4 已完成

- [x] `system` message、預設內容與 `--no-system-prompt` 比較入口由本專案依目前 runner 需求設計。
- [x] `articles/day04.md` 只記錄本次 request-payload smoke test 與目前無 Metal device 的限制。
- [x] 沒有複製外部 Prompt、文章段落或程式碼；MLX-LM 文件只用來核對 chat-completions 與 message role 的介面。

## Day 8 已完成

- [x] 五份 `harbor-api` 工程文件、服務名稱、門檻、設定值與流程均由本專案自行設計。
- [x] `knowledge/inbox/processed/` 保存五份原始示範文件；`knowledge/raw/` 保存程式完整轉換並加上來源欄位的 Markdown。文件沒有放入真實公司資料、秘密、個人資料或第三方文章。
- [x] `incident-runbook.md` 的 untrusted text 是本專案自行加入的安全測試 fixture，並明確標示為文件資料，不是操作指令。
- [x] Day 8 的 `source-to-raw-md` skill、格式檢查與測試由本專案自行撰寫；Qwen 轉換舊版與舊 raw 保存在本機遷移備份，沒有當成現行交付。

## Day 9 已完成

- [x] `knowledge/ingest.py`、`knowledge/measure.py`、chunk manifest 格式、token budget 與 benchmark 問題由本專案依 Day 8 的五份虛構 `harbor-api` 文件自行設計。
- [x] 文章中的 5 份文件、11 個 chunks、324／542／831 input tokens 與 23.7／27.3／29.3 秒延遲來自本機實際命令；延遲只標為單次環境結果，不宣稱模型普遍效能。
- [x] 沒有把第三方文件正文、模型輸出全文或外部程式碼放入 Repository；manifest 可由 raw 重建，Qwen tokenizer 只作為本機依賴使用。

## Day 10 已完成

- [x] `knowledge/retrieve.py`、SQLite FTS5 schema、CJK 搜尋欄位、BM25 顯示與 5 項測試由本專案依 Day 9 manifest 自行設計。
- [x] 文章中的 5 份文件、11 個 chunks、`release owner` 的單筆命中與中文 `部署` 的 3 筆命中來自本機命令；BM25 只描述文字匹配，不宣稱回答品質。
- [x] SQLite 索引是可重建衍生物；原始文件、manifest 與 chunk 文字保留在本專案，沒有納入第三方文件正文或外部程式碼。

## 每日發文前

- [ ] 文章內容來自當天自己的實作、測試與失敗紀錄。
- [ ] 外部概念、數據、圖片與程式碼都有清楚來源及授權說明。
- [ ] 沒有沿用外部作品的專案名、檔名、類別名、命令名或專有敘事。
- [ ] 沒有複製外部作品的目錄配置、文章順序、Prompt、commit 訊息、圖表或示範案例。
- [ ] 文章中的程式碼已逐段確認為自己撰寫或有合法授權。
- [ ] 文章與程式已執行本地文字／程式相似度檢查，並保存檢查日期與結果。
- [ ] 使用的資料集沒有個資、秘密或未授權全文。

## Release 前

- [ ] 檢查完整 Git 歷史是否能反映逐日獨立產出。
- [ ] 檢查 README、文章、程式註解與圖片是否互相一致。
- [ ] 檢查所有第三方依賴的 license 與再散布條件。
- [ ] 對照賽事當年度正式規範完成最後人工審閱。
