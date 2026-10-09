---
document_id: "doc-15d1d2bdedc9a444"
source_name: "reference/command-line-tools-reference/feature-gates/StaleControllerConsistencyReplicaSet.md"
source_type: "text"
source_format: "md"
source_sha256: "3c88b9fa6fcbb224ee5beba1de73fa6fd7f1384dbb94c599ec8e427b1ec2f3a7"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/StaleControllerConsistencyReplicaSet.md"
extracted_sha256: "3c88b9fa6fcbb224ee5beba1de73fa6fd7f1384dbb94c599ec8e427b1ec2f3a7"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/StaleControllerConsistencyReplicaSet.md"
---

---
title: StaleControllerConsistencyReplicaSet
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true  
    fromVersion: "1.36"
---
Enables behavior within the ReplicaSet controller to ensure that prior writes to
the API server are observed before proceeding with additional reconciliation for the same ReplicaSet.
This is to prevent stale cache from causing incorrect or spurious updates to the ReplicaSet.
