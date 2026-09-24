# AI Engineering 研究前線：30 天讀懂一週一週長出來的技術脈絡

## Day 11：知識庫不能只是關鍵字搜尋

Day 10 完成 SQLite FTS5（SQLite 的全文檢索功能）後，系統現在能從 11 個 `chunks` 找到含有關鍵字的內容。

`FTS5` 可以回答「文字在哪裡」，使用者還缺一個從文件清單開始瀏覽的入口。五份 `harbor-api` 文件各自放在 `knowledge/raw/`，使用者要先知道檔名，才知道該從哪一份開始讀。

這裡需要一個 wiki 層。

`wiki` 層就是放在 `raw` 文件旁邊的導覽頁。它列出來源文件，並保存文件標題、來源名稱、`document_id` 和 raw 連結。

`raw` 保存可回查的原始內容，`FTS5` 找出候選 `chunks`，`wiki` 層則讓人從文件清單開始瀏覽。缺少 wiki 時，使用者只能依賴檔名或直接下關鍵字查詢。

這次先做來源目錄（source catalog）。`knowledge/wiki.py` 讀取 raw 文件，自動產生來源索引和來源頁（source page）；使用者不用手動建立頁面，也不用先替來源文件分類。

[GitHub Repository](https://github.com/gilbertytw-lab/ai-engineering-frontier)

## 今天要完成的事情

今天新增三項可驗證的產物：

- `knowledge/wiki.py`：從 `knowledge/raw/*.md` 產生來源索引。
- `knowledge/wiki/index.md`：列出所有來源文件和對應的 source page。
- `knowledge/wiki/sources/*.md`：每份 raw 文件一頁，保留來源資訊（provenance）和回查連結。

這一版的 `wiki` 只負責導覽，原始內容仍留在 `knowledge/raw/`，也不會呼叫 Qwen。

## 一個命令產生來源頁

在專案根目錄執行：

```bash
uv run python knowledge/wiki.py
```

這次的輸出是：

```text
建立 /Users/gilbert/Projects/ai-engineering-frontier/knowledge/wiki：5 份來源、5 個 source pages、index.md
```

產生的目錄如下：

```text
knowledge/wiki/
├── index.md
└── sources/
    ├── doc-3317e1a5be5eb33f.md
    ├── doc-3a8e2b68f2b171e3.md
    ├── doc-891dc9cf617077c2.md
    ├── doc-e837190a1e6017a9.md
    └── doc-fe96deca8c6c492f.md
```

頁面檔名使用 `document_id`，所以原始來源檔案改名後，對應的 wiki 頁面仍沿用同一個識別方式。每一頁的 `frontmatter`（前置資料）會保存：

- `document_id`
- `source_name`
- `raw_path`
- `source_snapshot`
- `source_sha256`
- `extracted_sha256`
- converter 的方法和版本

頁面正文只放文件標題、來源欄位和 raw 連結。例如，`api-spec.md` 會產生一個來源頁，指向 `knowledge/raw/doc-fe96deca8c6c492f.md`。

raw 正文不會在 wiki 再放一份。多一份副本只會增加同步成本，回查仍然要靠原始連結。

## source catalog 不等於完整 wiki

今天只產生 `source` 頁；`concept`、`howto` 和 `derived` 頁都還沒有。

source page 可以直接從既有中介資料（metadata）產生；跨文件的概念整理需要判斷，不能只靠檔名猜測。

例如「production release 前要檢查什麼」會同時牽涉 `release-policy.md` 和 `deployment-guide.md`。這種內容之後可以成為 `howto` 或 `derived` 頁，但今天先不把它假裝成已經存在的知識結論。

現在的資料流是：

```text
knowledge/raw/*.md
    ↓
knowledge/wiki.py
    ↓
knowledge/wiki/index.md + sources/*.md
```

`manifest.json` 和 SQLite FTS5 維持原本的資料流。source catalog 只是導覽層，不會取代 `chunk manifest`，也不會直接成為模型的回答內容。

## 重跑同一個命令會發生什麼事？

這個腳本的輸出必須可重建，讓 wiki 能跟著 raw 文件狀態更新，不留下難以確認版本的頁面。

我補了三個測試：

1. 相同 raw 文件重跑兩次，`index.md` 和 source pages 內容完全相同。
2. 已不存在、且由腳本產生的 source page 會被移除；手寫頁面會保留。
3. 不同 raw 文件使用相同 `document_id` 時直接拒絕，避免產生互相覆蓋的頁面。

Day 11 的測試：

```bash
uv run python -m unittest tests.test_day11_wiki -v
```

輸出結果：

```text
Ran 3 tests in 0.006s

OK
```

完整回歸測試結果：

```bash
uv run python -m unittest discover -s tests -v
```

```text
Ran 35 tests in 0.059s

OK
```

執行時間會隨電腦不同而變動；這次測試涵蓋 3 個 Day 11 行為，以及既有的 32 個測試。

## 今天留下的邊界

Day 11 產生的是 source catalog。完整的知識 wiki 還沒完成。

目前可以確定：

- source catalog 可從 raw 文件重建；source page 會保留回到 raw 的連結，也不要求使用者手動建立頁面或分類來源。
- wiki 尚未產生跨文件的概念、操作流程或衍生結論。
- `FTS5` 目前尚未讀取 wiki，wiki 內容也尚未放進 Qwen 的 prompt。

這個範圍故意很小。今天先讓來源有一個不需要額外輸入的入口，後面再處理哪些整理內容值得保存，以及它們要怎麼回到原始證據。

## 參考資料

- Day 10：資料分段後的查詢手法
- [Knowledge files](../knowledge/README.md)
- [設計決策紀錄](../docs/design-decisions.md)
