---
document_id: "doc-d75f5a9dbeb3a558"
source_name: "reference/command-line-tools-reference/feature-gates/CRDObservedGenerationTracking.md"
source_type: "text"
source_format: "md"
source_sha256: "0ea2b1ab19cb47d1f872f565017af492a08c5e9f203185d44d59a078f24bfde3"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/CRDObservedGenerationTracking.md"
extracted_sha256: "0ea2b1ab19cb47d1f872f565017af492a08c5e9f203185d44d59a078f24bfde3"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/CRDObservedGenerationTracking.md"
---

---
title: CRDObservedGenerationTracking
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: false
    fromVersion: "1.35"
---
Allows for the observed generation to be tracked in CRD conditions. Setting to
false will make it so CRD conditions will have the observed generation wiped.
