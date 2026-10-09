---
document_id: "doc-aa67af8eb435a5d1"
source_name: "reference/command-line-tools-reference/feature-gates/StorageCapacityScoring.md"
source_type: "text"
source_format: "md"
source_sha256: "c4af0ab899d4a214bd1e5071526606b478be10ef7acad51c2f5e899de19d3d3d"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/StorageCapacityScoring.md"
extracted_sha256: "c4af0ab899d4a214bd1e5071526606b478be10ef7acad51c2f5e899de19d3d3d"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/StorageCapacityScoring.md"
---

---
title: StorageCapacityScoring
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.33"
    toVersion: "1.36"
  - stage: beta
    defaultValue: true
    fromVersion: "1.37"
---
The feature gate `VolumeCapacityPriority` was used in v1.32 to support storage that are
statically provisioned. Starting from v1.33, the new feature gate `StorageCapacityScoring`
replaces the old `VolumeCapacityPriority` gate with added support to dynamically provisioned storage.
When `StorageCapacityScoring` is enabled, the VolumeBinding plugin in the kube-scheduler is extended
to score Nodes based on the storage capacity on each of them.
This feature is applicable to CSI volumes that supported [Storage Capacity](/docs/concepts/storage/storage-capacity/),
including local storage backed by a CSI driver.
