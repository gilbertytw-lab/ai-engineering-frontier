---
document_id: "doc-eec29d64ff42a2e9"
source_name: "reference/command-line-tools-reference/feature-gates/EndpointSliceNodeName.md"
source_type: "text"
source_format: "md"
source_sha256: "dbbaaa38428e6f317b46f9ceee57cf7e99f8cb1dd97cfc2640fcfc68113a220a"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/EndpointSliceNodeName.md"
extracted_sha256: "dbbaaa38428e6f317b46f9ceee57cf7e99f8cb1dd97cfc2640fcfc68113a220a"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/EndpointSliceNodeName.md"
---

---
# Removed from Kubernetes
title: EndpointSliceNodeName
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.20"
    toVersion: "1.20"
  - stage: stable
    defaultValue: true
    fromVersion: "1.21"
    toVersion: "1.24"    

removed: true  
---
Enables EndpointSlice `nodeName` field.
