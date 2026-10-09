---
document_id: "doc-5eb1caff1f652516"
source_name: "reference/command-line-tools-reference/feature-gates/MultiCIDRServiceAllocator.md"
source_type: "text"
source_format: "md"
source_sha256: "8da15e0b842834623968867e03673f34a6254b5003e59dfc849287587d366248"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/MultiCIDRServiceAllocator.md"
extracted_sha256: "8da15e0b842834623968867e03673f34a6254b5003e59dfc849287587d366248"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/MultiCIDRServiceAllocator.md"
---

---
title: MultiCIDRServiceAllocator
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.27"
    toVersion: "1.30"
  - stage: beta
    defaultValue: false
    fromVersion: "1.31"
    toVersion: "1.32"
  - stage: stable
    defaultValue: true
    locked: true
    fromVersion: "1.33"
---
Track IP address allocations for Service cluster IPs using IPAddress objects.
