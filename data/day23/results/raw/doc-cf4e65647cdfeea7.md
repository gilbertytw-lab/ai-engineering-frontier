---
document_id: "doc-cf4e65647cdfeea7"
source_name: "reference/command-line-tools-reference/feature-gates/HugePages.md"
source_type: "text"
source_format: "md"
source_sha256: "4f2f6da016359bc4f9a2bbc84b0360e1aabe65328b736b7d279f9b9b224b609b"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/HugePages.md"
extracted_sha256: "4f2f6da016359bc4f9a2bbc84b0360e1aabe65328b736b7d279f9b9b224b609b"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/HugePages.md"
---

---
# Removed from Kubernetes
title: HugePages
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
    toVersion: "1.13"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.14"
    toVersion: "1.16"    

removed: true  
---
Enable the allocation and consumption of pre-allocated
[huge pages](/docs/tasks/manage-hugepages/scheduling-hugepages/).
