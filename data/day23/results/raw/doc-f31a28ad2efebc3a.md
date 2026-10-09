---
document_id: "doc-f31a28ad2efebc3a"
source_name: "reference/command-line-tools-reference/feature-gates/RecursiveReadOnlyMounts.md"
source_type: "text"
source_format: "md"
source_sha256: "048e43b8c8e5b7032e9feb35e450a4fdac45baa069fa649df0ba6cf70d7a7e99"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/RecursiveReadOnlyMounts.md"
extracted_sha256: "048e43b8c8e5b7032e9feb35e450a4fdac45baa069fa649df0ba6cf70d7a7e99"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/RecursiveReadOnlyMounts.md"
---

---
title: RecursiveReadOnlyMounts
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.30"
    toVersion: "1.30"
  - stage: beta
    defaultValue: true
    fromVersion: "1.31"
    toVersion: "1.32"
  - stage: stable
    defaultValue: true
    locked: true
    fromVersion: "1.33"
---
Enables support for recursive read-only mounts.
For more details, see [read-only mounts](/docs/concepts/storage/volumes/#read-only-mounts).
