---
document_id: "doc-e47f236bfe6bef05"
source_name: "reference/command-line-tools-reference/feature-gates/NodeDeclaredFeatures.md"
source_type: "text"
source_format: "md"
source_sha256: "b762cdbf2fb3d36f7bfdce634aed6e56eaa2bd90205a1cf06f5529a6c655a42f"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/NodeDeclaredFeatures.md"
extracted_sha256: "b762cdbf2fb3d36f7bfdce634aed6e56eaa2bd90205a1cf06f5529a6c655a42f"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/NodeDeclaredFeatures.md"
---

---
title: NodeDeclaredFeatures
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.35"
    toVersion: "1.35"
  - stage: beta
    defaultValue: true
    fromVersion: "1.36"
    toVersion: "1.36"
  - stage: stable
    defaultValue: true
    locked: true
    fromVersion: "1.37"
---
Enables Nodes to report supported features via their `.status`. This enables the
scheduler and admission controller to prevent operations on nodes lacking features
required by the Pod. See [Node Declared Features](/docs/concepts/scheduling-eviction/node-declared-features/).
