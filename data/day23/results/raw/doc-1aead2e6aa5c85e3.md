---
document_id: "doc-1aead2e6aa5c85e3"
source_name: "reference/command-line-tools-reference/feature-gates/ServiceAccountTokenNodeBinding.md"
source_type: "text"
source_format: "md"
source_sha256: "667d7754d10437a047491e9072e089612812c99259596ccfa0b9d191038cab08"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/ServiceAccountTokenNodeBinding.md"
extracted_sha256: "667d7754d10437a047491e9072e089612812c99259596ccfa0b9d191038cab08"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/ServiceAccountTokenNodeBinding.md"
---

---
title: ServiceAccountTokenNodeBinding
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.29"
    toVersion: "1.30"
  - stage: beta
    defaultValue: true
    fromVersion: "1.31"
    toVersion: "1.32"
  - stage: stable
    defaultValue: true
    locked: true
    fromVersion: "1.33"
---
Controls whether the API server allows binding service account tokens to Node objects.
