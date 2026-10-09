---
document_id: "doc-b0f0eee736dfd25b"
source_name: "reference/command-line-tools-reference/feature-gates/NativeHistograms.md"
source_type: "text"
source_format: "md"
source_sha256: "94aab5a084e8c3856f3da39742c98c0ef7937c293e3ea936074ed5485ab6c436"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/NativeHistograms.md"
extracted_sha256: "94aab5a084e8c3856f3da39742c98c0ef7937c293e3ea936074ed5485ab6c436"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/NativeHistograms.md"
---

---
title: NativeHistograms
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.36"
    toVersion: "1.36"
  - stage: beta
    defaultValue: true
    fromVersion: "1.37"
---
Enables Kubernetes components to expose metrics in Prometheus Native Histogram format for improved efficiency and finer bucket resolution.
See [Native Histograms](/docs/reference/instrumentation/native-histograms/) for more information.
