---
document_id: "doc-d5fa13e25dd76a7a"
source_name: "reference/command-line-tools-reference/feature-gates/InTreePluginGCEUnregister.md"
source_type: "text"
source_format: "md"
source_sha256: "8683cb52527a9ae1d27a7f762a5046888c4af64515f2cb0ff15545d35f2905f2"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/InTreePluginGCEUnregister.md"
extracted_sha256: "8683cb52527a9ae1d27a7f762a5046888c4af64515f2cb0ff15545d35f2905f2"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/InTreePluginGCEUnregister.md"
---

---
title: InTreePluginGCEUnregister
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
Stops registering the gce-pd in-tree plugin in kubelet
and volume controllers.
