---
document_id: "doc-d9a0e6c9b4f288e7"
source_name: "reference/command-line-tools-reference/feature-gates/DynamicProvisioningScheduling.md"
source_type: "text"
source_format: "md"
source_sha256: "0a349a5c9700eecf232076226f6bc3e616a64c17bc32469a182d966a0e484a5e"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/DynamicProvisioningScheduling.md"
extracted_sha256: "0a349a5c9700eecf232076226f6bc3e616a64c17bc32469a182d966a0e484a5e"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/DynamicProvisioningScheduling.md"
---

---
# Removed from Kubernetes
title: DynamicProvisioningScheduling
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.11"
    toVersion: "1.11"
  - stage: deprecated
    fromVersion: "1.12"

removed: true  
---
Extend the default scheduler to be aware of
volume topology and handle PV provisioning.
This feature was superseded by the `VolumeScheduling` feature  in v1.12.
