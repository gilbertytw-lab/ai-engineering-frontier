# 設計決策紀錄

這份文件記錄本專案自己的設計來源與取捨。每次改變核心資料流、目標讀者或安全邊界時，新增一筆決策，不覆寫歷史。

## D001：先做可跟做的最小本地系統

- 狀態：accepted
- 日期：2026-08-27
- 決策：30 天以讀者能在自己的電腦跑起來、看見結果、逐日提交為成功條件。
- 理由：目標讀者只有網頁對話式 AI 經驗；過早引入過多框架會讓學習成果變成安裝清單。

## D002：原始文件是可追溯來源

- 狀態：superseded by D014；目前以 D016 為準
- 日期：2026-08-27
- 決策：`knowledge/raw/` 保存原始證據；整理頁與索引不得取代原始文件。
- 理由：回答需要能回到來源，索引也必須能刪除後重建。

## D003：整理頁與機器索引分離

- 狀態：accepted
- 日期：2026-08-27
- 決策：人類可讀的知識頁負責導覽與壓縮，FTS／embedding index 負責查詢；兩者不混為同一個資料層。
- 理由：避免把導航內容和大量證據一起塞入本地模型 context。

## D004：context budget 是一級限制

- 狀態：accepted
- 日期：2026-08-27
- 決策：每次回答先扣除 system prompt、對話歷史、工具描述與輸出預留，再決定可放入多少證據。
- 理由：本地模型的 context 有限，增加文件數量不代表可以無限制增加輸入。

## D005：先做唯讀任務

- 狀態：accepted
- 日期：2026-08-27
- 決策：第一版只提供文件查詢、設定檢查等可驗證的唯讀能力；不開放 shell，也不讓模型任意寫檔。
- 理由：讓初學者先理解工具邊界、驗證與失敗處理，不把安全風險當成附帶細節。

## D006：所有外部參考都要留下來源

- 狀態：accepted
- 日期：2026-08-27
- 決策：外部文件、套件、模型卡與概念在 `sources.md` 登錄；程式碼、文章與示範資料由本專案重新設計與撰寫。
- 理由：維持可查證性，也避免把參考作品的內容或結構誤當成自己的成果。

## D007：專案不使用系統 Python 3.9

- 狀態：accepted
- 日期：2026-08-27
- 決策：教學與測試以 Python 3.13.x 為主，3.12 作為保守相容版本，3.14 在依賴完成 smoke test 後再測試。
- 理由：目前電腦上的 Python 3.9.6 已結束官方支援；隔離且較新的基線能降低新套件安裝與後續維護的風險。

## D008：第一週先固定一個本地 HTTP runtime

- 狀態：accepted
- 日期：2026-08-27
- 決策：Day 2 先使用 `mlx-lm` 的 server，透過本地 OpenAI-compatible HTTP endpoint 呼叫模型；暫不同時加入其他 runtime。
- 理由：目標讀者需要先看懂「呼叫端、runtime、模型」的邊界。固定一條可執行路徑，比一次比較多套框架更容易排錯，也方便 Day 3 往可重複使用的 Chat Runner 演進。

## D009：互動模式與單次模式共用同一個呼叫函式

- 狀態：accepted
- 日期：2026-08-28
- 決策：`frontier_knowledge.py` 同時支援單次 prompt 與互動模式；兩種入口都使用 `call_local_model()` 呼叫本地 runtime。
- 理由：連續提問需要一個可重複使用的 CLI，但固定問題的腳本和排錯命令仍需要單次入口。共用請求函式可以讓兩種模式維持相同的 endpoint、錯誤處理與模型參數。

## D010：Day 3 不保存對話歷史

- 狀態：accepted
- 日期：2026-08-28
- 決策：互動模式每次只送出目前輸入，不把先前問題或回答自動附加到下一次請求。
- 理由：先驗證互動迴圈、退出命令和錯誤後繼續的行為；對話歷史會改變每次請求的輸入大小與回答條件，應在獨立的一天處理。

## D011：Day 4 以 system message 放置固定回答規則

- 狀態：accepted
- 日期：2026-09-17
- 決策：在每次請求的 `messages` 前面加入一則預設的 `system` message；保留 `--no-system-prompt` 供基線比較，也允許用 `--system-prompt` 暫時替換規則。
- 理由：Day 3 已經驗證請求可以重複送出，Day 4 先只改變請求內容中的一個角色訊息，讓讀者能把「互動迴圈」和「回答規則」分開觀察。system message 是模型輸入的一部分，不當作保證模型一定遵守的硬限制。

## D012：使用者原檔與 canonical raw 分層

- 狀態：superseded by D015
- 日期：2026-09-22
- 決策：`knowledge/inbox/` 保存使用者提供的原始檔案；`scripts/normalize_documents.py` 將 Markdown、文字、DOC、DOCX 和可抽取文字的 PDF 轉成 `knowledge/raw/` 的 canonical Markdown。raw 包含自動產生的 `document_id` 與 provenance，但不要求使用者手寫任何固定欄位。
- 理由：輸入文件的格式與結構不應被知識庫規範綁死。系統需要一致的文字與來源欄位，應該由可重跑的轉換工作流產生，而不是要求讀者先把文件改寫成內部格式。

## D013：Document ID 由來源識別材料決定

- 狀態：superseded by D016；識別碼已在來源轉換時產生
- 日期：2026-09-22
- 決策：normalizer 使用輸入文件的相對檔名與原始 bytes 產生 deterministic `doc-<hash>` ID，並另外保存完整 `source_sha256`。使用者不需要在文件內提供 Document ID。
- 理由：同一批輸入重新執行時應得到相同名稱，方便 raw 重建；內容或來源名稱改變時產生新的 ID，也不會把新版本靜默覆蓋成舊文件。

## D014：D012 取代 D002 的 raw source-of-truth 定義

- 狀態：superseded by D015
- 日期：2026-09-22
- 決策：保留 D002 作為早期設計紀錄，但目前的 source of truth 改為 `knowledge/inbox/`；`knowledge/raw/` 是可重建的 canonical evidence layer。
- 理由：D002 把「原始證據」和「可供程式處理的標準化文字」放在同一層，會要求使用者先遵守內部格式。D012 的分層才符合不同來源格式都能進入系統的目標。

## D015：raw 保存原始來源，ingest 留到後續

- 狀態：superseded by D016；曾取代 D012、D014
- 日期：2026-09-22
- 決策：`knowledge/raw/` 保存使用者交付的原始文件與可回讀的網頁原文，不要求固定格式或欄位。Day 8 只放入五份原始示範文件；文字抽取、來源識別、切塊與索引由後續 ingest 實作，衍生物不得覆寫 raw 原檔。
- 理由：raw 與 Miracle Vault 一樣代表可以回頭核對的原始來源。讀者至 Day 7 只完成 Chat Runner；Day 8 先保存資料，後續再教資料如何進入系統，較符合連載的理解順序。

## D016：Day 8 以本地模型建立來源轉換工作流

- 狀態：superseded by D018
- 日期：2026-09-22
- 決策：`knowledge/inbox/` 保存原始檔案或下載的網頁快照；`source-to-raw-md` skill 從文字檔、有文字層的 PDF 或靜態網頁抽取文字，交給本地 Qwen3.8-27B 排成 Markdown。程式計算穩定的 `document_id`、來源 SHA-256、來源快照路徑及模型名稱，檢查原文各行仍存在後，把固定格式的 Markdown 寫入 `knowledge/raw/`。文件版本與 chunk manifest 留給 Day 9。
- 理由：只建立資料夾不足以展示第二週的進展；來源轉換讓讀者能把自己的資料實際放入工作流。識別欄位由程式計算，避免模型捏造；原件留在 inbox 供日後核對。Qwen 非推理模式是本次在本機完成轉換的設定。

## D017：長文件不逐字交給 Qwen 轉寫

- 狀態：superseded by D018
- 日期：2026-09-22
- 決策：正式實驗仍使用 Qwen3.8-27B，但只讓它回答由檢索選出的短證據。長 PDF 的抽字、分段、來源欄位與索引由確定性程式完成；`source-to-raw-md` 的 Qwen 排版先保留給短文件與品質對照，不把它當成所有文件的必經步驟。Day 9 量測本機可用的輸入長度、延遲與記憶體，Day 13 以實測值設定回答時的證據預算。
- 理由：Day 8 的三份隨機完整論文（4、14、8 頁）都超過目前轉換器的大小或文字長度上限；已完成的 Day 5、Day 6 網頁逐字轉換則各花數分鐘。PDF 的多欄與圖表也不能靠純文字抽取保證還原。這些結果顯示「整篇文件排版」與「短證據問答」應分開測試，不能從前者的失敗直接推定後者也不可行。

## D018：Day 8 來源轉換改為程式處理全文

- 狀態：accepted；Day 8 批次入口與來源位置由 D019 補充
- 日期：2026-09-22
- 決策：`source-to-raw-md` 不呼叫模型，對文字檔保留完整正文、對 PDF 逐頁抽取文字層、對靜態網頁選取正文，加入來源識別與原件位置後寫入 `knowledge/raw/`。`knowledge/inbox/` 保存原檔或網頁快照。PDF 若有空白文字層的頁面就拒絕輸出；頁面文字、圖表、雙欄與公式仍需回看原檔。Day 9 才處理分段、索引，以及本機 Qwen 問答預算。
- 理由：三份完整論文共 26 頁由程式轉換後，逐頁輸出與 `pypdf` 抽取結果一致，耗時約 0.4～3.2 秒；三篇網頁約 0.2～0.3 秒。這解除了模型逐字轉寫的上下文與生成速度限制，但沒有解決 PDF 版面與圖像語意。正式問答仍使用 Qwen3.8-27B，待檢索後只送少量相關證據。

## D019：Day 8 由讀者執行批次轉換，已處理原檔移出待處理區

- 狀態：accepted
- 日期：2026-09-22
- 決策：讀者把支援格式的原檔放入 `knowledge/inbox/`，在終端機執行 `knowledge/convert.py`。程式逐份呼叫 `source-to-raw-md` 的轉換與驗證函式；成功後把原檔移入 `knowledge/inbox/processed/`，讓 `raw/` 的 `source_snapshot` 指向該處。後續執行略過 `processed/`，失敗或格式不支援的原檔保留在待處理區。Day 8 不要求 Chat Runner 或 Qwen 具備工具呼叫介面。
- 理由：讀者至 Day 7 只有互動式 Chat Runner，尚不能透過模型呼叫 skill。批次入口提供可直接照做的文件匯入步驟；分開待處理與已處理原檔，避免每次執行都重複轉換。

## D020：Day 9 以 tokenizer 與來源位置建立可重建 chunk manifest

- 狀態：accepted
- 日期：2026-09-23
- 決策：`knowledge/ingest.py` 只讀取 `knowledge/raw/*.md`，使用 `mlx-community/Qwen3.8-27B-4bit` 的 tokenizer，以行邊界優先、token slice 作為超長行後備，產生 `knowledge/index/manifest.json`。每個 chunk 保存 `chunk_id`、raw 行號、token 數、文字雜湊與文件版本；manifest 不覆寫 raw，也不假裝自己是搜尋索引。
- 理由：字元數不能直接代表模型輸入成本，chunk 又必須能回到原始文件位置。先保存 deterministic 的文件版本與分段結果，Day 10 才在這個產物上加入關鍵字搜尋；量測命令另以固定證據大小記錄本機 Qwen 的輸入 token 與延遲。

## D021：Day 10 先用 SQLite FTS5 做 lexical retrieval

- 狀態：accepted
- 日期：2026-09-24
- 決策：`knowledge/retrieve.py` 讀取 Day 9 的 chunk manifest，建立可刪除後重建的 SQLite FTS5 索引，以 BM25 排序關鍵字命中的 chunks。結果保留 chunk ID、來源檔名、raw 路徑、行號、token 數與 hash；查詢詞採參數傳入，多個詞目前以 AND 處理，不開放直接執行 FTS5 運算子。
- 理由：目前示範文件有明確的工程識別字與操作詞，先用標準函式庫提供的 SQLite FTS5 驗證「查詢 → 排序 → 回到來源」資料流，不先引入向量資料庫。SQLite 的內建 tokenizer 對中文分詞不足，因此另保存只供搜尋的 CJK 字元邊界欄位；原始 chunk 文字保持不變。

## D022：Day 11 先自動建立 source catalog，不要求手動分類

- 狀態：accepted
- 日期：2026-09-25
- 決策：`knowledge/wiki.py` 從 `knowledge/raw/*.md` 自動建立 `knowledge/wiki/index.md` 與 `knowledge/wiki/sources/*.md`。source page 保存 raw 路徑、來源 snapshot、文件 ID、hash 和 converter 資訊；不複製 raw 正文，也不要求使用者替文件選擇 `source`、`concept`、`howto` 或 `derived` 類型。
- 理由：每次匯入文件都要求使用者手動建立和分類頁面，會把知識頁變成另一份輸入資料。先自動建立可回查的 source catalog，才能驗證 wiki 導覽層的價值；跨文件的 concept、howto 和 derived 頁面留到有明確內容時再加入。

## D023：Day 13 以完整 message token 計算 context budget

- 狀態：accepted
- 日期：2026-09-25
- 決策：`knowledge/context.py` 在 FTS5 候選和 Local LLM 之間加入 bounded context builder。它先扣除 system prompt、問題、history、tool schema 和 output reserve，再依 BM25 排序選入完整 chunks；同一文件的重疊行號只保留排名較前者，所有淘汰原因都寫入結果。
- 理由：只加總 raw chunk 的 token 數會漏掉 chat template、來源標頭和未來工具／歷史的成本。先以同一個 tokenizer 計算實際 messages，才能在不擴大 context 的情況下知道證據可用空間，也才能診斷候選是被重複內容或預算淘汰。

## D024：Day 14 引用必須來自本次實際送入模型的 chunks

- 狀態：accepted
- 日期：2026-09-28
- 決策：`knowledge/rag.py` 將完整 bounded messages 送到本地 Qwen，驗證 `answer`、`citations`、`no_answer`；citation allowlist 只包含本次 selected chunks，來源檔名與 raw 行號由程式查回。只有 `finish_reason=stop` 才接受回覆，失敗保留完整 runtime 回應。token 計算與 request 都使用 `enable_thinking=false`。
- 理由：資料庫中存在某個 chunk，不代表模型這一輪看過它；讓模型產生來源位置也會新增可避免的錯誤。引用存在性、回答格式與完整生成可以由程式檢查，逐句語意支持仍需要另行驗證。

## D025：Day 14 將兩種拒答分開記錄，以少量固定案例驗收

- 狀態：accepted
- 日期：2026-09-28
- 決策：每次啟動 RAG 從 manifest 重建 FTS5；沒有選入證據時程式直接拒答，有證據但缺少答案時由模型回覆 `no_answer=true`、空引用。checkpoint 固定驗收跨文件數值、模型拒答與零命中三種情況，記錄 tokens、model_called、耗時與完整 context，結果 append 到已排除 Git 的 `runs/`。
- 理由：重建適合目前五份示範文件，能避免使用舊索引。分開拒答來源才能知道是不是模型真的判斷資料不足；三個固定案例只驗收目前資料流，不當成整體品質或安全保證。
