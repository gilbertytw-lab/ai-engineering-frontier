---
document_id: "doc-aed42009c441eab5"
source_name: "reference/command-line-tools-reference/feature-gates/AllowExtTrafficLocalEndpoints.md"
source_type: "text"
source_format: "md"
source_sha256: "58a1f1ad956cbeea3de84490b5d7ce2ebb9e265633b4c0889503553b9e8b1885"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/AllowExtTrafficLocalEndpoints.md"
extracted_sha256: "58a1f1ad956cbeea3de84490b5d7ce2ebb9e265633b4c0889503553b9e8b1885"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/AllowExtTrafficLocalEndpoints.md"
---

---
# Removed from Kubernetes
title: AllowExtTrafficLocalEndpoints
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: beta 
    defaultValue: false
    fromVersion: "1.4"
    toVersion: "1.6"
  - stage: stable
    defaultValue: true
    fromVersion: "1.7"
    toVersion: "1.9"

removed: true
---
Enable a service to route external requests to node local endpoints.
