# Knowledge files

`inbox/` 是待處理區，`inbox/processed/` 保存已成功轉換的原檔，`raw/` 保存固定格式的 Markdown。Day 8 的 [`convert.py`](convert.py) 由使用者在終端機執行；它使用 [`source-to-raw-md`](../skills/source-to-raw-md/SKILL.md) 的轉換與驗證程式，不需要 Qwen 呼叫 skill。

目前有五份自行撰寫的虛構 `harbor-api` 文件，用於後續檢索實驗：

```text
knowledge/inbox/processed/api-spec.md    已處理原檔
knowledge/raw/doc-fe96deca8c6c492f.md   轉換結果
```

把 `.txt`、`.md`、`.markdown`、有文字層的 `.pdf`、`.html` 或 `.htm` 放入 `knowledge/inbox/`，在專案根目錄執行：

```bash
uv run --with pypdf --with fonttools python knowledge/convert.py
```

程式會處理待處理區中所有支援的檔案，逐份核對 raw 與原件，成功後才把原檔移入 `processed/`。下次執行會略過 `processed/`。失敗或格式不支援的檔案留在待處理區，並在終端機顯示原因。也可以單獨重查整個 `raw/`：

```bash
uv run --with pypdf --with fonttools python skills/source-to-raw-md/scripts/validate.py knowledge/raw
```

PDF 每頁都有標記，但圖表、公式、表格與雙欄順序要對照原檔；掃描 PDF 需要先做 OCR。只靠 JavaScript 顯示正文的網頁也不在目前範圍。Day 11 的 [`wiki.py`](wiki.py) 會從 `raw/` 自動建立 `wiki/index.md` 與 `wiki/sources/`，使用者不需要手動替來源文件分類。Day 10 的 [`retrieve.py`](retrieve.py) 會從 Day 9 的 chunk manifest 建立 SQLite FTS5 索引；它目前只回傳關鍵字命中的候選 chunks，還沒有接到 Chat Runner 或 Qwen prompt。

重建 source catalog：

```bash
uv run python knowledge/wiki.py
```

source pages 只提供來源導覽與 provenance，完整正文仍以 `raw/` 為準。

這五份示範文件不含真實公司資料、秘密或個人資料。`incident-runbook.md` 裡的英文指令句是刻意加入的測試資料，不是系統指令。
