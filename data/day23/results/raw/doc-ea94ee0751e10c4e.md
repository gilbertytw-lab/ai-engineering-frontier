---
document_id: "doc-ea94ee0751e10c4e"
source_name: "reference/command-line-tools-reference/feature-gates/PodLifecycleSleepAction.md"
source_type: "text"
source_format: "md"
source_sha256: "7040b5b29248b454b804eeb5b92dd51a471134c59cca5b85fece36157d5fa7ce"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/PodLifecycleSleepAction.md"
extracted_sha256: "7040b5b29248b454b804eeb5b92dd51a471134c59cca5b85fece36157d5fa7ce"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/PodLifecycleSleepAction.md"
---

---
title: PodLifecycleSleepAction
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.29"
    toVersion: "1.29"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.30"
    toVersion: "1.33"
  - stage: stable
    locked: true
    defaultValue: true
    fromVersion: "1.34"
---
Enables the `sleep` action in Container lifecycle hooks (`preStop` and `postStart`).
