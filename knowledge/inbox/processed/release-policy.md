# Harbor API Release Policy

## Normal release window

一般 release window 是每週二與週四 14:00–16:00 UTC。每次 production release 都需要一位 release owner 和一位 reviewer 在 release record 中確認。

## Required checks

release owner 必須確認：

- CI 已通過，且 release ID 與 image tag 相同。
- staging 的 `/healthz`、`/readyz` 和建立測試工作都成功。
- production canary 已觀察滿 15 分鐘。
- release record 已填入 rollback 目標。

## Emergency release

修復正在影響 production 的 incident 時，可以跳過一般 release window，但仍然需要 reviewer、incident ID 和 rollback 目標。事後要在下一個工作日補齊 release record。

## Out of scope

這份 policy 沒有定義 log retention、個別客戶的資料保留期限，或第三方 queue service 的 SLA。需要這些資訊時，必須查找對應的正式文件。
