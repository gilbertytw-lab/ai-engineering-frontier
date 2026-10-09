---
document_id: "doc-90e1fdd6f34ca728"
source_name: "reference/command-line-tools-reference/feature-gates/WatchFromStorageWithoutResourceVersion.md"
source_type: "text"
source_format: "md"
source_sha256: "b9fab00d2bbb44a878764a70ec6c004f09b4b435af8b57ba87f0c15b81566fcd"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/WatchFromStorageWithoutResourceVersion.md"
extracted_sha256: "b9fab00d2bbb44a878764a70ec6c004f09b4b435af8b57ba87f0c15b81566fcd"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/WatchFromStorageWithoutResourceVersion.md"
---

---
title: WatchFromStorageWithoutResourceVersion
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: false
    fromVersion: "1.30"
    toVersion: "1.32"
  - stage: deprecated
    defaultValue: false
    fromVersion: "1.33"


---
Enables watches without `resourceVersion` to be served from storage.
