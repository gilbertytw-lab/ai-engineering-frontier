---
document_id: "doc-ed253f8b7f6fa4d6"
source_name: "reference/command-line-tools-reference/feature-gates/CSIMigrationOpenStack.md"
source_type: "text"
source_format: "md"
source_sha256: "8a11255ffb2f6e9d63e93bcc4262bb21b3dc2fcdb1d52d9368edea8bc0b092c5"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/CSIMigrationOpenStack.md"
extracted_sha256: "8a11255ffb2f6e9d63e93bcc4262bb21b3dc2fcdb1d52d9368edea8bc0b092c5"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/CSIMigrationOpenStack.md"
---

---
# Removed from Kubernetes
title: CSIMigrationOpenStack
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.14"
    toVersion: "1.17"  
  - stage: beta 
    defaultValue: true
    fromVersion: "1.18"
    toVersion: "1.23"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.24"
    toVersion: "1.25"    

removed: true
---
Enables shims and translation logic to route volume
operations from the Cinder in-tree plugin to Cinder CSI plugin. Supports
falling back to in-tree Cinder plugin for mount operations to nodes that have
the feature disabled or that do not have Cinder CSI plugin installed and
configured. Does not support falling back for provision operations, for those
the CSI plugin must be installed and configured. Requires CSIMigration
feature flag enabled.
