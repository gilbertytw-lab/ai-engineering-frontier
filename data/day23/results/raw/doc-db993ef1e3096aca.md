---
document_id: "doc-db993ef1e3096aca"
source_name: "reference/command-line-tools-reference/feature-gates/KubeProxyDrainingTerminatingNodes.md"
source_type: "text"
source_format: "md"
source_sha256: "8bddddd7b98616b5fc7de7534f0ddcb0f24f5424a6396e8281210d6a4793b586"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/KubeProxyDrainingTerminatingNodes.md"
extracted_sha256: "8bddddd7b98616b5fc7de7534f0ddcb0f24f5424a6396e8281210d6a4793b586"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/KubeProxyDrainingTerminatingNodes.md"
---

---
title: KubeProxyDrainingTerminatingNodes
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.28"
    toVersion: "1.30"
  - stage: beta
    defaultValue: true
    fromVersion: "1.30"
    toVersion: "1.30"
  - stage: stable
    defaultValue: true
    fromVersion: "1.31"
    toVersion: "1.32"

removed: true
---
Implement connection draining for
terminating nodes for `externalTrafficPolicy: Cluster` services.
