---
document_id: "doc-a3e1cfdcf8e9a332"
source_name: "reference/command-line-tools-reference/feature-gates/VolumeSubpath.md"
source_type: "text"
source_format: "md"
source_sha256: "11e4c2d9860353c5facdc24529fd42175c7517518b814107935e342e52801e5b"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/VolumeSubpath.md"
extracted_sha256: "11e4c2d9860353c5facdc24529fd42175c7517518b814107935e342e52801e5b"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/VolumeSubpath.md"
---

---
# Removed from Kubernetes
title: VolumeSubpath
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: stable
    defaultValue: true
    fromVersion: "1.10"
    toVersion: "1.24"

removed: true
---
Allow mounting a subpath of a volume in a container.
