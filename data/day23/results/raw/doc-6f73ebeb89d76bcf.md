---
document_id: "doc-6f73ebeb89d76bcf"
source_name: "reference/command-line-tools-reference/feature-gates/QOSReserved.md"
source_type: "text"
source_format: "md"
source_sha256: "0b18e3a0c5a85617496e4c4d5ebfaa7f8c7e22d01daaeff99b3653e27b6d2631"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/QOSReserved.md"
extracted_sha256: "0b18e3a0c5a85617496e4c4d5ebfaa7f8c7e22d01daaeff99b3653e27b6d2631"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/QOSReserved.md"
---

---
title: QOSReserved
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.11"
---
Allows resource reservations at the QoS level preventing pods
at lower QoS levels from bursting into resources requested at higher QoS levels
(memory only for now).
