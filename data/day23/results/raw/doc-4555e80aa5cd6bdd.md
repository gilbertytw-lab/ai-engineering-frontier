---
document_id: "doc-4555e80aa5cd6bdd"
source_name: "reference/command-line-tools-reference/feature-gates/DynamicResourceAllocation.md"
source_type: "text"
source_format: "md"
source_sha256: "9c88acfb651121fba261230a1c5a1c9adba30b5bea8e675c0c80496d4ab4624f"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/DynamicResourceAllocation.md"
extracted_sha256: "9c88acfb651121fba261230a1c5a1c9adba30b5bea8e675c0c80496d4ab4624f"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/DynamicResourceAllocation.md"
---

---
title: DynamicResourceAllocation
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.30"
    toVersion: "1.31"
  - stage: beta
    defaultValue: false
    fromVersion: "1.32"
    toVersion: "1.33"
  - stage: stable
    defaultValue: true
    locked: false
    fromVersion: "1.34"
    toVersion: "1.34"
  - stage: stable
    defaultValue: true
    locked: true
    fromVersion: "1.35"

---
Enables support for resources with custom parameters and a lifecycle
that is independent of a Pod. Allocation of resources is handled
by the Kubernetes scheduler based on "structured parameters".
