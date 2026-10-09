---
document_id: "doc-c94d44872b77eaba"
source_name: "reference/command-line-tools-reference/feature-gates/GangScheduling.md"
source_type: "text"
source_format: "md"
source_sha256: "ec4761c57d626b36326863284477bcbabdba72d7c830fde25079d022d88a1923"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/GangScheduling.md"
extracted_sha256: "ec4761c57d626b36326863284477bcbabdba72d7c830fde25079d022d88a1923"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/GangScheduling.md"
---

---
title: GangScheduling
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.35"
    toVersion: "1.36"

removed: true
---

Enables the GangScheduling plugin in kube-scheduler, which implements "all-or-nothing"
scheduling algorithm. The [Workload API](/docs/concepts/workloads/workload-api/) is used
to express the requirements.

This feature gate was removed in 1.37 and merged together with the `GenericWorkload` feature gate.
