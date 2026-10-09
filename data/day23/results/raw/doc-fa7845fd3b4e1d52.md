---
document_id: "doc-fa7845fd3b4e1d52"
source_name: "reference/command-line-tools-reference/feature-gates/RemoveSelfLink.md"
source_type: "text"
source_format: "md"
source_sha256: "30effcaf5b9c6223de49a1e45d7d23adfc6d7635cbfed0fd1d8ffaad8936dc57"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/RemoveSelfLink.md"
extracted_sha256: "30effcaf5b9c6223de49a1e45d7d23adfc6d7635cbfed0fd1d8ffaad8936dc57"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/RemoveSelfLink.md"
---

---
title: RemoveSelfLink
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.16"
    toVersion: "1.19"
  - stage: beta
    defaultValue: true
    fromVersion: "1.20"  
    toVersion: "1.23" 
  - stage: stable
    defaultValue: true
    fromVersion: "1.24"  
    toVersion: "1.29"

removed: true
---
Sets the `.metadata.selfLink` field to blank (empty string) for all
objects and collections. This field has been deprecated since the Kubernetes v1.16
release. When this feature is enabled, the `.metadata.selfLink` field remains part of
the Kubernetes API, but is always unset.
