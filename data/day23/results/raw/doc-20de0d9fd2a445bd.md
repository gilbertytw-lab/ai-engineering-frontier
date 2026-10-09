---
document_id: "doc-20de0d9fd2a445bd"
source_name: "reference/command-line-tools-reference/feature-gates/PersistentVolumeClaimUnusedSinceTime.md"
source_type: "text"
source_format: "md"
source_sha256: "89429cc98f446bebd579dc98b935ba6986b7b4181b59974ca75fb293b152d854"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/PersistentVolumeClaimUnusedSinceTime.md"
extracted_sha256: "89429cc98f446bebd579dc98b935ba6986b7b4181b59974ca75fb293b152d854"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/PersistentVolumeClaimUnusedSinceTime.md"
---

---
title: PersistentVolumeClaimUnusedSinceTime
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.36"
    toVersion: "1.36"
  - stage: beta
    defaultValue: true
    fromVersion: "1.37"
---
When enabled, the PVC protection controller adds an `Unused` condition to
PersistentVolumeClaims that tracks whether the PVC is currently referenced by
any non-terminal Pod. The condition's `lastTransitionTime` records when the PVC
last transitioned between being in use and being unused.
