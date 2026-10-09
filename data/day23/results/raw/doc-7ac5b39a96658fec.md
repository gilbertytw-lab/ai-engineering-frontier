---
document_id: "doc-7ac5b39a96658fec"
source_name: "reference/command-line-tools-reference/feature-gates/ValidateProxyRedirects.md"
source_type: "text"
source_format: "md"
source_sha256: "c85730a165f203b6d2d1c78dafd496052b5d49f5b8e6744c94f3cd79fda8725c"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/ValidateProxyRedirects.md"
extracted_sha256: "c85730a165f203b6d2d1c78dafd496052b5d49f5b8e6744c94f3cd79fda8725c"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/ValidateProxyRedirects.md"
---

---
# Removed from Kubernetes
title: ValidateProxyRedirects
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.12"
    toVersion: "1.13"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.14"
    toVersion: "1.21"    
  - stage: deprecated 
    defaultValue: true
    fromVersion: "1.22"
    toVersion: "1.24"

removed: true
---
This flag controls whether the API server should validate that redirects
are only followed to the same host. Only used if the `StreamingProxyRedirects` flag is enabled.
