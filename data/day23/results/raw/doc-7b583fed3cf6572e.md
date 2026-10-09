---
document_id: "doc-7b583fed3cf6572e"
source_name: "reference/command-line-tools-reference/feature-gates/ServiceIPStaticSubrange.md"
source_type: "text"
source_format: "md"
source_sha256: "8f4c5fea0bcc1b4fab61e8ea5716b9142cbec116b9c904327f5c74c929bafa95"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/ServiceIPStaticSubrange.md"
extracted_sha256: "8f4c5fea0bcc1b4fab61e8ea5716b9142cbec116b9c904327f5c74c929bafa95"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/ServiceIPStaticSubrange.md"
---

---
title: ServiceIPStaticSubrange
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.24"
    toVersion: "1.24"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.25"
    toVersion: "1.25"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.26"
    toVersion: "1.27"    

removed: true  
---
Enables a strategy for Services ClusterIP allocations, whereby the
ClusterIP range is subdivided. Dynamic allocated ClusterIP addresses will be allocated preferently
from the upper range allowing users to assign static ClusterIPs from the lower range with a low
risk of collision. See
[Avoiding collisions](/docs/reference/networking/virtual-ips/#avoiding-collisions)
for more details.
