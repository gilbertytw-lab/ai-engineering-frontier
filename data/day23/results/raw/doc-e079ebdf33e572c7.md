---
document_id: "doc-e079ebdf33e572c7"
source_name: "reference/command-line-tools-reference/feature-gates/PodHasNetworkCondition.md"
source_type: "text"
source_format: "md"
source_sha256: "0ceb33d038d712d85a0d157a3ea92d6b3c68919aab7d3b9719bd278eb806d45e"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/PodHasNetworkCondition.md"
extracted_sha256: "0ceb33d038d712d85a0d157a3ea92d6b3c68919aab7d3b9719bd278eb806d45e"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/PodHasNetworkCondition.md"
---

---
title: PodHasNetworkCondition
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.25"
    toVersion: "1.27"

removed: true
---
Enable the kubelet to mark the [PodHasNetwork](/docs/concepts/workloads/pods/pod-lifecycle/#pod-has-network)
condition on pods. This was renamed to `PodReadyToStartContainersCondition` in 1.28.
