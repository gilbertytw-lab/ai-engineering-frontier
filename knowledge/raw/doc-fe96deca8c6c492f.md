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

# Harbor API Specification

## `POST /v1/jobs`

這個 endpoint 建立一筆非同步工作。

### Request body

```json
{
  "job_type": "reindex",
  "source": "knowledge/raw"
}
```

`job_type` 目前只接受 `reindex` 和 `health-check`。`source` 必須是服務允許讀取的資料來源名稱，不接受任意檔案系統路徑。

### Successful response

成功時回傳 HTTP 202，body 包含 `job_id`、`status` 和 `created_at`。新工作初始狀態是 `queued`。

### Error responses

- HTTP 400：request body 缺少欄位，或欄位值不在允許清單中。
- HTTP 409：相同 `job_type` 已有一筆 `queued` 或 `running` 的工作。
- HTTP 503：queue service 暫時無法接受新工作。

## `GET /v1/jobs/{job_id}`

查詢工作狀態時，成功回傳 HTTP 200。`status` 可能是 `queued`、`running`、`succeeded` 或 `failed`。找不到 `job_id` 時回傳 HTTP 404。
