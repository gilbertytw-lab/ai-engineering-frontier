---
document_id: "doc-fc8168b7e456f2bf"
source_name: "reference/command-line-tools-reference/feature-gates/ResourceLimitsPriorityFunction.md"
source_type: "text"
source_format: "md"
source_sha256: "3c1752a5a4882d9d0deda976708ed4ddced18f0f38d592921cee53a7ceca2d3c"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/ResourceLimitsPriorityFunction.md"
extracted_sha256: "3c1752a5a4882d9d0deda976708ed4ddced18f0f38d592921cee53a7ceca2d3c"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/ResourceLimitsPriorityFunction.md"
---

---
# Removed from Kubernetes
title: ResourceLimitsPriorityFunction
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.9"
    toVersion: "1.18"
  - stage: deprecated
    fromVersion: "1.19"
    toVersion: "1.19"

removed: true
---
Enable a scheduler priority function that
assigns a lowest possible score of 1 to a node that satisfies at least one of
the input Pod's cpu and memory limits. The intent is to break ties between
nodes with same scores.
