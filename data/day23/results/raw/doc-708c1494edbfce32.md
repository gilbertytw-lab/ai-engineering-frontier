---
document_id: "doc-708c1494edbfce32"
source_name: "reference/command-line-tools-reference/feature-gates/InPlacePodVerticalScalingMemoryBackedVolumes.md"
source_type: "text"
source_format: "md"
source_sha256: "a6713adea3545572958f2ca93b8d4e74b188200401ff431c8d7f5b2e886b0409"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/InPlacePodVerticalScalingMemoryBackedVolumes.md"
extracted_sha256: "a6713adea3545572958f2ca93b8d4e74b188200401ff431c8d7f5b2e886b0409"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/InPlacePodVerticalScalingMemoryBackedVolumes.md"
---

---
title: InPlacePodVerticalScalingMemoryBackedVolumes
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.37"
---
Enables in-place vertical scaling for memory-backed `emptyDir` volume size limits.
