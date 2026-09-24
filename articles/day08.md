# AI Engineering 研究前線：30 天讀懂一週一週長出來的技術脈絡

## Day 8：為本地知識庫打地基

Day 7 的 Chat Runner 已經能帶著對話紀錄呼叫本地 Qwen3.8-27B。今天我們要開始建立知識庫，第一步驟就是建立一個存放原始資料的地方，並建立一個能將原始資料轉換成.md檔的轉換器。但在這台硬體上，模型能使用的上下文非常有限，所以轉換器必須純是Python檔案且轉換過程不經過模型。程式直接讀取文字檔、有文字層的 PDF 和靜態 HTML，寫出帶來源資訊的 Markdown；Qwen 留給後續只需要少量證據的問答。

[GitHub Repository](https://github.com/gilbertytw-lab/ai-engineering-frontier)

## 今天做的事

```text
文字檔／有文字層的 PDF／靜態網頁 HTML
    ↓
把原檔放進 knowledge/inbox/
    ↓
執行 knowledge/convert.py
    ↓
程式全程讀取、轉換並寫出 Markdown
    ↓
原檔移到 knowledge/inbox/processed/
轉換結果寫入 knowledge/raw/
```

`inbox/` 是待處理區。成功處理的原檔會移到裡面的 `processed/`，`raw/` 則存放統一格式的 Markdown。原檔仍然保留，讓後續程式或讀者需要時可以追溯來源。

批次入口是 [`knowledge/convert.py`](../knowledge/convert.py)。它接受 `.txt`、`.md`、`.markdown`、`.pdf`、`.html` 和 `.htm`，逐份處理 `inbox/` 裡的檔案，不需要啟動模型。文字檔與 Markdown 保留完整正文；PDF 按頁抽取文字層；HTML 則取出文章正文，最後把結果寫入 `knowledge/raw/`。

## 把自己的文件放進 inbox，執行一次

把要匯入的 Markdown、文字檔、PDF 或靜態 HTML 放進 `knowledge/inbox/`。在專案根目錄執行：

```bash
uv run --with pypdf --with fonttools python knowledge/convert.py
```

執行完成後，成功處理的原檔會移到 `knowledge/inbox/processed/`，轉換結果寫入 `knowledge/raw/`。之後只要把新檔案放進 `inbox/`，再執行同一個命令即可。以 `api-spec.md` 為例，產生的是 `knowledge/raw/doc-fe96deca8c6c492f.md`。打開檔案，最前面是程式加上的來源資訊，後面才是原本的文件正文：

```yaml
---
document_id: "doc-fe96deca8c6c492f"
source_name: "api-spec.md"
source_type: "text"
source_format: "md"
source_sha256: "a389a84e365eb143ee127b3949a423c1c43684ba945d617196338c488da2542c"
source_snapshot: "knowledge/inbox/processed/api-spec.md"
extracted_sha256: "a389a84e365eb143ee127b3949a423c1c43684ba945d617196338c488da2542c"
conversion_method: "programmatic"
converter_version: "0.3.0"
---
```

這些欄位讓後續程式知道文字來自哪份原檔，也讓每份 raw Markdown 都能追溯回來源。`document_id` 是檔案識別碼，`source_sha256` 是原檔的指紋；兩者都由程式計算，不需要讀者自己填。原本就是 Markdown 的文件，正文直接保留。

## 程式處理哪些來源？

同一支程式也能處理靜態網頁，保留文章標題、段落、連結與程式碼區塊。整個轉換階段不需要 Qwen 參與。

PDF 會從第一頁讀到最後一頁，並在 Markdown 中保留對應的頁碼標記。程式只處理 PDF 裡可抽取的文字層，不負責理解圖表、公式或雙欄版面的閱讀順序。

因此，`raw/` 是供程式搜尋與引用的文字副本，不是 PDF 視覺版面的完整重建。遇到重要數值、表格或圖說，仍要回看原 PDF。[pypdf 文件](https://pypdf.readthedocs.io/en/stable/user/extract-text.html)也說明，PDF 本身沒有可靠的標題、段落與表格語意層。

掃描版 PDF 若沒有文字層，這個工具會要求先做 OCR。網頁如果要執行 JavaScript 才顯示正文，也不在目前這條路徑內。程式另設 100 MiB 的單檔安全上限；它是檔案大小限制，與模型 context 無關。

## 模型只在查到證據後出場

今天先把原始文件轉成可查詢的 raw Markdown；Qwen 還不直接讀取整份來源。Day 9 會先把文件切成帶來源位置的小段，建立可搜尋紀錄，再只把與問題相關的片段送進 Qwen3.8-27B。這樣才能把有限的 context 留給真正需要模型處理的內容。

今天留下的是一條由程式全程處理來源的入口：長文件留在檔案系統，模型只在後續取得少量相關證據時工作。

## 參考資料

- Day 7：第一週交付前，先讓本地聊天程式跑完一次驗收
- [source-to-raw-md 開源 Repository](https://github.com/gilbertytw-lab/source-to-raw-md)
- [pypdf：Extract Text from a PDF](https://pypdf.readthedocs.io/en/stable/user/extract-text.html)
