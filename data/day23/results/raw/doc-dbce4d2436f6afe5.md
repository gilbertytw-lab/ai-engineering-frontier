---
document_id: "doc-dbce4d2436f6afe5"
source_name: "reference/command-line-tools-reference/feature-gates/InTreePluginAWSUnregister.md"
source_type: "text"
source_format: "md"
source_sha256: "fd1b198969b4f1c6c3541159325c018f3b44ec69553b52894d60904700c16c7b"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/InTreePluginAWSUnregister.md"
extracted_sha256: "fd1b198969b4f1c6c3541159325c018f3b44ec69553b52894d60904700c16c7b"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/InTreePluginAWSUnregister.md"
---

---
title: InTreePluginAWSUnregister
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
Stops registering the aws-ebs in-tree plugin in kubelet
and volume controllers.
