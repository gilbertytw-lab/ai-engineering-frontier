---
document_id: "doc-04e634dae2f4ddf9"
source_name: "reference/command-line-tools-reference/feature-gates/ListFromCacheSnapshot.md"
source_type: "text"
source_format: "md"
source_sha256: "cdcd7a867e8944fb268cc95936ee61560883a257c35a9ab9ed4060786bde31ba"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/ListFromCacheSnapshot.md"
extracted_sha256: "cdcd7a867e8944fb268cc95936ee61560883a257c35a9ab9ed4060786bde31ba"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/ListFromCacheSnapshot.md"
---

---
title: ListFromCacheSnapshot
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.33"
    toVersion: "1.33"
  - stage: beta
    defaultValue: true
    fromVersion: "1.34"

--- 
Enables the API server to generate snapshots for the watch cache store and using them to serve LIST requests.
