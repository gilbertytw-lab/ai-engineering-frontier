---
document_id: "doc-646dadcdfa7c1ce5"
source_name: "reference/command-line-tools-reference/feature-gates/GracefulNodeShutdown.md"
source_type: "text"
source_format: "md"
source_sha256: "d45ef136115363d01519190b4cfa6e5121b0e758730a61f54f7e00589637feb0"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/GracefulNodeShutdown.md"
extracted_sha256: "d45ef136115363d01519190b4cfa6e5121b0e758730a61f54f7e00589637feb0"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/GracefulNodeShutdown.md"
---

---
title: GracefulNodeShutdown
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.20"
    toVersion: "1.20"
  - stage: beta
    defaultValue: true
    fromVersion: "1.21"
---
Enables support for graceful shutdown in kubelet.
During a system shutdown, kubelet will attempt to detect the shutdown event
and gracefully terminate pods running on the node. See
[Graceful Node Shutdown](/docs/concepts/architecture/nodes/#graceful-node-shutdown)
for more details.
