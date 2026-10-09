---
document_id: "doc-88b29cddc627a01e"
source_name: "reference/command-line-tools-reference/feature-gates/APIResponseCompression.md"
source_type: "text"
source_format: "md"
source_sha256: "7fca2a8402c5dd10ea6dcc0de2fca1943d8a2c92fcf5edd7a9bbc1a484ad30de"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/APIResponseCompression.md"
extracted_sha256: "7fca2a8402c5dd10ea6dcc0de2fca1943d8a2c92fcf5edd7a9bbc1a484ad30de"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/APIResponseCompression.md"
---

---
title: APIResponseCompression
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: "alpha" 
    defaultValue: false
    fromVersion: "1.7"
    toVersion: "1.15"
  - stage: beta
    defaultValue: true
    fromVersion: "1.16"
---
Compress the API responses for `LIST` or `GET` requests.
