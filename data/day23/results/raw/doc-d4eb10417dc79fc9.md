---
document_id: "doc-d4eb10417dc79fc9"
source_name: "reference/command-line-tools-reference/feature-gates/UserNamespacesStatelessPodsSupport.md"
source_type: "text"
source_format: "md"
source_sha256: "40e38bd6a4ec9eb3da769abd7db13f1b6e34b1d30f94f9cd711f460fa5fdb024"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/UserNamespacesStatelessPodsSupport.md"
extracted_sha256: "40e38bd6a4ec9eb3da769abd7db13f1b6e34b1d30f94f9cd711f460fa5fdb024"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/UserNamespacesStatelessPodsSupport.md"
---

---
title: UserNamespacesStatelessPodsSupport
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.25"
    toVersion: "1.27"

removed: true
---
Enable user namespace support for stateless Pods. This feature gate was superseded
by the `UserNamespacesSupport` feature gate in the Kubernetes v1.28 release.
