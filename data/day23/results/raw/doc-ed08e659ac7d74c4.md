---
document_id: "doc-ed08e659ac7d74c4"
source_name: "reference/command-line-tools-reference/feature-gates/MutablePodResourcesForSuspendedJobs.md"
source_type: "text"
source_format: "md"
source_sha256: "ec29ce59f328c390d9ac3ecd24883dbb0914369c66f8046e2705d1209b5ddd72"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/MutablePodResourcesForSuspendedJobs.md"
extracted_sha256: "ec29ce59f328c390d9ac3ecd24883dbb0914369c66f8046e2705d1209b5ddd72"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/MutablePodResourcesForSuspendedJobs.md"
---

---
title: MutablePodResourcesForSuspendedJobs 
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.35"
    toVersion: "1.35"
  - stage: beta
    defaultValue: true
    fromVersion: "1.36"
removed: false
---
Enable the ability to patch pod templates for suspended Jobs, in order to change requests or limits for infrastructure resources.
