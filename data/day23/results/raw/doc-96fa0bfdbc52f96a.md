---
document_id: "doc-96fa0bfdbc52f96a"
source_name: "reference/command-line-tools-reference/feature-gates/CSRDuration.md"
source_type: "text"
source_format: "md"
source_sha256: "96120f8c1bbdb0a8d26ba26247b8b35e227a7bac47c9d259400efbc9982f19bb"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/CSRDuration.md"
extracted_sha256: "96120f8c1bbdb0a8d26ba26247b8b35e227a7bac47c9d259400efbc9982f19bb"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/CSRDuration.md"
---

---
# Removed from Kubernetes
title: CSRDuration
content_type: feature_gate

_build:
  list: never
  render: false

stages:
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
Allows clients to request a duration for certificates issued
via the Kubernetes CSR API.
