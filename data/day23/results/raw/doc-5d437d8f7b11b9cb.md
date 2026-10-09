---
document_id: "doc-5d437d8f7b11b9cb"
source_name: "reference/command-line-tools-reference/feature-gates/ServerSideApply.md"
source_type: "text"
source_format: "md"
source_sha256: "f8732e08fcab1060f57ffb533c519810ef6943ca2250d5982092c12b0fe41b0c"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/ServerSideApply.md"
extracted_sha256: "f8732e08fcab1060f57ffb533c519810ef6943ca2250d5982092c12b0fe41b0c"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/ServerSideApply.md"
---

---
title: ServerSideApply
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.14"
    toVersion: "1.15"
  - stage: beta
    defaultValue: true
    fromVersion: "1.16"  
    toVersion: "1.21" 
  - stage: stable
    defaultValue: true
    fromVersion: "1.22"  
    toVersion: "1.31"

removed: true
---
Enables the [Sever Side Apply (SSA)](/docs/reference/using-api/server-side-apply/)
feature on the API Server.
