---
document_id: "doc-a062f7cebbed1d06"
source_name: "reference/command-line-tools-reference/feature-gates/VolumeSnapshotDataSource.md"
source_type: "text"
source_format: "md"
source_sha256: "73d8332251a99aa577f1d1cc26e466ff068928cdecaee1bb183721987441d8a9"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/VolumeSnapshotDataSource.md"
extracted_sha256: "73d8332251a99aa577f1d1cc26e466ff068928cdecaee1bb183721987441d8a9"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/VolumeSnapshotDataSource.md"
---

---
# Removed from Kubernetes
title: VolumeSnapshotDataSource
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.12"
    toVersion: "1.16"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.17"
    toVersion: "1.19"
  - stage: stable
    defaultValue: true
    fromVersion: "1.20"
    toVersion: "1.22"

removed: true
---
Enable volume snapshot data source support.
