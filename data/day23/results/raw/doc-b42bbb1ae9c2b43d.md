---
document_id: "doc-b42bbb1ae9c2b43d"
source_name: "reference/command-line-tools-reference/feature-gates/StorageNamespaceIndex.md"
source_type: "text"
source_format: "md"
source_sha256: "38a7694228da15aa4aee0fb3eb6ba489753454c3680b72e7abe7080fd3bf21cc"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/StorageNamespaceIndex.md"
extracted_sha256: "38a7694228da15aa4aee0fb3eb6ba489753454c3680b72e7abe7080fd3bf21cc"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/StorageNamespaceIndex.md"
---

---
title: StorageNamespaceIndex
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: beta 
    defaultValue: true
    fromVersion: "1.30"
    toVersion: "1.32"
  - stage: deprecated
    defaultValue: true
    fromVersion: "1.33"


---
Enables a namespace indexer for namespace scoped resources
in API server cache to accelerate list operations.
