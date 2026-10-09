---
document_id: "doc-719baf8e5094bd5e"
source_name: "reference/command-line-tools-reference/feature-gates/InTreePluginAzureDiskUnregister.md"
source_type: "text"
source_format: "md"
source_sha256: "79c0677a3fd6b6ce5b27cfe24e43815ca9b5a3ba47c312e2881374fb2d9fa7a8"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/InTreePluginAzureDiskUnregister.md"
extracted_sha256: "79c0677a3fd6b6ce5b27cfe24e43815ca9b5a3ba47c312e2881374fb2d9fa7a8"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/InTreePluginAzureDiskUnregister.md"
---

---
title: InTreePluginAzureDiskUnregister
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.21"
    toVersion: "1.30"

removed: true
---
Stops registering the azuredisk in-tree plugin in kubelet
and volume controllers.
