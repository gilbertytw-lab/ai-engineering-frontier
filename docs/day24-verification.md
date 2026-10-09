# Day 24 Kubernetes 索引規模與查詢效能

驗證日期：2026-10-07（Asia/Taipei）。文章：[Day 24：資料變多後，索引和查詢慢多少？](../articles/day24.md)。

## 固定輸入與程式

沿用 Day 23 的 Kubernetes website commit `77db41e9c776b614fdb31de4cc6c8e9a70673817`，CC BY 4.0。輸入為 Repository 中 `data/day23/results/raw/*.md` 的 1,720 份 raw，實際合計 17,362,225 bytes；這個數字按本次封裝後的 raw（包含來源欄位）計算，與原始 Markdown 的 16,198,192 bytes 分開。

raw fingerprint：`4f34b15de3c0e8cf35ecfcdfe536b440e7e4410c90adf5f9b7155e79fa96ac6b`。依 raw 檔名排序，逐份將 UTF-8 檔名、NUL 與原始 bytes 的 SHA-256 digest（32 bytes）送入整批 SHA-256。這個算法用於本日 raw 核對，與 Day 22 的原始語料 checksum 分開。

固定查詢詞：[data/day24-queries.json](../data/day24-queries.json)，SHA-256 `c39114b573da6b7775adf7fce55bd33e798aba28cf896844e5c339c40a072b9e`。十組英文詞由 Day 22 題目主題人工選定，另加 `Pod` 與 `frontierday24nomatch7d81`。中文題集沒有直接送入 FTS，也沒有自動改寫；本日不使用查詢詞的命中數判定 Recall@K。

新增 `knowledge/benchmark_scale.py`，直接沿用 `ingest.build_manifest()`、`retrieve.build_index()` 和 `retrieve.search()`。ingest 增加可選的 `document_limit`／`--document-limit`，依排序取前 N 份；未指定時保留原本全量行為。raw 讀取改用 `newline=""`，讓 `raw_sha256` 與 CRLF 文件的實際 bytes 一致，原始 raw 未改動。

## 環境與量測邊界

- Apple M5、32 GiB 記憶體；macOS 26.6.2 arm64。
- Python 3.13.15、SQLite 3.53.1、transformers 5.16.1。
- tokenizer：`mlx-community/Qwen3.8-27B-4bit`，只讀本機快取；子程序環境固定 `HF_HUB_OFFLINE=1`、`TOKENIZERS_PARALLELISM=false`。
- chunks：160 tokens 上限、24 tokens 重疊預算；三組實際最大 chunk 都為 160 tokens。
- 每組使用新的 Python 子程序與空的輸出目錄，各建置一次；沒有清除 OS 檔案快取。100、500、1,720 組依序執行，選取 raw 檔名排序的前 N 份，較小組為較大組的子集。
- ingest 計時：tokenizer 載入、raw 解析、切塊、hash、manifest 序列化與寫檔。
- FTS 建置計時：manifest 讀取／解析、schema、插入、`optimize`、commit 與 close。manifest 物件先釋放，再執行 FTS 建置；每組新資料庫沒有沿用舊索引。
- 查詢計時：完整 `search()`，包含 query parsing、新連線、MATCH、BM25 排序、fetch、Python 結果轉換與 close。未含索引建置、context 組裝或 LLM request。
- 每組 12 詞先各暖身一次，再固定順序執行 20 輪，共 240 筆；每次 `limit=5`。暖身不納入分位數，每次結果與該詞暖身結果比較，確保索引固定時結果一致。
- p50 為 `statistics.median()`；p95 為 nearest rank，排序後取 `ceil(0.95 * N)`，240 筆的第 228 筆、20 筆的第 19 筆。
- RSS 取子程序的 `resource.getrusage(RUSAGE_SELF).ru_maxrss`。這台 macOS 的 `man getrusage` 明定單位為 bytes；Linux 分支乘 1024。峰值涵蓋整個 worker，包含 tokenizer 和完整性檢查，不能解讀為 FTS 單獨用量或 Qwen 作答時的用量。未載入模型權重。

## 原始量測結果

測量完成時間：2026-10-07 23:33:26（Asia/Taipei），報告以 UTC 保存。

| 文件數 | raw bytes | chunks | ingest 秒 | FTS 建置秒 |
|---:|---:|---:|---:|---:|
| 100 | 1,249,614 | 2,689 | 2.531371375 | 0.037234250 |
| 500 | 5,004,216 | 10,543 | 5.820277250 | 0.156626250 |
| 1,720 | 17,362,225 | 36,807 | 18.685379000 | 0.575466083 |

| 文件數 | manifest bytes | SQLite bytes | 峰值 RSS bytes | query p50 ms | query p95 ms |
|---:|---:|---:|---:|---:|---:|
| 100 | 2,115,728 | 6,770,688 | 506,478,592 | 0.113229500 | 0.660583000 |
| 500 | 8,423,468 | 25,821,184 | 507,117,568 | 0.182041500 | 1.653500001 |
| 1,720 | 29,246,578 | 78,622,720 | 648,970,240 | 0.357062500 | 5.861042000 |

完整報告：[data/day24-scale-summary.json](../data/day24-scale-summary.json)，保存選取檔名、每個規模的 raw fingerprint、逐詞 20 筆耗時、回傳 chunk IDs、環境、計時範圍與分位數算法。建置數字是單次量測，未量測建置的 p50／p95。查詢統計是暖身後固定 12 詞的混合分布，無法代表一般使用者問題、冷快取或多人並行。

全量組的 `Pod` 匹配 7,091 chunks，回傳 5 個，逐詞 p95 6.246125000 ms；`readiness probe` 匹配 69，回傳 5，p95 0.240083000 ms；零命中詞 p95 0.157375000 ms。候選數是在量測完成後另用 `count(*) ... MATCH ?` 查得，未納入原計時。完整候選數與索引 audit 見 [data/day24-index-audit.json](../data/day24-index-audit.json)。

## 重跑命令

從 Repository 根目錄執行；工作區必須尚未存在。再次重跑使用新的 `data/day24/reproduction-*` 名稱，避免覆寫量測紀錄。

```bash
HF_HUB_OFFLINE=1 uv run python knowledge/benchmark_scale.py \
  --raw-dir data/day23/results/raw \
  --workspace-root data/day24/reproduction \
  --sizes 100 500 1720 \
  --max-tokens 160 --overlap-tokens 24 \
  --rounds 20 --limit 5
```

第一次實際執行使用相同預設值的 `HF_HUB_OFFLINE=1 uv run python knowledge/benchmark_scale.py`。產物保留於 `data/day24/reproduction/`，由 `.gitignore` 排除；小型結果報告另保存於上述兩份 JSON，供文章核對。

## 驗證結果

```bash
uv run --with pypdf python -m unittest discover -s tests -v
uv run python skills/source-to-raw-md/scripts/validate.py \
  data/day23/results/raw --root "$PWD"
git diff --check
```

全專案 91 個測試通過，包含本日新增 6 個：CRLF raw SHA-256、排序取前 N 與來源不變、分位數算法、暖身排除與查詢不重建索引、非法查詢集合、超量規模在寫入工作區前拒絕。測試中的 fake tokenizer 只驗證程式流程，文章數字來自三組真實 tokenizer 的執行。

三組 SQLite `PRAGMA integrity_check` 與 FTS5 `integrity-check` 全數通過；每組 manifest 文件數／chunk 數與 FTS5 筆數一致。逐份確認 raw hash、chunk text hash、來源行號範圍與 token 上限，核對結果保存於 `data/day24-index-audit.json`。1,720 份 raw 通過既有 converter validator，完整輸出保存在 `data/day24/reproduction/raw-validation.log`。

每組和整批量測前後 raw fingerprint 相同，查詢詞檔案的 SHA-256 也相同。既有 `knowledge/index/manifest.json` 無 Git 差異（SHA-256 `34aa5ec4416d9b7c86338e3cd836236b4bb51eb5c25c9b597083769fd6fc643d`），`harbor-api` 示範文件與索引未重建。

本日沒有執行 Qwen 作答、Recall@K 或引用支持度評分。文章只包含可公開存取的 Repo 與 SQLite 官方連結；尚未發布的 Day 24 程式和資料只寫路徑文字。Git commit、push 與發文未執行。
