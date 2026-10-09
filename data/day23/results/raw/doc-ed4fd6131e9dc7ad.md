---
document_id: "doc-ed4fd6131e9dc7ad"
source_name: "reference/command-line-tools-reference/feature-gates/Accelerators.md"
source_type: "text"
source_format: "md"
source_sha256: "89601c11a67feaec6857bc9d6dfdd0e1809c45e57ecccbc264c08f346eeb8407"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/Accelerators.md"
extracted_sha256: "89601c11a67feaec6857bc9d6dfdd0e1809c45e57ecccbc264c08f346eeb8407"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/Accelerators.md"
---

---
title: Accelerators
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.6"
    toVersion: "1.10"
  - stage: deprecated
    fromVersion: "1.11"
    toVersion: "1.11"

removed: true
---
Provided an early form of plugin to enable Nvidia GPU support when using
Docker Engine; no longer available. See
[Device Plugins](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/) for
an alternative.
