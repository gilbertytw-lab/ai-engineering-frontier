---
document_id: "doc-4d8fbf5e82dbf750"
source_name: "reference/command-line-tools-reference/feature-gates/LocalStorageCapacityIsolation.md"
source_type: "text"
source_format: "md"
source_sha256: "8fe478f8da889501607fac551df4eb84c437f28eb72fbfad3e73394466674f57"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/LocalStorageCapacityIsolation.md"
extracted_sha256: "8fe478f8da889501607fac551df4eb84c437f28eb72fbfad3e73394466674f57"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/LocalStorageCapacityIsolation.md"
---

---
# Removed from Kubernetes
title: LocalStorageCapacityIsolation
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.7"
    toVersion: "1.9"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.10"
    toVersion: "1.24"
  - stage: stable
    defaultValue: true
    fromVersion: "1.25"
    toVersion: "1.26"

removed: true
---
Enable the consumption of
[local ephemeral storage](/docs/concepts/configuration/manage-resources-containers/)
and also the `sizeLimit` property of an
[emptyDir volume](/docs/concepts/storage/volumes/#emptydir).
