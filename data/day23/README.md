# Day 23 Kubernetes 語料

本目錄保存鐵人賽 Day 23 使用的固定版本語料與匯入結果，讀者 clone 專案後即可使用。

- 上游來源：[Kubernetes website](https://github.com/kubernetes/website)，commit `77db41e9c776b614fdb31de4cc6c8e9a70673817`
- 範圍：`source/content/en/docs/**/*.md`，共 1,720 份 Markdown
- 原始容量：16,198,192 bytes（約 15.45 MiB）
- 語料 checksum：`f24ab9f07bf34806d5f2e703d0b283660693bda0ec0a49b32c31e8a1792a9413`
- 授權：Kubernetes 文件依隨附的 [LICENSE](source/LICENSE) 採 CC BY 4.0
- 歸屬：Kubernetes website contributors；原文連結以固定 commit 為準

`source/` 保存上游 Markdown；`results/raw/` 保存轉換器輸出的 Markdown 與來源欄位，`source_snapshot` 指向 repo 內的相對路徑；`results/reports/` 保存三輪逐檔報告和最終審核。報告中的本機絕對路徑欄位已移除，其他逐檔結果與量測值保留。1,720 份 raw 已用專案的 validator 對這份語料逐份核對通過。

原始完整工作區與 Day 8 的測試備份集中放在專案內的 `data/local-workspaces/`，並由 `.gitignore` 排除。這些資料包含第三方 PDF、網頁快照與回復用副本，不是 GitHub 發布素材；Day 23 可重用的語料和 raw 則保存在本目錄。
