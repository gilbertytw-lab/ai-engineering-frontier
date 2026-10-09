---
document_id: "doc-53e6da30b4d1baba"
source_name: "reference/command-line-tools-reference/feature-gates/KubeletEnsureSecretPulledImages.md"
source_type: "text"
source_format: "md"
source_sha256: "36cb2f4d3a13fe76979cca58aec117f1e44192640830250a65cc7af80c566c0a"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/KubeletEnsureSecretPulledImages.md"
extracted_sha256: "36cb2f4d3a13fe76979cca58aec117f1e44192640830250a65cc7af80c566c0a"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/KubeletEnsureSecretPulledImages.md"
---

---
title: KubeletEnsureSecretPulledImages
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.33"
    toVersion: "1.34"
  - stage: beta
    defaultValue: true
    fromVersion: "1.35"
---
Ensure that pods requesting an image are authorized to access the image
with the provided credentials when the image is already present on the node.
See [Ensure Image Pull Credential Verification](/docs/concepts/containers/images#ensureimagepullcredentialverification).
