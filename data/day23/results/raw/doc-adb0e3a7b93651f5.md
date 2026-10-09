---
document_id: "doc-adb0e3a7b93651f5"
source_name: "reference/command-line-tools-reference/feature-gates/RuntimeClass.md"
source_type: "text"
source_format: "md"
source_sha256: "efa13969b7959321b7f3c7d32bc30d9f7c9b64a81a4f7bd56146071b3dd4fae6"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/RuntimeClass.md"
extracted_sha256: "efa13969b7959321b7f3c7d32bc30d9f7c9b64a81a4f7bd56146071b3dd4fae6"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/RuntimeClass.md"
---

---
# Removed from Kubernetes
title: RuntimeClass
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.12"
    toVersion: "1.13"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.14"
    toVersion: "1.19"
  - stage: stable
    defaultValue: true
    fromVersion: "1.20"
    toVersion: "1.24"

removed: true
---
Enable the [RuntimeClass](/docs/concepts/containers/runtime-class/) feature for
selecting container runtime configurations.
