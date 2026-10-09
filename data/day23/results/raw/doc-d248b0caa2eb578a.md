---
document_id: "doc-d248b0caa2eb578a"
source_name: "reference/command-line-tools-reference/feature-gates/NonPreemptingPriority.md"
source_type: "text"
source_format: "md"
source_sha256: "8af76e8a6b915dfabdcc4477f7c682ec508966e0cd4b5a898b2527022a6d2e7c"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/NonPreemptingPriority.md"
extracted_sha256: "8af76e8a6b915dfabdcc4477f7c682ec508966e0cd4b5a898b2527022a6d2e7c"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/NonPreemptingPriority.md"
---

---
# Removed from Kubernetes
title: NonPreemptingPriority
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.15"
    toVersion: "1.18"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.19"
    toVersion: "1.23"
  - stage: stable
    defaultValue: true
    fromVersion: "1.24"
    toVersion: "1.25"

removed: true
---
Enable `preemptionPolicy` field for PriorityClass and Pod.
