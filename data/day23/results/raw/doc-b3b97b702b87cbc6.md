---
document_id: "doc-b3b97b702b87cbc6"
source_name: "reference/command-line-tools-reference/feature-gates/VolumePVCDataSource.md"
source_type: "text"
source_format: "md"
source_sha256: "05a1e7e82e4dad461e161d87dbfddfbbb3c80fc028fe2a5c41af5c2b900de930"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/VolumePVCDataSource.md"
extracted_sha256: "05a1e7e82e4dad461e161d87dbfddfbbb3c80fc028fe2a5c41af5c2b900de930"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/VolumePVCDataSource.md"
---

---
# Removed from Kubernetes
title: VolumePVCDataSource
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.15"
    toVersion: "1.15"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.16"
    toVersion: "1.17"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.18"
    toVersion: "1.21"    

removed: true
---
Enable support for specifying an existing PVC as a DataSource.
