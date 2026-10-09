---
document_id: "doc-57eeadaa91f2aa76"
source_name: "reference/command-line-tools-reference/feature-gates/NetworkPolicyEndPort.md"
source_type: "text"
source_format: "md"
source_sha256: "0105c6b89f680933df8dd699db5c2be4cfd4406e4644a0763001de89f1b34ee9"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/NetworkPolicyEndPort.md"
extracted_sha256: "0105c6b89f680933df8dd699db5c2be4cfd4406e4644a0763001de89f1b34ee9"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/NetworkPolicyEndPort.md"
---

---
title: NetworkPolicyEndPort
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
    toVersion: "1.24"
  - stage: stable
    defaultValue: true
    fromVersion: "1.25"
    toVersion: "1.26"

removed: true
---
Allows you to define ports in a
[NetworkPolicy](/docs/concepts/services-networking/network-policies/)
rule as a range of port numbers.
