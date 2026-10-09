# Day 22 語料盤點與起始題集

盤點日期：2026-10-05（Asia/Taipei）。

文章：[Day 22：五份範例文件夠測知識庫嗎？我把語料換成 Kubernetes 文件](../articles/day22.md)

## 語料範圍

- 來源：[`kubernetes/website`](https://github.com/kubernetes/website)，Kubernetes 官方網站與文件原始碼。
- 來源 commit：`77db41e9c776b614fdb31de4cc6c8e9a70673817`（當日 `main`）。
- 文件版本：官方版本頁當日列出的目前文件版本為 v1.37。
- 範圍：`content/en/docs/**/*.md`，只計英文 Markdown 文件。
- 檔案數：1,720。
- 原始位元組數：16,198,192 bytes（約 15.45 MiB）；不含圖片、網站建置產物或轉換後的文字。
- Git tree：`1be7bed35186d35a167f369e5bd9b565b1e211fd`（`content/en/docs`）。
- Markdown checksum：`f24ab9f07bf34806d5f2e703d0b283660693bda0ec0a49b32c31e8a1792a9413`。

Checksum 計算方式：按相對路徑排序所有 `.md` 檔案，對每一檔依序更新 SHA-256，內容依序為相對路徑 UTF-8 位元組長度（8-byte big-endian）、相對路徑、檔案位元組長度（8-byte big-endian）、檔案內容。這不是壓縮檔 checksum。

取得方式為 shallow clone `main`，再用 sparse checkout 取 `content/en/docs`；commit 和目錄 tree ID 會固定這次選到的內容。Kubernetes website 儲存庫的 `LICENSE` 是 CC BY 4.0。起始題的答案採轉述並保留來源路徑；沒有把原始 Markdown 全文複製進本專案。

## 起始題集

`data/benchmark.jsonl` 目前有 10 題，每題包含題目、預期答案和來源路徑／章節。這是人工整理的初始題集，不是完整 benchmark，也尚未由模型作答或評分。

| ID | 題目範圍 | 證據文件 |
|---|---|---|
| k8s-001 | `spec` 與 `status` | `concepts/overview/working-with-objects/_index.md` |
| k8s-002 | Deployment 更新 ReplicaSet | `concepts/workloads/controllers/deployment.md` |
| k8s-003 | Service selector 與 Pods | `concepts/services-networking/service.md` |
| k8s-004 | readiness probe 失敗的影響 | `concepts/workloads/pods/probes.md` |
| k8s-005 | ConfigMap、Secret 與 etcd 儲存限制 | `concepts/configuration/configmap.md`、`concepts/configuration/secret.md` |
| k8s-006 | StatefulSet 適用條件 | `concepts/workloads/controllers/statefulset.md` |
| k8s-007 | PersistentVolume 與 PersistentVolumeClaim | `concepts/storage/persistent-volumes.md` |
| k8s-008 | kube-scheduler 篩選與評分 | `concepts/scheduling-eviction/kube-scheduler.md` |
| k8s-009 | RBAC 最小權限 | `concepts/security/rbac-good-practices.md` |
| k8s-010 | startup probe 的作用 | `concepts/workloads/pods/probes.md` |

## 驗證邊界

本日量測的是來源 Markdown 的檔案數、位元組數和固定來源版本。沒有把語料放入 `knowledge/inbox/`、執行 converter、重建索引、呼叫 Qwen 或計算檢索與回答分數。因此這份記錄不能證明目前的知識庫已經能正確回答 Kubernetes 問題。
