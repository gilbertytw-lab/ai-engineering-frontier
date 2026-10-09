---
document_id: "doc-2d1cb5586b7b8ef2"
source_name: "reference/command-line-tools-reference/feature-gates/IndexedJob.md"
source_type: "text"
source_format: "md"
source_sha256: "2f39aeb6eab303b2f24eb62ba05d988de8590dbfbbf7c3cd00c54cc0402a51e0"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/IndexedJob.md"
extracted_sha256: "2f39aeb6eab303b2f24eb62ba05d988de8590dbfbbf7c3cd00c54cc0402a51e0"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/IndexedJob.md"
---

---
# Removed from Kubernetes
title: IndexedJob
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
    toVersion: "1.23"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.24"
    toVersion: "1.25"    

removed: true
---
Allows the [Job](/docs/concepts/workloads/controllers/job/)
controller to manage Pod completions per completion index.
