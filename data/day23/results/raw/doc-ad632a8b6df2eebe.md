---
document_id: "doc-ad632a8b6df2eebe"
source_name: "reference/command-line-tools-reference/feature-gates/DRASchedulerFilterTimeout.md"
source_type: "text"
source_format: "md"
source_sha256: "7a8c7e879d2a8033dcf5207b5c6b39d418b898f79eaf174243e9f13b4dfe9f22"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/DRASchedulerFilterTimeout.md"
extracted_sha256: "7a8c7e879d2a8033dcf5207b5c6b39d418b898f79eaf174243e9f13b4dfe9f22"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/DRASchedulerFilterTimeout.md"
---

---
title: DRASchedulerFilterTimeout
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.34"

---
Enables aborting the per-node filter operation in the scheduler after a certain
time (10 seconds by default, configurable in the DynamicResources scheduler
plugin configuration).
