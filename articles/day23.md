# AI Engineering 研究前線：30 天讀懂一週一週長出來的技術脈絡

## Day 23：用大量文件匯入來做壓力測試

Day 22 固定了 Kubernetes 官方英文文件的來源版本，也整理出十道模型評估題。今天我把這批 1,720 份 Markdown 送進 Day 8 的轉換流程，確認原文能不能保存、轉成附有來源資訊的 raw 文件。

第一輪有 1,719 份通過。一份失敗。

查到最後，問題不在文件內容，而在讀檔時換行字元被轉換了。

[GitHub Repo](https://github.com/gilbertytw-lab/ai-engineering-frontier)

## 先固定資料來源與檔案身分

語料固定在 Kubernetes website commit `77db41e9c776b614fdb31de4cc6c8e9a70673817`，範圍是 `content/en/docs/**/*.md`。這批 Markdown 共 1,720 份、16,198,192 bytes，約 15.45 MiB；checksum 是 `f24ab9f07bf34806d5f2e703d0b283660693bda0ec0a49b32c31e8a1792a9413`。

同一批文件裡有 178 個檔案都叫 `_index.md`。只記檔名會失去章節資訊，所以每份文件的 `source_name` 使用 `content/en/docs/` 底下的相對路徑，`source_url` 則帶上固定 commit。這樣即使兩份文件同名、內容相同，仍可回到各自的來源位置。文件 ID 也由來源網址和原始內容計算。

匯入器會把來源欄位附在 raw 文件前面：

```json
{
  "source_name": "concepts/configuration/configmap.md",
  "source_url": "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/concepts/configuration/configmap.md",
  "charset": "utf-8"
}
```

原始 Markdown、轉換後的 1,720 份 raw 和逐檔報告都放在專案的 [`data/day23/`](../data/day23/README.md)，clone 後可以直接下載使用。語料依隨附的 Kubernetes `LICENSE` 採 CC BY 4.0。

每份 raw 的 `source_snapshot` 也指向 repo 內的相對路徑；下載後能在本機找到原始 Markdown，不會連到匯入時使用的絕對路徑。

## 用專案內的固定語料重跑

以下命令從 Repository 根目錄執行。它直接讀取專案附帶的語料，輸出寫進專案內的 `data/day23/reproduction/`：

```bash
corpus_source="$PWD/data/day23/source/content/en/docs"
corpus_workspace="$PWD/data/day23/reproduction"

uv run python knowledge/import_corpus.py \
  --source-dir "$corpus_source" \
  --workspace-root "$corpus_workspace" \
  --source-base-url "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs" \
  --expected-checksum f24ab9f07bf34806d5f2e703d0b283660693bda0ec0a49b32c31e8a1792a9413
```

checksum 不符時，程式會在寫入工作區前停止，避免把不同版本的 Kubernetes 文件混在同一批結果裡。完整來源與原始量測報告見 [`data/day23/`](../data/day23/README.md) 和[驗證紀錄](../docs/day23-verification.md)。

## 一份文件讓驗證失敗

第一次執行花了 2.046 秒：

```text
完成：1719 份新轉換，0 份沿用，1 份失敗。
成功率：99.94%；耗時：2.046 秒。
```

這次時間包含本機 checksum 核對、原檔與來源中繼資料準備、轉換和逐檔驗證，不含 Git 下載與報告寫檔。量測環境是 Apple M5、32 GiB 記憶體；這是單次結果。

失敗文件是 `contribute/generate-ref-docs/metrics-reference.md`，錯誤訊息是「Markdown 正文與來源抽取結果不一致」。原檔使用 CRLF（`\r\n`）。轉換器解碼原始位元組後保留 CRLF，但驗證器以預設文字模式讀取 raw 時，Python 會自動把 CRLF 轉成 LF（`\n`）。兩邊的正文因此不同，驗證就停在這一份。先前五份 `harbor-api` 範例沒有 CRLF，沒遇到這個狀況。

修正方式是在驗證器和轉換器讀取既有 raw 時，要求 Python 保留原換行：

```python
with path.open(encoding="utf-8", newline="") as stream:
    raw = stream.read()
```

原始文件位元組沒有更動。我也補了測試，涵蓋首次匯入、沿用既有結果，以及重新處理 raw 時的 CRLF 情況。

## 修正後的重跑，先看轉換，再看沿用

| 執行 | 新轉換 | 沿用並驗證 | 失敗 | 耗時 |
|---|---:|---:|---:|---:|
| 第一輪 | 1,719 | 0 | 1 | 2.046 秒 |
| 修正後重跑 | 1 | 1,719 | 0 | 0.426 秒 |
| 再跑一次 | 0 | 1,720 | 0 | 0.397 秒 |

修正後重跑只重新轉換原先失敗的文件，其餘 1,719 份核對後沿用。第三次執行則沿用並驗證全部 1,720 份，沒有新增 raw。後兩輪主要花在檢查已存在的結果，不能拿來當成空工作區首次匯入的速度。

最終比對確認：保存的 1,720 份原檔都與來源位元組相同，1,720 份 raw 全數通過來源欄位、hash 和正文驗證，待處理區沒有剩餘檔案。raw 共 17,515,305 bytes，約 16.70 MiB。來源欄位會增加檔案容量，因此原始語料和 raw 分開記錄。

## 全數匯入，還不代表文件內容完整

這裡的成功率只代表原檔已保存，raw 也通過轉換器驗證。它能確認文件可追溯到來源；不代表網站每個畫面上的內容都已匯入，更不代表模型已答對問題。這批資料目前還沒有切塊、建立搜尋索引或產生模型答案。

Kubernetes Markdown 裡還有網站建置時使用的 Hugo shortcode。抽查 ConfigMap 和 metrics 文件時，`glossary_definition`、`include` 等標記原樣留在 raw，轉換器沒有展開。被 shortcode 引入的定義、段落或圖片不一定在這批 Markdown 裡。1,720 份都通過匯入，不能推論網站上所有內容都已收齊。

這次批次匯入補出了五份範例沒碰到的 CRLF 情況。每份 raw 也都留有來源位置，後續檢查可以回查固定版本的原文。

## 來源

- [Kubernetes 文件原始碼快照](https://github.com/kubernetes/website/tree/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs)
- [發生 CRLF 驗證失敗的 metrics 文件](https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/contribute/generate-ref-docs/metrics-reference.md)
- [ConfigMap 文件原始碼](https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/concepts/configuration/configmap.md)
- [固定快照的授權檔（CC BY 4.0）](https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/LICENSE)
