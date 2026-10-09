---
document_id: "doc-a3ec00ab89bffb74"
source_name: "reference/command-line-tools-reference/feature-gates/ScheduleDaemonSetPods.md"
source_type: "text"
source_format: "md"
source_sha256: "c66d202cbd963ef7ee17a2b9ee4f9b40b5723d270ff5679e207d43b8171e37e5"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/ScheduleDaemonSetPods.md"
extracted_sha256: "c66d202cbd963ef7ee17a2b9ee4f9b40b5723d270ff5679e207d43b8171e37e5"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/ScheduleDaemonSetPods.md"
---

---
# Removed from Kubernetes
title: ScheduleDaemonSetPods
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.11"
    toVersion: "1.11"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.12"
    toVersion: "1.16"
  - stage: stable
    defaultValue: true
    fromVersion: "1.17"
    toVersion: "1.18"

removed: true
---
Enable DaemonSet Pods to be scheduled by the default scheduler instead
of the DaemonSet controller.
