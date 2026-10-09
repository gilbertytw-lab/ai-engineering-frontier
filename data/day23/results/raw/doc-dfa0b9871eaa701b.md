---
document_id: "doc-dfa0b9871eaa701b"
source_name: "reference/command-line-tools-reference/feature-gates/NamespaceDefaultLabelName.md"
source_type: "text"
source_format: "md"
source_sha256: "0c677fc7853f63a2e238ebb87a47d207f9a258cea9bf5d546f96edf0d03fc3d4"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/NamespaceDefaultLabelName.md"
extracted_sha256: "0c677fc7853f63a2e238ebb87a47d207f9a258cea9bf5d546f96edf0d03fc3d4"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/NamespaceDefaultLabelName.md"
---

---
# Removed from Kubernetes
title: NamespaceDefaultLabelName
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: beta 
    defaultValue: true
    fromVersion: "1.21"
    toVersion: "1.21"
  - stage: stable
    defaultValue: true
    fromVersion: "1.22"
    toVersion: "1.23"

removed: true
---
Configure the API Server to set an immutable
{{< glossary_tooltip text="label" term_id="label" >}} `kubernetes.io/metadata.name`
on all namespaces, containing the namespace name.
