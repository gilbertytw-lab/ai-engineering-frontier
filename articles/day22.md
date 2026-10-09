# AI Engineering 研究前線：30 天讀懂一週一週長出來的技術脈絡

## Day 22：從範例到實戰：準備 Kubernetes 文件

Day 21 回頭檢查了工具呼叫流程：模型提出操作，Python 驗證參數，再決定要不要執行。

今天改用 Kubernetes 官方文件準備下一批模型評估題。Kubernetes 是一套開源的容器編排平台，用來部署、擴縮和管理容器化應用程式；官方文件說明如何設定與使用這些功能。

我選這組文件，是因為它涵蓋多種主題和相近術語，適合檢查模型能否根據文件正確回答不同類型的問題。官方來源版本可以固定，每題也能回查原文位置。

原本的 `harbor-api` 是五份自行撰寫的虛構文件，問題都有明確答案，適合快速檢查索引和工具流程；但主題較少，無法充分檢驗模型面對內容更多、概念更廣的官方文件時，回答是否仍然正確。

[GitHub  Repo](https://github.com/gilbertytw-lab/ai-engineering-frontier)

## 先把「Kubernetes 文件」定義清楚

這次只取 Kubernetes 官方網站 `content/en/docs/` 裡的英文 Markdown，不含圖片或網站其他內容。截至 2026 年 10 月 5 日，官方版本頁列出的目前文件版本是 v1.37。我也固定了來源儲存庫的 commit，讓題目和答案能對回同一版文件。

這次鎖定的版本是 `kubernetes/website` commit `77db41e9c776b614fdb31de4cc6c8e9a70673817`。盤點這個目錄裡的 Markdown，共有 1,720 個檔案、16,198,192 位元組，約 15.45 MiB。這是原始 Markdown 的容量；文件尚未經過專案轉換、切塊（chunking）或建立搜尋索引。

官方來源儲存庫的 `LICENSE` 標示 Creative Commons Attribution 4.0 International（姓名標示 4.0 國際授權條款，CC BY 4.0）。題目會記下文件路徑和章節，答案則用自己的話整理。專案沒有複製 Kubernetes 文件全文。後續使用這批文件時，仍須保留來源與授權資訊。

## 準備十題固定題，下一步用來驗證模型回答

選好語料後，我先整理十道固定問題，作為後續評估模型回答的共同基準。題目涵蓋不同 Kubernetes 主題；每題都附上預期答案和官方文件章節，方便比對模型回答是否符合文件。完整題集放在 `data/benchmark.jsonl`。目前還沒用這些題目測試模型或評分。

## 今天完成語料與題集，模型評估留待後續

固定 commit 和檔案清單後，後續測試才能使用同一批材料。今天確認了官方來源和授權，盤點檔案數與原始容量，也整理出第一組模型評估題。這批文件尚未匯入 `knowledge/inbox/`、轉成 `knowledge/raw/` 或建立索引，Qwen 也還沒作答，因此目前沒有模型評估結果。

五份虛構文件仍留著，繼續當快速、可預期的開發檢查。接下來會批次匯入 Kubernetes 文件並建立索引，再用這十題評估模型回答是否正確、是否有文件依據。

## 來源

- [Kubernetes 官方文件版本](https://kubernetes.io/docs/home/supported-doc-versions/)
- [Kubernetes 文件原始碼快照](https://github.com/kubernetes/website/tree/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs)
- [該快照的授權檔](https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/LICENSE)
- [readiness probe 文件](https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/concepts/workloads/pods/probes.md)
- [ConfigMap 文件](https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/concepts/configuration/configmap.md)
- [Secret 文件](https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/concepts/configuration/secret.md)
