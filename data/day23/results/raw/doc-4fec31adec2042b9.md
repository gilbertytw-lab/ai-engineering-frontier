---
document_id: "doc-4fec31adec2042b9"
source_name: "reference/command-line-tools-reference/feature-gates/SeparateCacheWatchRPC.md"
source_type: "text"
source_format: "md"
source_sha256: "323277fee88983d3799fdaa0e6cc8aa43289729f5285c957aa0d3f48d16f5812"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/SeparateCacheWatchRPC.md"
extracted_sha256: "323277fee88983d3799fdaa0e6cc8aa43289729f5285c957aa0d3f48d16f5812"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/SeparateCacheWatchRPC.md"
---

---
title: SeparateCacheWatchRPC
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.28"
    toVersion: "1.32"
  - stage: deprecated
    defaultValue: false
    fromVersion: "1.33"

---
Allows the API server watch cache to create a watch on a dedicated RPC.
This prevents watch cache from being starved by other watches.
