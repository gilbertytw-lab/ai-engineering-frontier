---
document_id: "doc-ecf63717ed3d21c5"
source_name: "reference/command-line-tools-reference/feature-gates/JobBackoffLimitPerIndex.md"
source_type: "text"
source_format: "md"
source_sha256: "f6a04d621f88c250a526c27618024cd386d06c1ca2fc16c1f712b76b42bdf2d0"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/JobBackoffLimitPerIndex.md"
extracted_sha256: "f6a04d621f88c250a526c27618024cd386d06c1ca2fc16c1f712b76b42bdf2d0"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/JobBackoffLimitPerIndex.md"
---

---
title: JobBackoffLimitPerIndex
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.28"
    toVersion: "1.28"
  - stage: beta
    defaultValue: true
    fromVersion: "1.29"
    toVersion: "1.32"
  - stage: stable
    defaultValue: true
    locked: true
    fromVersion: "1.33"
---
Allows specifying the maximal number of pod
retries per index in Indexed jobs.
