---
document_id: "doc-6771eefba55f182f"
source_name: "reference/command-line-tools-reference/feature-gates/SetHostnameAsFQDN.md"
source_type: "text"
source_format: "md"
source_sha256: "a7064c450466ea52fab358c359ce2d0a8ed5838fec74a9fff89bb620c3b29539"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/SetHostnameAsFQDN.md"
extracted_sha256: "a7064c450466ea52fab358c359ce2d0a8ed5838fec74a9fff89bb620c3b29539"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/SetHostnameAsFQDN.md"
---

---
# Removed from Kubernetes
title: SetHostnameAsFQDN
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.19"
    toVersion: "1.19"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.20"
    toVersion: "1.21"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.22"
    toVersion: "1.24"    

removed: true
---
Enable the ability of setting Fully Qualified Domain Name(FQDN) as the
hostname of a pod. See
[Pod's `setHostnameAsFQDN` field](/docs/concepts/services-networking/dns-pod-service/#pod-sethostnameasfqdn-field).
