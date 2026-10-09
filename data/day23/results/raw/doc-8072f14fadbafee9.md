---
document_id: "doc-8072f14fadbafee9"
source_name: "reference/command-line-tools-reference/feature-gates/CSIDriverRegistry.md"
source_type: "text"
source_format: "md"
source_sha256: "f6c0c85259ef04ae65dcb6258554296c135faca9379adf2d1544014febd6c65d"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/CSIDriverRegistry.md"
extracted_sha256: "f6c0c85259ef04ae65dcb6258554296c135faca9379adf2d1544014febd6c65d"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/CSIDriverRegistry.md"
---

---
# Removed from Kubernetes
title: CSIDriverRegistry
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
    toVersion: "1.17"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.18"
    toVersion: "1.21"    

removed: true
---
Enable all logic related to the CSIDriver API object in
`csi.storage.k8s.io`.
