---
document_id: "doc-0b13fef9a5adb2b8"
source_name: "reference/command-line-tools-reference/feature-gates/VolumeScheduling.md"
source_type: "text"
source_format: "md"
source_sha256: "b6bbd022ae8d920b945a0052fd186237e67dfb9e122e298ff39ee19dc842408c"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/VolumeScheduling.md"
extracted_sha256: "b6bbd022ae8d920b945a0052fd186237e67dfb9e122e298ff39ee19dc842408c"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/VolumeScheduling.md"
---

---
# Removed from Kubernetes
title: VolumeScheduling
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.9"
    toVersion: "1.9"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.10"
    toVersion: "1.12"
  - stage: stable
    defaultValue: true
    fromVersion: "1.13"
    toVersion: "1.16"

removed: true
---
Enable volume topology aware scheduling and make the PersistentVolumeClaim
(PVC) binding aware of scheduling decisions. It also enables the usage of
[`local`](/docs/concepts/storage/volumes/#local) volume type when used together with the
`PersistentLocalVolumes` feature gate.
