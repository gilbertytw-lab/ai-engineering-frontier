---
document_id: "doc-f07e03f63caa2e23"
source_name: "reference/command-line-tools-reference/feature-gates/DevicePlugins.md"
source_type: "text"
source_format: "md"
source_sha256: "22003de9788f197a15b19ca52a6963c6d95d39c9aaba992b4c58bdc00d3e8d3c"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/DevicePlugins.md"
extracted_sha256: "22003de9788f197a15b19ca52a6963c6d95d39c9aaba992b4c58bdc00d3e8d3c"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/DevicePlugins.md"
---

---
title: DevicePlugins
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.8"
    toVersion: "1.9"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.10"
    toVersion: "1.25"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.26"
    toVersion: "1.27"    

removed: true  
---
Enable the [device-plugins](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/)
based resource provisioning on nodes.
