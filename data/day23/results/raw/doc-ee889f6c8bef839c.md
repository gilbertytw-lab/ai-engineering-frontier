---
document_id: "doc-ee889f6c8bef839c"
source_name: "reference/command-line-tools-reference/feature-gates/TokenRequestProjection.md"
source_type: "text"
source_format: "md"
source_sha256: "692cfad8721a10e6f1be670a852641d9cc6def2f3f80b76e41ff780b126dfb97"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/TokenRequestProjection.md"
extracted_sha256: "692cfad8721a10e6f1be670a852641d9cc6def2f3f80b76e41ff780b126dfb97"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/TokenRequestProjection.md"
---

---
# Removed from Kubernetes
title: TokenRequestProjection
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.11"
    toVersion: "1.11"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.12"
    toVersion: "1.19"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.20"
    toVersion: "1.21"    

removed: true
---
Enable the injection of service account tokens into a Pod through a
[`projected` volume](/docs/concepts/storage/volumes/#projected).
