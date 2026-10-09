---
document_id: "doc-c1bf79a04fcd3a34"
source_name: "reference/command-line-tools-reference/feature-gates/InTreePluginPortworxUnregister.md"
source_type: "text"
source_format: "md"
source_sha256: "0034ca9113482df36c0db3d0c10967cb7883d53a8a2a3da688b31f02d18da75e"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/InTreePluginPortworxUnregister.md"
extracted_sha256: "0034ca9113482df36c0db3d0c10967cb7883d53a8a2a3da688b31f02d18da75e"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/InTreePluginPortworxUnregister.md"
---

---
title: InTreePluginPortworxUnregister
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.23"
    toVersion: "1.35"

removed: true
---
Stops registering the Portworx in-tree plugin in kubelet
and volume controllers.
