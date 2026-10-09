---
document_id: "doc-c260aedd7453cc0c"
source_name: "reference/command-line-tools-reference/feature-gates/EndpointSlice.md"
source_type: "text"
source_format: "md"
source_sha256: "fe7abe8d0316e145a8090712283497bdbc3cfcc216c08a5dd678bf6dd1a912e6"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/EndpointSlice.md"
extracted_sha256: "fe7abe8d0316e145a8090712283497bdbc3cfcc216c08a5dd678bf6dd1a912e6"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/EndpointSlice.md"
---

---
# Removed from Kubernetes
title: EndpointSlice
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.16"
    toVersion: "1.16"
  - stage: beta 
    defaultValue: false
    fromVersion: "1.17"
    toVersion: "1.17"    
  - stage: beta 
    defaultValue: true
    fromVersion: "1.18"
    toVersion: "1.20"      
  - stage: stable
    defaultValue: true
    fromVersion: "1.21"
    toVersion: "1.24"    

removed: true  
---
Enables EndpointSlices for more scalable and extensible
 network endpoints. See [Enabling EndpointSlices](/docs/concepts/services-networking/endpoint-slices/).
