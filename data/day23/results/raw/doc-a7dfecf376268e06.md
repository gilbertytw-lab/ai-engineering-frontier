---
document_id: "doc-a7dfecf376268e06"
source_name: "reference/command-line-tools-reference/feature-gates/JobManagedBy.md"
source_type: "text"
source_format: "md"
source_sha256: "0b4598c613b502d292a6c0cf777e51a72165c47991d31d80375a602d89545470"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/JobManagedBy.md"
extracted_sha256: "0b4598c613b502d292a6c0cf777e51a72165c47991d31d80375a602d89545470"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/JobManagedBy.md"
---

---
title: JobManagedBy
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.30"
    toVersion: "1.31"
  - stage: beta
    defaultValue: true
    fromVersion: "1.32"
    toVersion: "1.34"
  - stage: stable
    defaultValue: true
    fromVersion: "1.35"
---
Allows to delegate reconciliation of a Job object to an external controller.
