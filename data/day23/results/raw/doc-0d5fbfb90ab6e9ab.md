---
document_id: "doc-0d5fbfb90ab6e9ab"
source_name: "reference/command-line-tools-reference/feature-gates/CSIMigration.md"
source_type: "text"
source_format: "md"
source_sha256: "a08e132ad17c7b7a62261390cd6d31165a8ed58bb96f328b3b778e359fb23b65"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/CSIMigration.md"
extracted_sha256: "a08e132ad17c7b7a62261390cd6d31165a8ed58bb96f328b3b778e359fb23b65"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/CSIMigration.md"
---

---
# Removed from Kubernetes
title: CSIMigration
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.14"
    toVersion: "1.16"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.17"
    toVersion: "1.24"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.25"
    toVersion: "1.26"    

removed: true
---
Enables shims and translation logic to route volume
operations from in-tree plugins to corresponding pre-installed CSI plugins
