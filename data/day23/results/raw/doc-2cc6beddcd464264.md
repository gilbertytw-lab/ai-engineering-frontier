---
document_id: "doc-2cc6beddcd464264"
source_name: "reference/command-line-tools-reference/feature-gates/KubeletInUserNamespace.md"
source_type: "text"
source_format: "md"
source_sha256: "6ea6a080001a905c42d57848c55d5ebdd6579ae440d9216feaa39d4618b3c18b"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/KubeletInUserNamespace.md"
extracted_sha256: "6ea6a080001a905c42d57848c55d5ebdd6579ae440d9216feaa39d4618b3c18b"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/KubeletInUserNamespace.md"
---

---
title: KubeletInUserNamespace
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.22"
    toVersion: "1.36"
  - stage: beta
    defaultValue: true
    fromVersion: "1.37"
---
Enables support for running kubelet in a
{{<glossary_tooltip text="user namespace" term_id="userns">}}.
 See [Running Kubernetes Node Components as a Non-root User](/docs/tasks/administer-cluster/kubelet-in-userns/).
