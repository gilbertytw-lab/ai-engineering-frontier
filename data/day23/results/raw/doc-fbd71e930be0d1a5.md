---
document_id: "doc-fbd71e930be0d1a5"
source_name: "reference/command-line-tools-reference/feature-gates/CustomPodDNS.md"
source_type: "text"
source_format: "md"
source_sha256: "33949f9899eb4c9cb58bb1520732313c36976a6d61a27ca80ec989ae0db84cff"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/CustomPodDNS.md"
extracted_sha256: "33949f9899eb4c9cb58bb1520732313c36976a6d61a27ca80ec989ae0db84cff"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/CustomPodDNS.md"
---

---
# Removed from Kubernetes
title: CustomPodDNS
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.9"
    toVersion: "1.9"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.10"
    toVersion: "1.13"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.14"
    toVersion: "1.16"

removed: true  
---
Enable customizing the DNS settings for a Pod using its `dnsConfig` property.
Check [Pod's DNS Config](/docs/concepts/services-networking/dns-pod-service/#pod-dns-config)
for more details.
