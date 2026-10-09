---
document_id: "doc-d59d4a75e2c26f9f"
source_name: "reference/command-line-tools-reference/feature-gates/BtreeWatchCache.md"
source_type: "text"
source_format: "md"
source_sha256: "09a2e1fad9a7d0218214db35c9ce0e72d20f76777ae36081b59d914dfb5ef151"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/BtreeWatchCache.md"
extracted_sha256: "09a2e1fad9a7d0218214db35c9ce0e72d20f76777ae36081b59d914dfb5ef151"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/BtreeWatchCache.md"
---

---
title: BtreeWatchCache
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: beta 
    defaultValue: true
    fromVersion: "1.32"
    toVersion: "1.32"
  - stage: stable
    defaultValue: true
    locked: true
    fromVersion: "1.33"

---
When enabled, the API server will replace the legacy HashMap-based _watch cache_
with a BTree-based implementation. This replacement may bring performance improvements.
