---
document_id: "doc-b4d68c0fd900bb06"
source_name: "reference/command-line-tools-reference/feature-gates/ServiceAppProtocol.md"
source_type: "text"
source_format: "md"
source_sha256: "ba8a1cac7596baa10af3a574c04bb88a277860937bf2530de8d46e9f4361a3d6"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/ServiceAppProtocol.md"
extracted_sha256: "ba8a1cac7596baa10af3a574c04bb88a277860937bf2530de8d46e9f4361a3d6"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/ServiceAppProtocol.md"
---

---
# Removed from Kubernetes
title: ServiceAppProtocol
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.18"
    toVersion: "1.18"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.19"
    toVersion: "1.19"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.20"
    toVersion: "1.22"    

removed: true
---
Enables the `appProtocol` field on Services and Endpoints.
