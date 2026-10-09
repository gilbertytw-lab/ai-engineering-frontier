---
document_id: "doc-cefed56c6de5a40d"
source_name: "reference/command-line-tools-reference/feature-gates/ConcurrentWatchObjectDecode.md"
source_type: "text"
source_format: "md"
source_sha256: "9f7ff6b6f57d1ca12b6df527211ef2635498f4f5e8b663cdc43a5543fc0ba159"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/ConcurrentWatchObjectDecode.md"
extracted_sha256: "9f7ff6b6f57d1ca12b6df527211ef2635498f4f5e8b663cdc43a5543fc0ba159"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/ConcurrentWatchObjectDecode.md"
---

---
title: ConcurrentWatchObjectDecode
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: false
    fromVersion: "1.31"
    toVersion: "1.36"
  - stage: beta
    defaultValue: true
    fromVersion: "1.37"

---
Enable concurrent watch object decoding. This is to avoid starving the API server's
watch cache when a conversion webhook is installed.
