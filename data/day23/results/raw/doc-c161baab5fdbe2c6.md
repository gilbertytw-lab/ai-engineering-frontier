---
document_id: "doc-c161baab5fdbe2c6"
source_name: "reference/command-line-tools-reference/feature-gates/DRADeviceTaintRules.md"
source_type: "text"
source_format: "md"
source_sha256: "8de4a519a05e65b846c93c8ce8cf485de6edb6f2d7bc51575e9876fbf0807618"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/DRADeviceTaintRules.md"
extracted_sha256: "8de4a519a05e65b846c93c8ce8cf485de6edb6f2d7bc51575e9876fbf0807618"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/DRADeviceTaintRules.md"
---

---
title: DRADeviceTaintRules
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.35"
    toVersion: "1.35"
  - stage: beta
    defaultValue: false
    fromVersion: "1.36"
    toVersion: "1.37"
  - stage: stable
    defaultValue: true
    locked: true
    fromVersion: "1.37"
---
Enables support for
[tainting devices through DeviceTaintRule objects](/docs/concepts/resource-management/dynamic-resource-allocation/device-taints/#device-taints-and-tolerations)
when using dynamic resource allocation to manage devices.

This feature gate has no effect unless you also enable the `DRADeviceTaints` feature gate.
