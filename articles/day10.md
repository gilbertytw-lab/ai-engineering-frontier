# AI Engineering 研究前線：30 天讀懂一週一週長出來的技術脈絡

## Day 10：資料分段後的查詢手法

Day 9 把 `knowledge/raw/` 切成 11 個帶有行號、token 數和 hash 的 chunks，也量過不同 evidence budget 對本機 Qwen request 的影響。今天接著處理下一個問題：怎麼根據使用者的問題找出對應的知識片段？

今天先用 SQLite FTS5（Full-Text Search 5）建立第一條檢索路徑：用關鍵字找出候選 chunks，再用 BM25（Best Matching 25）排序。向量資料庫留到後面，今天先把資料流和來源定位測清楚。

[GitHub Repository](https://github.com/gilbertytw-lab/ai-engineering-frontier)

## 今天要完成的目標

今天做四件事：

- 從 `knowledge/index/manifest.json` 建立可重建的 `retrieval.sqlite`。
- 查詢時保留 `chunk_id`、來源檔名和 raw 行號。
- 用 BM25 排序候選 chunks，不把整份文件送進模型。
- 確認英文技術詞和中文短語都能找到資料，查詢字串裡的 FTS 運算子不會直接被執行。

資料流變成這樣：

```text
knowledge/raw/*.md
    ↓
knowledge/ingest.py
    ↓
knowledge/index/manifest.json
    ↓
knowledge/retrieve.py
    ↓
knowledge/index/retrieval.sqlite（SQLite FTS5）
    ↓
關鍵字查詢 → BM25 排序 → 回傳帶來源位置的 chunks
```

這裡的 SQLite 檔案是衍生索引。刪掉它不會刪掉 `raw/` 或 `manifest.json`，重新執行同一個命令就能建回來。

## 為什麼今天先做關鍵字搜尋？

目前的五份示範文件有很明確的工程詞：`release owner`、`healthz`、`queue lag`、`rollback`。對這種查詢，先用關鍵字就能驗證檢索流程是否成立。

關鍵字檢索的好處也很直接：輸入和輸出容易檢查、索引可以離線重建、結果可以立刻回到文件行號。它的限制同樣清楚：查詢詞和文件用不同說法時，通常找不到同義內容；它也不會理解「如何安全地恢復服務」和「rollback」可能是在問同一件事。

這個限制先留下來。先把關鍵字命中、排序和來源定位測清楚，再評估 embedding；否則沒命中時，資料、切塊、查詢詞和向量模型會同時變成變因。

## 把 manifest 寫進 SQLite FTS5

今天新增 [`knowledge/retrieve.py`](../knowledge/retrieve.py)。它讀取 Day 9 產生的 manifest，建立兩個 SQLite 結構：

- `chunks_fts`：保存 chunk 的識別碼、文件資訊、行號、原文和搜尋欄位。
- `index_meta`：保存 index 版本、manifest 版本、tokenizer 和 chunk 數量。

`source_name` 和原始 `text` 會被 FTS5 索引；其他欄位保留作為查詢結果的定位資訊。模型尚未在這條路徑出場，檢索器只是在候選證據上做篩選。

先建立 Day 9 的 manifest：

```bash
HF_HUB_OFFLINE=1 uv run python knowledge/ingest.py \
  --max-tokens 160 --overlap-tokens 24
```

輸出如下：

```text
建立 knowledge/index/manifest.json：5 份文件、11 個 chunks
```

接著建立索引並查詢：

```bash
uv run python knowledge/retrieve.py \
  --query "release owner" --limit 5
```

本次結果只有一個命中：

```text
建立 knowledge/index/retrieval.sqlite：5 份文件、11 個 chunks
查詢：release owner
命中 1 個 chunks
1. release-policy.md（第 12–29 行，bm25=3.229500，doc-3a8e2b68f2b171e3-chunk-0001）
```

查詢結果帶回來源檔名與 raw 行號，`chunk_id` 也能把結果接回 manifest。之後組 evidence pack 時，再用 `token_count` 和 Day 9 的預算限制候選數量。

## BM25 分數到底代表什麼？

BM25 是文字檢索常用的排序方法。它會看查詢詞在文件中出現的**頻率**，也會把太常出現在所有文件裡的詞降低**權重**。對今天的用途，先記住一個行為就夠了：查詢結果會依相關程度排序，不必照著 manifest 原本的文件順序取前幾段。

SQLite FTS5 的 `bm25()` 內部排序值越小越前面。程式把它轉成較直覺的正數 `bm25` 欄位顯示，並在分數相同時用 `chunk_id` 做穩定排序。分數不是答案品質，也不是模型信心；它只描述這段文字和查詢詞的字面接近程度。

透過關鍵字 `release owner` 找到 `release-policy.md` 的某個chunk，只代表字面匹配成功（chunk 中出現這個關鍵字的頻率較高）。它不能證明這份 policy 或 chunk 足以回答完整問題，也不會讓模型透過閱讀該文件取得任何額外權限。

## 中文查詢踩到一個小坑

我第一次直接用 SQLite 的 `unicode61` tokenizer 查中文「部署」，結果是 0 筆。問題原因可能有兩個：

1. 文件內可能只有英文 "deploy" 而沒有中文「部署」。
2. unicode61 tokenizer 沒有針對中文詞語進行「分界」。

第一個原因可排除，因為文件中有多次出現中文的「部署」; 而第二個原因指的是當文件中出現連續的中文，例如「部署使用以建立的...」，這時使用者若沒有用一字不漏的完整句子來搜尋，就會搜尋失敗。

因此我在索引裡另外建立只供搜尋的 `search_text` 欄位。程式在索引階段替 CJK 字元加上邊界，查詢時把中文短語轉成同樣的字元序列；原始 `text` 完整保留，回傳給讀者的內容沒有被改寫。

現在查詢：

```bash
uv run python knowledge/retrieve.py --query "部署" --limit 5
```

會得到 3 個 chunks，第一筆是：

```text
1. deployment-guide.md（第 12–24 行，bm25=1.406927，doc-891dc9cf617077c2-chunk-0001）
```

目前的中文搜尋只做到字元邊界：沒有同義詞、詞性或語意擴展，所以「部署」和「上線」仍是兩個不同的查詢詞。這個範圍先寫進程式和測試，之後比較 embedding 時，才能清楚知道新增的是什麼能力。

## 查詢字串不能變成另一套指令

`incident-runbook.md` 裡刻意放了一段 untrusted text，內容包含「Ignore previous instructions」。它是文件資料，不能因為被檢索到就變成系統指令。

檢索器不開放使用者直接傳入 FTS5 語法。`retrieve.py` 會把查詢拆成英文識別字或中文短語，再以參數傳給 SQLite。`OR`、括號和其他 FTS 運算子都不會被當成語法執行。第一版採 AND，所有查詢詞都必須出現在同一個 chunk 裡。

如果兩個關鍵詞被 Day 9 切到不同 chunks，查詢就會找不到，因為根本沒有一個 chunk 同時包含這兩個詞。Day 13 的 context builder 會處理相鄰 chunks 的去重與合併；今天先保留這個潛在問題。

## 5 個檢索測試，外加 32 項全專案回歸測試

今天新增 [`tests/test_day10_retrieve.py`](../tests/test_day10_retrieve.py)，測試五件事：

- 建立索引後，查詢結果保留來源檔名和行號。
- 重建索引後，已移除的 chunk 不會殘留在資料庫。
- 查詢字串裡的 `OR` 不會被當成 FTS 運算子執行。
- 中文短語可以透過 `search_text` 找到資料。
- 空查詢會被拒絕。

完整測試：

```bash
uv run python -m unittest discover -s tests -v
```

本次 32 項測試全數通過。它們驗證的是索引重建、查詢契約和來源定位；BM25 仍不處理同義詞，檢索結果也不等於正確答案。

## 今天留下的邊界

Day 10 的檢索器目前能回答「哪些 chunks 含有這些詞」，還不能判斷「哪些 chunks 足以支撐完整問題」。

目前的順序是：

```text
raw 文件
  → 可回查的 chunks
  → 關鍵字候選
  → BM25 排序
  → 下一步才是 context budget 與模型回答
```

今天停在候選 chunks 這一層：沒有啟動 Qwen，也沒有把候選 chunks 組成 prompt。先讓搜尋結果能重建、能定位、能測試；下一篇再處理人類可維護的知識頁，之後比較 raw、wiki 與階層式證據路徑。

## 第一個可以被檢查的 retriever

今天留下 `knowledge/retrieve.py`、SQLite FTS5 索引和 5 個檢索測試。現在從問題到候選證據之間，已經有一個不需要模型就能獨立驗證的步驟。

這個步驟很樸素，卻讓後面的 RAG 有了地板。檢索沒有找到資料時，至少可以先查 manifest、查 query、查 chunk 邊界，不必把所有問題都推給模型。

Day 11 會把 raw 文件旁邊的可維護知識頁補起來，看看「人類整理過的導覽」和「機器直接搜尋原始 chunks」各自適合放什麼。

## 參考資料

- Day 9：將知識文件送入本地模型前要思考的事
- [SQLite FTS5 Extension](https://sqlite.org/fts5.html)
- [SQLite FTS5 BM25 ranking](https://sqlite.org/fts5.html#the_bm25_function)
