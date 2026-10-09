---
document_id: "doc-c5fd3012e2b0e60b"
source_name: "reference/command-line-tools-reference/feature-gates/HugepageAwareEviction.md"
source_type: "text"
source_format: "md"
source_sha256: "82f4f052d16acee0bd045959170aa66ac455c7dca6e2cfda2dfc57497bfc1e05"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/HugepageAwareEviction.md"
extracted_sha256: "82f4f052d16acee0bd045959170aa66ac455c7dca6e2cfda2dfc57497bfc1e05"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/HugepageAwareEviction.md"
---

---
title: HugepageAwareEviction
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.37"
---
Subtracts hugepage capacity from `memory.available` so the kubelet's eviction
signal reflects actual regular-memory availability. Without this gate, hugepage
reservations inflate `AvailableBytes`, delaying eviction and causing OOM kills
on nodes with hugepages configured.
