---
document_id: "doc-a8fca4c221b923a0"
source_name: "reference/command-line-tools-reference/feature-gates/PodPriority.md"
source_type: "text"
source_format: "md"
source_sha256: "06554efc628349c45abec2e66fb0673233f4535d454cbe04690cf69453bd9c11"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/PodPriority.md"
extracted_sha256: "06554efc628349c45abec2e66fb0673233f4535d454cbe04690cf69453bd9c11"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/PodPriority.md"
---

---
# Removed from Kubernetes
title: PodPriority
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.8"
    toVersion: "1.10"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.11"
    toVersion: "1.13"
  - stage: stable
    defaultValue: true
    fromVersion: "1.14"
    toVersion: "1.18"

removed: true
---
Enable the descheduling and preemption of Pods based on their
[priorities](/docs/concepts/scheduling-eviction/pod-priority-preemption/).
