---
document_id: "doc-ef467b662e6d16dd"
source_name: "reference/command-line-tools-reference/feature-gates/DynamicVolumeProvisioning.md"
source_type: "text"
source_format: "md"
source_sha256: "3d6daee7ca38adeee9832b28af06522f47e10c460d1ada93b873e17ce755c574"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/DynamicVolumeProvisioning.md"
extracted_sha256: "3d6daee7ca38adeee9832b28af06522f47e10c460d1ada93b873e17ce755c574"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/DynamicVolumeProvisioning.md"
---

---
# Removed from Kubernetes
title: DynamicVolumeProvisioning
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: true
    fromVersion: "1.3"
    toVersion: "1.7"
  - stage: stable
    defaultValue: true
    fromVersion: "1.8"
    toVersion: "1.12"    

removed: true  
---
Enable the
[dynamic provisioning](/docs/concepts/storage/dynamic-provisioning/) of persistent volumes to Pods.
