---
document_id: "doc-cfe8fa24efbb0a43"
source_name: "reference/command-line-tools-reference/feature-gates/CustomResourcePublishOpenAPI.md"
source_type: "text"
source_format: "md"
source_sha256: "bfacc38f3f0414e9117ff1f2274afc0e52f363abd575a2a83b7161b802583f19"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/CustomResourcePublishOpenAPI.md"
extracted_sha256: "bfacc38f3f0414e9117ff1f2274afc0e52f363abd575a2a83b7161b802583f19"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/CustomResourcePublishOpenAPI.md"
---

---
# Removed from Kubernetes
title: CustomResourcePublishOpenAPI
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.14"
    toVersion: "1.14"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.15"
    toVersion: "1.15"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.16"
    toVersion: "1.18"

removed: true  
---
Enables publishing of CRD OpenAPI specs.
