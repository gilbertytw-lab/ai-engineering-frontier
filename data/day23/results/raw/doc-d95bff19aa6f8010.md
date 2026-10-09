---
document_id: "doc-d95bff19aa6f8010"
source_name: "reference/command-line-tools-reference/feature-gates/APIPriorityAndFairness.md"
source_type: "text"
source_format: "md"
source_sha256: "2ad54e705bcc5d882e2935e52ad93a25def9ac9ca42fbc9e2a69275faf582fe0"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/APIPriorityAndFairness.md"
extracted_sha256: "2ad54e705bcc5d882e2935e52ad93a25def9ac9ca42fbc9e2a69275faf582fe0"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/APIPriorityAndFairness.md"
---

---
title: APIPriorityAndFairness
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.18"
    toVersion: "1.19"
  - stage: beta
    defaultValue: true
    fromVersion: "1.20"
    toVersion: "1.28"
  - stage: stable
    defaultValue: true
    fromVersion: "1.29"
    toVersion: "1.30"

removed: true
---
Enable managing request concurrency with
prioritization and fairness at each server. (Renamed from `RequestManagement`)
