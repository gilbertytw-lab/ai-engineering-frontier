---
document_id: "doc-133bdf6e587dcad9"
source_name: "reference/command-line-tools-reference/feature-gates/SizeMemoryBackedVolumes.md"
source_type: "text"
source_format: "md"
source_sha256: "c0f29edd921f88efc01d3671769c4a8dabd3068933e14bd7f2be4ceff6485e71"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/SizeMemoryBackedVolumes.md"
extracted_sha256: "c0f29edd921f88efc01d3671769c4a8dabd3068933e14bd7f2be4ceff6485e71"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/SizeMemoryBackedVolumes.md"
---

---
title: SizeMemoryBackedVolumes
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.20"
    toVersion: "1.21"
  - stage: beta
    defaultValue: true
    fromVersion: "1.22"
    toVersion: "1.31"
  - stage: stable
    defaultValue: true
    locked: true
    fromVersion: "1.32"
    toVersion: "1.34"

removed: true

---
Enable kubelets to determine the size limit for
memory-backed volumes (mainly `emptyDir` volumes).
