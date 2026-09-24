# Harbor API Service Configuration

## Staging defaults

| Key | Value | Purpose |
| --- | --- | --- |
| `HARBOR_ENV` | `staging` | 選擇 staging 的依賴與限制 |
| `HARBOR_MAX_RETRIES` | `3` | 單筆工作最多重試次數 |
| `HARBOR_WORKER_COUNT` | `2` | staging 預設 worker 數量 |
| `HARBOR_CONFIG_REV` | `2026-09-17` | 設定檔版本 |

## Production defaults

| Key | Value | Purpose |
| --- | --- | --- |
| `HARBOR_ENV` | `production` | 選擇 production 的依賴與限制 |
| `HARBOR_MAX_RETRIES` | `5` | 單筆工作最多重試次數 |
| `HARBOR_WORKER_COUNT` | `8` | production 預設 worker 數量 |
| `HARBOR_CONFIG_REV` | `2026-09-17` | 設定檔版本 |

## Change rule

修改 production default 前，需要一筆 release record 和一位 reviewer 的核准。設定檔不保存任何 token、密碼或其他秘密值；秘密由部署環境在啟動時注入。
