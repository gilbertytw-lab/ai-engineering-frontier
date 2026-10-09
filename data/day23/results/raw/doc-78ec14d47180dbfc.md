---
document_id: "doc-78ec14d47180dbfc"
source_name: "reference/command-line-tools-reference/feature-gates/ContainerCheckpoint.md"
source_type: "text"
source_format: "md"
source_sha256: "2d1dac33614cde88e10a3049a2f85e4fc4524c57ea20ee0d39fa4e6bed164544"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/ContainerCheckpoint.md"
extracted_sha256: "2d1dac33614cde88e10a3049a2f85e4fc4524c57ea20ee0d39fa4e6bed164544"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/ContainerCheckpoint.md"
---

---
title: ContainerCheckpoint
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.25"
    toVersion: "1.29"
  - stage: beta
    defaultValue: true
    fromVersion: "1.30"
---
Enables the kubelet `checkpoint` API.
See [Kubelet Checkpoint API](/docs/reference/node/kubelet-checkpoint-api/) for more details.
