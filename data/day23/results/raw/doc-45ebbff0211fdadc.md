---
document_id: "doc-45ebbff0211fdadc"
source_name: "reference/command-line-tools-reference/feature-gates/ServiceLBNodePortControl.md"
source_type: "text"
source_format: "md"
source_sha256: "1e740b72be437d176b07ac68edddd72b4187c7a94b9df7229076e3b942eff401"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/ServiceLBNodePortControl.md"
extracted_sha256: "1e740b72be437d176b07ac68edddd72b4187c7a94b9df7229076e3b942eff401"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/ServiceLBNodePortControl.md"
---

---
# Removed from Kubernetes
title: ServiceLBNodePortControl
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.20"
    toVersion: "1.21"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.22"
    toVersion: "1.23"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.24"
    toVersion: "1.25"    

removed: true
---
Enables the `allocateLoadBalancerNodePorts` field on Services.
