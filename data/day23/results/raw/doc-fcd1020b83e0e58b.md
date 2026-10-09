---
document_id: "doc-fcd1020b83e0e58b"
source_name: "reference/command-line-tools-reference/feature-gates/ResilientWatchCacheInitialization.md"
source_type: "text"
source_format: "md"
source_sha256: "bd7b78f4743ccb761626936486c35d4842d8d6b730600f70555c013a54c16439"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/ResilientWatchCacheInitialization.md"
extracted_sha256: "bd7b78f4743ccb761626936486c35d4842d8d6b730600f70555c013a54c16439"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/ResilientWatchCacheInitialization.md"
---

---
title: ResilientWatchCacheInitialization
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: beta 
    defaultValue: true
    fromVersion: "1.31"
    toVersion: "1.33"
  - stage: stable
    locked: true
    defaultValue: true
    fromVersion: "1.34"

---
Enables resilient watchcache initialization to avoid controlplane overload.
