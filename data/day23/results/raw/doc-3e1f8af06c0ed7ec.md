---
document_id: "doc-3e1f8af06c0ed7ec"
source_name: "reference/command-line-tools-reference/feature-gates/NodeDisruptionExclusion.md"
source_type: "text"
source_format: "md"
source_sha256: "9264dbd182dddca9dba97027ebddfb443d9d937ef40e9d97675c138053e170e8"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/NodeDisruptionExclusion.md"
extracted_sha256: "9264dbd182dddca9dba97027ebddfb443d9d937ef40e9d97675c138053e170e8"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/NodeDisruptionExclusion.md"
---

---
# Removed from Kubernetes
title: NodeDisruptionExclusion
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.16"
    toVersion: "1.18"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.19"
    toVersion: "1.20"
  - stage: stable
    defaultValue: true
    fromVersion: "1.21"
    toVersion: "1.22"

removed: true
---
Enable use of the Node label `node.kubernetes.io/exclude-disruption`
which prevents nodes from being evacuated during zone failures.
