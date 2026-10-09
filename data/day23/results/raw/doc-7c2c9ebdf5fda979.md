---
document_id: "doc-7c2c9ebdf5fda979"
source_name: "reference/command-line-tools-reference/feature-gates/NodeLogQuery.md"
source_type: "text"
source_format: "md"
source_sha256: "ff2830a0ed9571ffb3cf5c67b2eb3fa51f387f209ba1da15c6d7f0a96a901a0a"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/NodeLogQuery.md"
extracted_sha256: "ff2830a0ed9571ffb3cf5c67b2eb3fa51f387f209ba1da15c6d7f0a96a901a0a"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/NodeLogQuery.md"
---

---
title: NodeLogQuery
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.27"
    toVersion: "1.29"
  - stage: beta
    defaultValue: false
    fromVersion: "1.30"
    toVersion: "1.35"
  - stage: stable
    defaultValue: true
    fromVersion: "1.36"
---
Enables querying logs of node services using the `/logs` endpoint.
