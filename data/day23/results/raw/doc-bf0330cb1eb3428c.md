---
document_id: "doc-bf0330cb1eb3428c"
source_name: "reference/command-line-tools-reference/feature-gates/BlockVolume.md"
source_type: "text"
source_format: "md"
source_sha256: "80485aac008fdc8ddaa1bd1ccf56e0e03378be07c75c82108655ea1e657db3aa"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/BlockVolume.md"
extracted_sha256: "80485aac008fdc8ddaa1bd1ccf56e0e03378be07c75c82108655ea1e657db3aa"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/BlockVolume.md"
---

---
# Removed from Kubernetes
title: BlockVolume
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.9"
    toVersion: "1.12"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.13"
    toVersion: "1.17"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.18"
    toVersion: "1.21"    

removed: true
---
Enable the definition and consumption of raw block devices in Pods.
See [Raw Block Volume Support](/docs/concepts/storage/persistent-volumes/#raw-block-volume-support)
for more details.
