---
document_id: "doc-f99a55be1a60c8f9"
source_name: "reference/command-line-tools-reference/feature-gates/CSINodeExpandSecret.md"
source_type: "text"
source_format: "md"
source_sha256: "662a1c1869e1aef741c6643aed0f7a128d8fd220667013c246d972c8f8978445"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/CSINodeExpandSecret.md"
extracted_sha256: "662a1c1869e1aef741c6643aed0f7a128d8fd220667013c246d972c8f8978445"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/CSINodeExpandSecret.md"
---

---
title: CSINodeExpandSecret
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.25"
    toVersion: "1.26"
  - stage: beta
    defaultValue: true
    fromVersion: "1.27"  
    toVersion: "1.28" 
  - stage: stable
    defaultValue: true
    fromVersion: "1.29"
    toVersion: "1.30"

removed: true
---
Enable passing secret authentication data to a CSI driver for use
 during a `NodeExpandVolume` CSI operation.
