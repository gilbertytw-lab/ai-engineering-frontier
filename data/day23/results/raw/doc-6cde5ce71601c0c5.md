---
document_id: "doc-6cde5ce71601c0c5"
source_name: "reference/command-line-tools-reference/feature-gates/ReadOnlyAPIDataVolumes.md"
source_type: "text"
source_format: "md"
source_sha256: "3a31e64a390e7270b188141484023523f81392922419125f3c88f47d7c60b2df"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/ReadOnlyAPIDataVolumes.md"
extracted_sha256: "3a31e64a390e7270b188141484023523f81392922419125f3c88f47d7c60b2df"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/ReadOnlyAPIDataVolumes.md"
---

---
# Removed from Kubernetes
title: ReadOnlyAPIDataVolumes
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: beta 
    defaultValue: true
    fromVersion: "1.8"
    toVersion: "1.9"
  - stage: stable
    fromVersion: "1.10"
    toVersion: "1.10"

removed: true  
---
Set [`configMap`](/docs/concepts/storage/volumes/#configmap), 
[`secret`](/docs/concepts/storage/volumes/#secret), 
[`downwardAPI`](/docs/concepts/storage/volumes/#downwardapi) and 
[`projected`](/docs/concepts/storage/volumes/#projected) 
{{< glossary_tooltip term_id="volume" text="volumes" >}} to be mounted read-only.

Since Kubernetes v1.10, these volume types are always read-only and you cannot opt out.
