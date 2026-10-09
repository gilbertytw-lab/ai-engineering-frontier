---
document_id: "doc-6391ff3cec0da215"
source_name: "reference/command-line-tools-reference/feature-gates/CSIPersistentVolume.md"
source_type: "text"
source_format: "md"
source_sha256: "6772f2ec9c3df2fa09c6884d451866a9715acec32d4e0586701084f3579fe4b9"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/CSIPersistentVolume.md"
extracted_sha256: "6772f2ec9c3df2fa09c6884d451866a9715acec32d4e0586701084f3579fe4b9"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/CSIPersistentVolume.md"
---

---
# Removed from Kubernetes
title: CSIPersistentVolume
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.9"
    toVersion: "1.9"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.10"
    toVersion: "1.12"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.13"
    toVersion: "1.16"

removed: true  
---
Enable discovering and mounting volumes provisioned through a
[CSI (Container Storage Interface)](https://git.k8s.io/design-proposals-archive/storage/container-storage-interface.md)
compatible volume plugin.
