---
document_id: "doc-f2c68b4f7633bbde"
source_name: "reference/command-line-tools-reference/feature-gates/ServiceLoadBalancerFinalizer.md"
source_type: "text"
source_format: "md"
source_sha256: "b4002644fb2af7132b4c6aa73cdce4c161ce56269e61a8493bc2623862cfcd63"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/ServiceLoadBalancerFinalizer.md"
extracted_sha256: "b4002644fb2af7132b4c6aa73cdce4c161ce56269e61a8493bc2623862cfcd63"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/ServiceLoadBalancerFinalizer.md"
---

---
# Removed from Kubernetes
title: ServiceLoadBalancerFinalizer
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.15"
    toVersion: "1.15"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.16"
    toVersion: "1.16"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.17"
    toVersion: "1.20"    

removed: true
---
Enable finalizer protection for Service load balancers.
