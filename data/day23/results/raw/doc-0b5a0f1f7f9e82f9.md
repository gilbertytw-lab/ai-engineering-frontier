---
document_id: "doc-0b5a0f1f7f9e82f9"
source_name: "reference/command-line-tools-reference/feature-gates/PodLifecycleSleepActionAllowZero.md"
source_type: "text"
source_format: "md"
source_sha256: "f6d6dc1f7a63bd5e800b19822efc225e318998c73b70567093cba7d35393cd27"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/PodLifecycleSleepActionAllowZero.md"
extracted_sha256: "f6d6dc1f7a63bd5e800b19822efc225e318998c73b70567093cba7d35393cd27"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/PodLifecycleSleepActionAllowZero.md"
---

---
title: PodLifecycleSleepActionAllowZero
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.32"
    toVersion: "1.32"
  - stage: beta
    defaultValue: true
    fromVersion: "1.33"
    toVersion: "1.33"
  - stage: stable
    locked: true
    defaultValue: true
    fromVersion: "1.34"
---
Enables setting zero value for the `sleep` action in
[container lifecycle hooks](/docs/concepts/containers/container-lifecycle-hooks/).
