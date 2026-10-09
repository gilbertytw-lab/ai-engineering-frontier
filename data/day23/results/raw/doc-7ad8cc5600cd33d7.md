---
document_id: "doc-7ad8cc5600cd33d7"
source_name: "reference/command-line-tools-reference/feature-gates/VolumeAttributesClass.md"
source_type: "text"
source_format: "md"
source_sha256: "15ef2d8452e0e4ee6276481c8875292ead87dae606b35760f66e53b57c56bb84"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/VolumeAttributesClass.md"
extracted_sha256: "15ef2d8452e0e4ee6276481c8875292ead87dae606b35760f66e53b57c56bb84"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/VolumeAttributesClass.md"
---

---
title: VolumeAttributesClass
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.29"
    toVersion: "1.30"
  - stage: beta
    defaultValue: false
    fromVersion: "1.31"
    toVersion: "1.33"
  - stage: stable
    defaultValue: true
    fromVersion: "1.34"
    toVersion: "1.35"
  - stage: stable
    defaultValue: true
    locked: true
    fromVersion: "1.36"
---
Enable support for VolumeAttributesClasses.
See [Volume Attributes Classes](/docs/concepts/storage/volume-attributes-classes/)
for more information.
