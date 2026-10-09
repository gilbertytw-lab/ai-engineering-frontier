---
document_id: "doc-d61ecd2aa9f1decc"
source_name: "reference/command-line-tools-reference/feature-gates/AllowServiceLBStatusOnNonLB.md"
source_type: "text"
source_format: "md"
source_sha256: "6819573caab7ea1c3deb5896affeecce5aef54724eb807ed40add04007da3c13"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/AllowServiceLBStatusOnNonLB.md"
extracted_sha256: "6819573caab7ea1c3deb5896affeecce5aef54724eb807ed40add04007da3c13"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/AllowServiceLBStatusOnNonLB.md"
---

---
title: AllowServiceLBStatusOnNonLB
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: deprecated
    defaultValue: false
    fromVersion: "1.29"    
    toVersion: "1.34"

removed: true
---
Enables `.status.ingress.loadBalancer` to be set on Services of types other than `LoadBalancer`.
