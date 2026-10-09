# Day 23 Kubernetes 批次匯入與 CRLF 修正

驗證日期：2026-10-07（Asia/Taipei）。

文章：[Day 23：大量文件匯得進來嗎？1,720 份 Kubernetes 文件的匯入紀錄](../articles/day23.md)。小型數據摘要：[data/day23-import-summary.json](../data/day23-import-summary.json)。

## 固定來源與環境

- 來源：[Kubernetes website](https://github.com/kubernetes/website)。
- 固定 commit：`77db41e9c776b614fdb31de4cc6c8e9a70673817`，沿用 Day 22。
- 範圍：`content/en/docs/**/*.md`，1,720 份、16,198,192 bytes（15.45 MiB）。
- checksum：`f24ab9f07bf34806d5f2e703d0b283660693bda0ec0a49b32c31e8a1792a9413`。算法沿用 [Day 22 紀錄](day22-verification.md)。
- 授權：固定快照 `LICENSE` 標示 CC BY 4.0。
- 硬體：Apple M5，32 GiB 記憶體；Python 3.13.15。
- 轉換器：專案內的 `source-to-raw-md` 0.3.0；本次修正只處理讀取時的換行轉換，未更動輸出格式或 document ID 算法。

重新取得固定 commit 後，檔案數、總 bytes 和 checksum 都與 Day 22 相同。此次不引用上游當日 main 的內容。文件中有 178 個 `_index.md`；來源中繼資料以完整相對路徑命名，URL 包含固定 commit。每份原件和 `.source.json` 一起由既有 batch converter 保存。

## 程式變更

`knowledge/import_corpus.py` 在 checksum 通過後，逐份準備 inbox 原件和 sidecar，呼叫既有 `batch.convert_selected_source()`。成功原件移入 `processed/corpus/`；失敗保留在 inbox，每筆結果包含相對路徑、來源大小、SHA-256、狀態、raw 路徑或錯誤及耗時。

重跑時，已保存的原件和 sidecar 必須符合本次輸入，raw 仍須通過 `validate_file()`，才記為 `reused`。已保存資料或 raw 被改動時會報錯，不覆蓋它們。checksum 不符、空語料或來源與輸出互相包含時，整批在寫入前停止。

`success_rate = (converted + reused) / source_files`。首次執行的成功代表完成轉換並驗證；重跑的成功也包含核對後沿用。`raw_files` 和 `raw_bytes` 只計本次通過驗證的文件，失敗過程可能留下的 raw 不算成功。

## 真實失敗與修正

首輪只失敗一份：`contribute/generate-ref-docs/metrics-reference.md`，2,694 bytes，SHA-256 `a51d1ba19a88fb9eb542e1bb5ee2ac65eb6412476350ce62c6d81f6a62bf7af7`。錯誤是「Markdown 正文與來源抽取結果不一致」。整批只有這份文件含有 CRLF，共 90 個 `\r\n`。

轉換器由原始 bytes 解碼後保留內文的 CRLF；`validate_file()` 原本用 `Path.read_text()` 讀 raw，會將 CRLF 轉成 LF，導致整段正文比較失敗。`convert()` 讀取既有輸出的分支也有同樣問題。

兩處都改用 `Path.open(encoding="utf-8", newline="")` 讀取，不做 universal-newline translation。保存的來源 bytes 不變，正文抽取規則也不變。修正後原先失敗的文件可重新處理；其餘 1,719 份沿用並驗證。

## 執行結果

| 執行 | 新轉換 | 沿用 | 失敗 | 成功率 | 耗時 |
|---|---:|---:|---:|---:|---:|
| 首輪，修正前 | 1,719 | 0 | 1 | 99.94186% | 2.045584 秒 |
| 修正後補轉 | 1 | 1,719 | 0 | 100% | 0.425505 秒 |
| 再跑一次 | 0 | 1,720 | 0 | 100% | 0.396911 秒 |

表格的耗時以各輪原始報告為準，精確浮點值保存在數據摘要。時間涵蓋本地 checksum、原件與 sidecar 準備、轉換／沿用核對，不包含 Git 下載與報告寫檔，也不包含切塊、索引或模型請求。首輪是修正前的整批轉換；後兩輪主要是既有資料驗證，不能拿來宣稱從空工作區轉換整批的效能。這是單機單次紀錄，沒有量測峰值記憶體。

最終審核：1,720 份 processed 原件逐一與固定來源 bytes 完全相同；1,720 份 raw 重新通過全部 frontmatter、hash、document ID 和正文驗證；1,720 份皆有來源 URL；待處理區 0 份檔案。raw 合計 17,515,305 bytes（16.70 MiB）。原有 `harbor-api` 的 inbox、raw 和 index 沒有變更。

抽查 ConfigMap、probes 和 metrics 文件的開頭、中間、結尾，程式碼圍欄、原始 frontmatter、連結和 shortcode 均保留。這項驗證核對轉換器與原始 Markdown 的一致性，沒有驗證網站建置後內容；`glossary_definition`、`include` 等 Hugo shortcode 未展開，圖片與被引入的其他檔案也未匯入。

## Repository 資料與重跑

Day 23 的輸入與輸出已放進 Repository，讀者 clone 後可直接使用：

- 固定來源：[`data/day23/source/content/en/docs/`](../data/day23/source/content/en/docs/)，1,720 份 Markdown。
- 授權原件：[`data/day23/source/LICENSE`](../data/day23/source/LICENSE)，CC BY 4.0。
- 驗證後 raw：[`data/day23/results/raw/`](../data/day23/results/raw/)，1,720 份；其中 `source_snapshot` 已改為 repo 相對路徑。
- 原始報告、修正後報告、重跑報告與最終 audit：[`data/day23/results/reports/`](../data/day23/results/reports/)。發布版報告移除了機器專屬的絕對路徑欄位，保留逐檔狀態、雜湊和量測值。

最初量測使用的完整工作區也搬進 `data/local-workspaces/ai-engineering-frontier/workspaces/day23-kubernetes-import-2026-10-07/` 留存；這個目錄含重複的 staging 副本，由 `.gitignore` 排除。公開資料包只放讀者可下載使用的來源 Markdown、raw 與報告。

以下命令從 Repository 根目錄執行，直接使用專案附帶的語料；重跑工作區留在專案內的 `data/day23/reproduction/`：

```bash
corpus_source="$PWD/data/day23/source/content/en/docs"
corpus_workspace="$PWD/data/day23/reproduction"

uv run python knowledge/import_corpus.py \
  --source-dir "$corpus_source" \
  --workspace-root "$corpus_workspace" \
  --source-base-url "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs" \
  --expected-checksum f24ab9f07bf34806d5f2e703d0b283660693bda0ec0a49b32c31e8a1792a9413
```

這份輸入與原量測來源逐檔比對，1,720 個相對路徑和 SHA-256 都相同。固定來源、授權與 checksum 也記在 [`data/day23/README.md`](../data/day23/README.md)。

封裝後重新執行 raw validator，1,720 份都能透過相對 `source_snapshot` 找到 repo 內的原檔並通過正文與 hash 核對：

```bash
uv run python skills/source-to-raw-md/scripts/validate.py \
  data/day23/results/raw --root "$PWD"
```

同日也用文章中的命令，從 `data/day23/source/content/en/docs/` 在全新的 `data/day23/reproduction/` 工作區重跑：1,720 份新轉換、0 份失敗，耗時 2.088 秒；接著逐份驗證，1,720 份全數通過。這次確認匯入器寫出的 `source_snapshot` 以該工作區為相對根目錄。`data/day23/reproduction/` 是本機重跑輸出，不納入 GitHub；可下載的原始結果在 `data/day23/results/`。

## 程式測試與完成邊界

```bash
uv run --with pypdf python -m unittest discover -s tests -v
uv run --with pypdf python -m unittest discover -s skills/source-to-raw-md/tests -v
git diff --check
```

全專案 85 個測試通過，converter 的 5 個測試通過。新增的 9 個匯入測試涵蓋相同檔名與內容的不同路徑、重跑不重寫 raw、CRLF 首次轉換和既有輸出分支、錯誤 UTF-8 留在待處理區且其他文件繼續、checksum 不符、保存原件被修改、raw 被竄改、重疊目錄與空語料。

本日完成到 raw，沒有執行這批文件的 chunking、FTS5 建置、Qwen 作答或十題評分。成功率只代表這批英文 Markdown 的保存與轉換驗證，不能代表網站完整度或答案品質。Git commit、push 與發文未執行。
