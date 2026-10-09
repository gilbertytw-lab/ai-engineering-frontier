# AI Engineering 研究前線：30 天讀懂一週一週長出來的技術脈絡

## Day 24：1,720 份文件建成索引，現有流程跑得動

Day 23 完成 1,720 份 Kubernetes Markdown 的匯入，修正了換行字元造成的驗證失敗。今天接著切塊、建立 SQLite FTS5 索引，確認原本用在少量範例上的流程，能否處理這批官方文件。

這批文件產生 36,807 個 chunks，切塊與寫出 manifest 花了 18.685 秒，FTS5 建置花了 0.575 秒，合計約 19 秒。以目前的資料規模，建置時間沒有構成問題。

固定查詢詞暖身後，全量索引的查詢 p95 為 5.861 毫秒。目前流程能完成切塊、建索引與查詢，也留下時間和容量的比較基準。還沒確認的是：查回來的前 5 個 chunks，是否包含回答題目需要的證據。

[GitHub Repo](https://github.com/gilbertytw-lab/ai-engineering-frontier)

## 固定輸入，留下可比較的基準

語料沿用 Day 23 的 Kubernetes website commit `77db41e9c776b614fdb31de4cc6c8e9a70673817`。我將 `data/day23/results/raw/` 按檔名排序，取前 100 份、前 500 份和全部 1,720 份。三組互相包含，但沒有依主題或文件長度抽樣。

每個 chunk 是一小段可供搜尋的內容，上限 160 tokens，重疊預算 24 tokens；token 數由本機快取中的 `mlx-community/Qwen3.8-27B-4bit` tokenizer 計算，設定沿用 Day 9。

新增的 `knowledge/benchmark_scale.py` 呼叫既有的 ingest 和 retriever，沿著「raw → chunk manifest → SQLite FTS5 → 固定查詢」量測。查詢詞保存在 `data/day24-queries.json`，逐筆結果保存在 `data/day24-scale-summary.json`。

每組都開新的 Python 子程序，從空目錄建立 manifest 和資料庫。環境是 Apple M5、32 GiB 記憶體、macOS 26.6.2、Python 3.13.15、SQLite 3.53.1。建置各量一次，數字只代表這台電腦的單次紀錄。

## 約 19 秒建好索引，查詢落在毫秒級

| 文件數 | chunks | 切塊與 manifest | FTS5 建置 | 查詢 p50 | 查詢 p95 |
|---:|---:|---:|---:|---:|---:|
| 100 | 2,689 | 2.531 秒 | 0.037 秒 | 0.113 毫秒 | 0.661 毫秒 |
| 500 | 10,543 | 5.820 秒 | 0.157 秒 | 0.182 毫秒 | 1.654 毫秒 |
| 1,720 | 36,807 | 18.685 秒 | 0.575 秒 | 0.357 毫秒 | 5.861 毫秒 |

「切塊與 manifest」包含 tokenizer 載入、raw 讀取、切塊、雜湊計算和 JSON 寫檔。「FTS5 建置」包含重新讀取 manifest、建立資料表、插入 chunks、執行 `optimize`、提交與關閉資料庫。兩段都不含 Day 23 的原文轉換。`optimize` 會合併索引內的結構，說明見 [SQLite FTS5 文件](https://sqlite.org/fts5.html#the_optimize_command)。

查詢詞由 Day 22 的十題主題人工選定，再加上常見詞 `Pod` 和零命中詞，共 12 組，沒有自動翻譯中文問題。每組先暖身一次，再固定順序跑 20 輪，每個規模留下 240 筆耗時。

計時涵蓋完整的 `search()`，包括連線、MATCH、BM25 排序與結果處理。p50 是中位數；p95 表示這批紀錄中至少 95% 的查詢耗時不超過該值。這是暖身後固定詞的混合分布，無法直接代表使用者實際提問的延遲。

全量索引裡，`readiness probe` 匹配 69 個 chunks，p95 為 0.240 毫秒；`Pod` 匹配 7,091 個 chunks，p95 為 6.246 毫秒。兩者都只回傳 5 筆，耗時也都落在毫秒級。

`LIMIT 5` 限定回傳數量，查詢仍要處理符合 MATCH 的候選與排序，BM25 的排序方式見 [SQLite 官方說明](https://sqlite.org/fts5.html#the_bm25_function)。零命中詞的 p95 只有 0.157 毫秒；只測查不到的詞，就會漏看常見詞的成本。候選數核對結果保存在 `data/day24-index-audit.json`。

## 檔案容量與程序記憶體分開算

全量 raw 為 16.56 MiB，manifest 為 27.89 MiB，SQLite 為 74.98 MiB；後兩個衍生檔案合計約 102.87 MiB。1 MiB 是 1,048,576 bytes。

raw 容量包含來源欄位；manifest 保存 chunk 正文、來源位置、行號和雜湊；SQLite 再保存可搜尋的文字與 FTS5 索引。規劃儲存空間時，這些檔案都要算進去。

全量程序的峰值 RSS 為 618.91 MiB。這是從載入 tokenizer 到切塊、建索引、查詢與完整性檢查的最高常駐記憶體用量，無法拆出 FTS5 單獨用了多少。這條路徑只載入 tokenizer，Qwen 模型權重的用量仍要在模型作答時另外量測。

## 從 Repository 根目錄重跑

備妥 Day 24 程式、Day 23 語料與 tokenizer 的本機快取後執行：

```bash
HF_HUB_OFFLINE=1 uv run python knowledge/benchmark_scale.py \
  --raw-dir data/day23/results/raw \
  --workspace-root data/day24/reproduction \
  --sizes 100 500 1720 \
  --max-tokens 160 --overlap-tokens 24 \
  --rounds 20 --limit 5
```

`HF_HUB_OFFLINE=1` 要求使用本機快取。manifest、SQLite 和重跑結果會寫入 `data/day24/reproduction/`，總表位於其中的 `summary.json`。工作區已存在時程式會停止；再次執行可將 `--workspace-root` 改成 `data/day24/reproduction-2`，保留前一次紀錄。

## 尚未核對的是檢索品質

三組 SQLite 都通過資料庫與 FTS5 完整性檢查；raw 與 chunk 雜湊、行號、資料庫筆數也已核對，量測前後 raw 不變。全專案 91 個測試通過。

這次確認了：1,720 份文件能建立索引，固定查詢也能完成，現有的切塊與索引流程可以繼續使用。量測到搜尋回傳結果為止，沒有模型生成答案的耗時。

前 5 個 chunks 是否包含 Day 22 標記的支援證據，仍要逐題對回題目和原文。
