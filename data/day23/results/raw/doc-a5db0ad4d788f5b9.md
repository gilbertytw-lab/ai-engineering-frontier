---
document_id: "doc-a5db0ad4d788f5b9"
source_name: "reference/command-line-tools-reference/feature-gates/StatefulSetAutoDeletePVC.md"
source_type: "text"
source_format: "md"
source_sha256: "266e50703b5bec42ff03a7fee90da07685475eb0a6b909e422207ffcf54cf316"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/StatefulSetAutoDeletePVC.md"
extracted_sha256: "266e50703b5bec42ff03a7fee90da07685475eb0a6b909e422207ffcf54cf316"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/StatefulSetAutoDeletePVC.md"
---

---
title: StatefulSetAutoDeletePVC
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.23"
    toVersion: "1.26"
  - stage: beta
    defaultValue: true
    fromVersion: "1.27"
    toVersion: "1.31"
  - stage: stable
    defaultValue: true
    fromVersion: "1.32"
---
Allows the use of the optional `.spec.persistentVolumeClaimRetentionPolicy` field, 
providing control over the deletion of PVCs in a StatefulSet's lifecycle.
See
[PersistentVolumeClaim retention](/docs/concepts/workloads/controllers/statefulset/#persistentvolumeclaim-retention)
for more details.
