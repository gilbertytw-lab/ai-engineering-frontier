---
document_id: "doc-b55fce424b3aa2aa"
source_name: "reference/command-line-tools-reference/feature-gates/NominatedNodeNameForExpectation.md"
source_type: "text"
source_format: "md"
source_sha256: "ad7af55bfb055ac338cdc3e1f9bf8f2e977b37680c58f2f7fd8a610e4a7abc08"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/NominatedNodeNameForExpectation.md"
extracted_sha256: "ad7af55bfb055ac338cdc3e1f9bf8f2e977b37680c58f2f7fd8a610e4a7abc08"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/NominatedNodeNameForExpectation.md"
---

---
title: NominatedNodeNameForExpectation
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.34"
    toVersion: "1.34"
  - stage: beta
    defaultValue: true
    fromVersion: "1.35"

---
When enabled, kube-scheduler uses `.status.nominatedNodeName` to express where a
Pod is going to be bound. The `.status.nominatedNodeName` field is set when kube-scheduler
triggers preemption of pods, or anticipates that WaitOnPermit or PreBinding phase will take
relatively long.
Other components may read and use `.status.nominatedNodeName`, but should not set it.

When disabled, kube-scheduler will only set `.status.nominatedNodeName` before triggering preemption.
