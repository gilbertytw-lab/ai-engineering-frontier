# Day 10 驗證紀錄

## 範圍

Day 10 新增 SQLite FTS5 lexical retriever。它讀取 Day 9 的 `knowledge/index/manifest.json`，建立可重建的 `knowledge/index/retrieval.sqlite`，並保留 chunk 的來源檔名、raw 路徑、行號、token 數與 hash。

本日沒有啟動 Qwen，也沒有把檢索結果送進模型。Qwen 的 evidence budget 與回答組裝留給後續文章。

## 實際命令

```bash
HF_HUB_OFFLINE=1 uv run python knowledge/ingest.py \
  --max-tokens 160 --overlap-tokens 24

uv run python knowledge/retrieve.py \
  --query "release owner" --limit 5
```

輸出：

```text
建立 knowledge/index/manifest.json：5 份文件、11 個 chunks
建立 knowledge/index/retrieval.sqlite：5 份文件、11 個 chunks
查詢：release owner
命中 1 個 chunks
1. release-policy.md（第 12–29 行，bm25=3.229500，doc-3a8e2b68f2b171e3-chunk-0001）
```

中文查詢也已驗證：`部署` 命中 3 個 chunks，第一筆是 `deployment-guide.md` 第 12–24 行。SQLite `unicode61` 對 CJK 沒有提供本專案需要的分詞，因此索引另外建立 `search_text`，以字元邊界支援中文短語；原始 `text` 不變。

## 自動化測試

```bash
uv run python -m unittest tests.test_day10_retrieve -v
uv run python -m unittest discover -s tests -v
```

結果：Day 10 測試 5 項通過；全專案測試 32 項通過。

測試涵蓋：

- BM25 查詢會保留來源檔名與 raw 行號。
- 重建索引會移除 manifest 中已不存在的 chunks。
- 查詢字串中的 FTS 運算子不會被直接執行。
- CJK 短語可以找到中文內容。
- 空查詢會被拒絕。

## 已知限制

- 多個查詢詞目前採 AND，必須出現在同一個 chunk。
- 關鍵字檢索不處理同義詞或語意相似度。
- 中文目前採字元邊界，不是完整中文斷詞器。
- BM25 分數只代表文字匹配程度，不代表答案正確率。
- `retrieval.sqlite` 是可刪除後重建的衍生索引，`raw/` 與 `manifest.json` 才是查詢前的來源材料。
