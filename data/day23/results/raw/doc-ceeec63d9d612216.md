---
document_id: "doc-ceeec63d9d612216"
source_name: "reference/command-line-tools-reference/feature-gates/JobSuccessPolicy.md"
source_type: "text"
source_format: "md"
source_sha256: "155c4be2a5ab94d8523a1634575d205adc84a8a4f2683d66a1b3aa0b053a08cc"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/JobSuccessPolicy.md"
extracted_sha256: "155c4be2a5ab94d8523a1634575d205adc84a8a4f2683d66a1b3aa0b053a08cc"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/JobSuccessPolicy.md"
---

---
title: JobSuccessPolicy
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.30"
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
Allow users to specify when a Job can be declared as succeeded based on the set of succeeded pods.
