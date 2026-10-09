---
document_id: "doc-f24308cfa8d1aae3"
source_name: "reference/command-line-tools-reference/feature-gates/DRADeviceTaints.md"
source_type: "text"
source_format: "md"
source_sha256: "3474bd88fd83fc8a2c713aa85b59a09018a3d57dd962d4543fad078c2550516b"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/DRADeviceTaints.md"
extracted_sha256: "3474bd88fd83fc8a2c713aa85b59a09018a3d57dd962d4543fad078c2550516b"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/DRADeviceTaints.md"
---

---
title: DRADeviceTaints
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.33"
    toVersion: "1.35"
  - stage: beta
    defaultValue: true
    fromVersion: "1.36"
    toVersion: "1.37"
  - stage: stable
    defaultValue: true
    locked: true
    fromVersion: "1.37"
---
Enables support for
[tainting devices and selectively tolerating those taints](/docs/concepts/resource-management/dynamic-resource-allocation/device-taints/#device-taints-and-tolerations)
when using dynamic resource allocation to manage devices.
