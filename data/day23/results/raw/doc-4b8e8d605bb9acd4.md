---
document_id: "doc-4b8e8d605bb9acd4"
source_name: "reference/command-line-tools-reference/feature-gates/StatefulSetRecreateStrategy.md"
source_type: "text"
source_format: "md"
source_sha256: "b923bf42f98f9e4efd0dce881f33afa7c9a6c113a7c4dbce34f6276186b772a1"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/StatefulSetRecreateStrategy.md"
extracted_sha256: "b923bf42f98f9e4efd0dce881f33afa7c9a6c113a7c4dbce34f6276186b772a1"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/StatefulSetRecreateStrategy.md"
---

---
title: StatefulSetRecreateStrategy
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.37"
---
Enables the `Recreate` update strategy for StatefulSets, which deletes all of a
StatefulSet's Pods before creating new Pods that reflect modifications made to the
StatefulSet's `.spec.template`. See
[Recreate](/docs/concepts/workloads/controllers/statefulset/#recreate) for details.
