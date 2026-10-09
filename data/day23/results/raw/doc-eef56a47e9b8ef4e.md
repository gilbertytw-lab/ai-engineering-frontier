---
document_id: "doc-eef56a47e9b8ef4e"
source_name: "reference/command-line-tools-reference/feature-gates/IngressClassNamespacedParams.md"
source_type: "text"
source_format: "md"
source_sha256: "9c2323a8708d1aa022242f535d3219221e260eb13cb67d01a57ee1ceff940ed2"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/IngressClassNamespacedParams.md"
extracted_sha256: "9c2323a8708d1aa022242f535d3219221e260eb13cb67d01a57ee1ceff940ed2"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/IngressClassNamespacedParams.md"
---

---
# Removed from Kubernetes
title: IngressClassNamespacedParams
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.21"
    toVersion: "1.21"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.22"
    toVersion: "1.22"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.23"
    toVersion: "1.24"    

removed: true
---
Allow namespace-scoped parameters reference in
`IngressClass` resource. This feature adds two fields - `Scope` and `Namespace`
to `IngressClass.spec.parameters`.
