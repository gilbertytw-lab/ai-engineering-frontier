# Day 8 驗證與編輯紀錄

查證日期：2026-09-22（Asia/Taipei）。本文只記錄實際完成的來源轉換；原始第三方論文和文章全文不進參賽 Repo。

## 轉換路徑與變更原因

第一版 skill 讓本地 Qwen3.8-27B 逐字整理來源。五份自撰 `harbor-api` 文件可轉，但三份隨機完整 PDF 論文都在模型呼叫前超過 5 MiB／12,000 字限制。Day 5～7 三篇網頁可轉，但各花約五到九分鐘。使用者要求完整來源才有意義，且不再做單頁樣本，因此轉換器改為純程式版 0.3.0，移除本地模型 API、`--model`、`--max-input-chars` 等參數。Qwen3.8-27B 保留給後續有檢索證據的問答。

目前 `source-to-raw-md` 接受 UTF-8 文字／Markdown、有文字層的 PDF、靜態 HTML 與 HTTP/HTTPS 網址。它保留原件或網頁快照於 `inbox/`，將完整抽取結果與固定來源欄位寫入 `raw/`。PDF 每頁都有標記；任何頁面抽不出文字就報錯。100 MiB 單檔上限是程式安全限制，與模型 context 無關。五份自撰文件已用新版轉換器重新產生；前版輸出已在遷移備份中保留。

Day 8 的讀者入口另設 [`knowledge/convert.py`](../knowledge/convert.py)。它掃描 `knowledge/inbox/` 的待處理檔案，逐份轉換並核對；成功後把原檔移到 `knowledge/inbox/processed/`，同時更新 `raw/` 的來源快照路徑。失敗或格式不支援的檔案留在待處理區。重跑時不掃 `processed/`，也不需要 Qwen 的工具呼叫介面。五份專案示範原檔已按此流程移入 `processed/`；再次執行顯示待處理區沒有來源檔，五份 raw 仍通過驗證。

## 三份隨機完整 PDF

從 `/Users/gilbert/Miracle/raw/papers` 的五份完整論文候選中，以 `random.Random(20260922).sample(sorted(papers), 3)` 取三份，唯讀測試。來源路徑與雜湊見本機 `day08-real-source-test/test-manifest.json`。三份來源與轉換結果只保存在 `/Users/gilbert/Data/ai-engineering-frontier/workspaces/day08-programmatic-migration/`。

| PDF | 頁數 | 抽取字元 | 轉換耗時 | 逐頁核對 |
| --- | ---: | ---: | ---: | --- |
| `Design_Trends_in_Smart_Gate_Driver_ICs_for_Power_GaN_HEMTs.pdf` | 4 | 19,671 | 0.36 秒 | 4/4 與 `pypdf` 抽字一致 |
| `A_Smart_Gate_Driver_IC_for_GaN_Power_HEMTs_With_Dynamic_Ringing_Suppression.pdf` | 14 | 60,286 | 3.19 秒 | 14/14 一致 |
| `doi-10.35848 High threshold voltage normally-off AlGaN_GaN MIS-HEMT.pdf` | 8 | 39,100 | 0.58 秒 | 8/8 一致 |

比對方法：重新以 `pypdf` 抽取原 PDF 每頁文字，對照輸出中對應的 `## 第 n 頁` 內容，前後空白去除後字串完全相同。這證明轉換器沒有把已抽出的文字截斷、漏頁或改寫，**不能**證明 PDF 文字層就是所有可見內容。三份論文有雙欄、圖、表、公式；閱讀順序與視覺資訊仍需回看 PDF。空白文字層的 PDF（例如掃描檔）目前拒絕，尚無 OCR。

另外以 ReportLab 產生非論文的兩頁帳單 `invoice-sample.pdf`：第一頁含帳單編號、日期、服務與總額，第二頁含付款期限與聯絡方式。程式輸出兩個頁碼標記與全部欄位，並通過 `validate.py`。檔案保存在本機 `day08-generic-pdf-check/` 工作區；這證明轉換器不要求論文標題、摘要或章節格式，但 PDF 文字層與圖表限制仍在。

再把上述三份完整 PDF 與 Day 5～7 的三份 HTML 快照放入本機 `day08-batch-real-test/knowledge/inbox/`，從 `knowledge/convert.py` 的批次入口重跑。結果為六份成功、零份失敗；六份原檔進入 `processed/`，六份 raw 保持可驗證。第二次執行顯示待處理區沒有來源檔。

## 三篇公開網頁

直接以網址測試 [Day 5](https://ithelp.ithome.com.tw/articles/10413625)、[Day 6](https://ithelp.ithome.com.tw/articles/10414325)、[Day 7](https://ithelp.ithome.com.tw/articles/10414659)。最新程式版三次各約 0.23～0.27 秒。輸出分別有 12、26、16 個程式碼圍欄標記，文章標題、段落、連結與末尾內容可見，沒有網站導覽混入；HTML 快照保存在本機工作區。這些數字是單機單次量測，不保證每個網站或網路環境都一樣快。其他網站使用通用 HTML 抽取，可能混入導覽；JavaScript 動態內容未測且不保證。

## 驗證命令

```bash
python3 /Users/gilbert/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/source-to-raw-md
uv run --with pypdf python -m unittest discover -s skills/source-to-raw-md/tests -v
uv run --with pypdf --with fonttools python knowledge/convert.py
uv run --with pypdf --with fonttools python skills/source-to-raw-md/scripts/validate.py knowledge/raw
uv run python -m unittest discover -s tests -v
uv run --with pypdf python -m py_compile skills/source-to-raw-md/scripts/convert.py
git diff --check
```

新版測試涵蓋超過舊 12,000 字上限的文字全文、HTML 正文／程式碼／導覽過濾、兩頁 PDF 順序，以及空白文字層拒絕。以上為程式測試；論文逐頁核對與真實網頁測試另行執行，不把短 mock 當成全文證據。

批次入口測試另驗證：多份待處理檔案一次轉換、成功原檔移入 `processed/`、重跑不重轉、格式不支援的檔案保留在待處理區，以及損壞 PDF 失敗後原檔留在待處理區。

`validate.py` 定義 Day 8 的 raw 契約：`doc-...md` 檔名、YAML frontmatter 中的固定來源欄位、非空正文，以及 PDF 的頁數與抽取範圍。它由保存的原件重新計算 SHA-256、Document ID 和完整 Markdown 正文，並核對輸出。五份專案示範檔、三份完整論文、三篇網頁與兩頁帳單，共 12 份均通過。測試另加入一份故意改掉結尾的 raw，驗證器會拒絕。這項驗證保證目前轉換器與原件的一致性；Day 9 的 ingest 尚未實作，不能宣稱已通過下游讀取。

## 保留與發布

轉換器舊版、五份舊 raw、舊文章與計畫，保存在 `/Users/gilbert/Data/ai-engineering-frontier/workspaces/day08-programmatic-migration/pre-change/`，可用來回復。第三方 PDF 與網頁快照均不放在參賽 Repo。[`source-to-raw-md` 獨立 Repository](https://github.com/gilbertytw-lab/source-to-raw-md) 已於本日發布，`main` commit 為 `a6b9e4a27902b294996e2d918b7e1a52222382fc`；本參賽 Repo 的 Day 8 修改尚未 commit 或 push。
