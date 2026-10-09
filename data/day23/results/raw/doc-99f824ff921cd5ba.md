---
document_id: "doc-99f824ff921cd5ba"
source_name: "reference/command-line-tools-reference/feature-gates/CPUManager.md"
source_type: "text"
source_format: "md"
source_sha256: "8572608eba2c7a65a6eb6aad702b4b89806f5937c33ba9884f17e53f60eff4e2"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/CPUManager.md"
extracted_sha256: "8572608eba2c7a65a6eb6aad702b4b89806f5937c33ba9884f17e53f60eff4e2"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/CPUManager.md"
---

---
title: CPUManager
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.8"
    toVersion: "1.9"
  - stage: beta
    defaultValue: true
    fromVersion: "1.10"  
    toVersion: "1.25" 
  - stage: stable
    defaultValue: true
    fromVersion: "1.26"  
    toVersion: "1.32"

removed: true
---
Enable container level CPU affinity support, see
[CPU Management Policies](/docs/tasks/administer-cluster/cpu-management-policies/).
