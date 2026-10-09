---
document_id: "doc-8debd91a9cf4e9c5"
source_name: "reference/command-line-tools-reference/feature-gates/BalanceAttachedNodeVolumes.md"
source_type: "text"
source_format: "md"
source_sha256: "6997f914bb55435acc3d1b2a52abab01f2e0d211f6bcbbfe30ba99c82be59bcb"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/BalanceAttachedNodeVolumes.md"
extracted_sha256: "6997f914bb55435acc3d1b2a52abab01f2e0d211f6bcbbfe30ba99c82be59bcb"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/BalanceAttachedNodeVolumes.md"
---

---
# Removed from Kubernetes
title: BalanceAttachedNodeVolumes
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.11"
    toVersion: "1.21"
  - stage: deprecated
    defaultValue: false
    fromVersion: "1.22"
    toVersion: "1.22"

removed: true
---
Include volume count on node to be considered for
balanced resource allocation while scheduling. A node which has closer CPU,
memory utilization, and volume count is favored by the scheduler while making decisions.
