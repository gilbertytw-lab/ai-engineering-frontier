---
document_id: "doc-d4c6164cec9324df"
source_name: "reference/command-line-tools-reference/feature-gates/VolumeLimitScaling.md"
source_type: "text"
source_format: "md"
source_sha256: "462d32b99374bda19a5897a9ce9bf8fa353eec2fa11ab9b008bae293e40214c3"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/VolumeLimitScaling.md"
extracted_sha256: "462d32b99374bda19a5897a9ce9bf8fa353eec2fa11ab9b008bae293e40214c3"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/VolumeLimitScaling.md"
---

---
title: VolumeLimitScaling
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.35"
    toVersion: "1.36"
  - stage: beta
    defaultValue: true
    fromVersion: "1.37"
---
Enables volume limit scaling for CSI drivers. This allows scheduler to
co-ordinate better with cluster-autoscaler for storage limits.
See [Storage Limits](/docs/concepts/storage/storage-limits/)
for more information.
