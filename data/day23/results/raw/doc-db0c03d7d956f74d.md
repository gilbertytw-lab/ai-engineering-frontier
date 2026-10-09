---
document_id: "doc-db0c03d7d956f74d"
source_name: "reference/command-line-tools-reference/feature-gates/PreventStaticPodAPIReferences.md"
source_type: "text"
source_format: "md"
source_sha256: "6b1179e8b6a5bc33e3cc98f64b3b9236c88a6733ede19886cbf572f12e7e999f"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/PreventStaticPodAPIReferences.md"
extracted_sha256: "6b1179e8b6a5bc33e3cc98f64b3b9236c88a6733ede19886cbf572f12e7e999f"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/PreventStaticPodAPIReferences.md"
---

---
title: PreventStaticPodAPIReferences
content_type: feature_gate

_build:
  list: never
  render: false

stages:
- stage: beta
  defaultValue: true
  fromVersion: "1.34"

---
Denies Pod admission if static Pods reference other API objects.
