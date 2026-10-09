---
document_id: "doc-1d87a55f20fc3be2"
source_name: "reference/command-line-tools-reference/feature-gates/PodReadinessGates.md"
source_type: "text"
source_format: "md"
source_sha256: "59ac41cd11e25f4d4eab65019190dc5f173c8b8364c4da42db9f692716bf70be"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/PodReadinessGates.md"
extracted_sha256: "59ac41cd11e25f4d4eab65019190dc5f173c8b8364c4da42db9f692716bf70be"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/PodReadinessGates.md"
---

---
# Removed from Kubernetes
title: PodReadinessGates
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.11"
    toVersion: "1.11"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.12"
    toVersion: "1.13"
  - stage: stable
    defaultValue: true
    fromVersion: "1.14"
    toVersion: "1.16"

removed: true
---
Enable the setting of `PodReadinessGate` field for extending
Pod readiness evaluation. See [Pod readiness gate](/docs/concepts/workloads/pods/pod-lifecycle/#pod-readiness-gate)
for more details.
