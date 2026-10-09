---
document_id: "doc-6c4e9eb061a35bbe"
source_name: "reference/command-line-tools-reference/feature-gates/InPlacePodVerticalScalingAllocatedStatus.md"
source_type: "text"
source_format: "md"
source_sha256: "ba783624209dbcbaebf7f90eef8b255523447578f85beb46f134cf4b37eadb41"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/InPlacePodVerticalScalingAllocatedStatus.md"
extracted_sha256: "ba783624209dbcbaebf7f90eef8b255523447578f85beb46f134cf4b37eadb41"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/InPlacePodVerticalScalingAllocatedStatus.md"
---

---
title: InPlacePodVerticalScalingAllocatedStatus
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.32"
    toVersion: "1.32"
  - stage: deprecated
    defaultValue: false
    fromVersion: "1.33"

---
Enables the `allocatedResources` field in the container status.
This feature requires the `InPlacePodVerticalScaling` gate be enabled as well.
