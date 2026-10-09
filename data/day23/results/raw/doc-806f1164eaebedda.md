---
document_id: "doc-806f1164eaebedda"
source_name: "reference/command-line-tools-reference/feature-gates/TTLAfterFinished.md"
source_type: "text"
source_format: "md"
source_sha256: "5f9bdd96824d3d01e2ca62dacbe0f893336902a5f15c77539163ff73136e5ea9"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/TTLAfterFinished.md"
extracted_sha256: "5f9bdd96824d3d01e2ca62dacbe0f893336902a5f15c77539163ff73136e5ea9"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/TTLAfterFinished.md"
---

---
# Removed from Kubernetes
title: TTLAfterFinished
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.12"
    toVersion: "1.20"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.21"
    toVersion: "1.22"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.23"
    toVersion: "1.24"    

removed: true
---
Allow a [TTL controller](/docs/concepts/workloads/controllers/ttlafterfinished/)
to clean up resources after they finish execution.
