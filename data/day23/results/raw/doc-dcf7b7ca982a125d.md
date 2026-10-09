---
document_id: "doc-dcf7b7ca982a125d"
source_name: "reference/command-line-tools-reference/feature-gates/GenericWorkload.md"
source_type: "text"
source_format: "md"
source_sha256: "797fe3e715f33baf084ca88011129ca11cd41af7fa708f1970cf1e74f2ed1a56"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/GenericWorkload.md"
extracted_sha256: "797fe3e715f33baf084ca88011129ca11cd41af7fa708f1970cf1e74f2ed1a56"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/GenericWorkload.md"
---

---
title: GenericWorkload
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.35"
    toVersion: "1.36"
  - stage: beta
    defaultValue: false
    fromVersion: "1.37"
---

Enables support for the [Workload API](/docs/concepts/workloads/workload-api/) and [PodGroup API](/docs/concepts/workloads/podgroup-api/) to express scheduling requirements at the workload level.

When enabled, Pods can reference a specific PodGroup to influence the way that they are scheduled. Starting in Kubernetes v1.37, this feature gate also encompasses [gang scheduling](/docs/concepts/scheduling-eviction/gang-scheduling/), and [workload-aware preemption](/docs/concepts/scheduling-eviction/workload-aware-preemption/).
