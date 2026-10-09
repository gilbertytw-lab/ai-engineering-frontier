---
document_id: "doc-7a3bf2c24f150bcf"
source_name: "reference/command-line-tools-reference/feature-gates/KubeletPSI.md"
source_type: "text"
source_format: "md"
source_sha256: "928fef7e1d3d2f3658ae85e0037a7f78c7edf08018de982f41dcafcbc7c18b32"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/KubeletPSI.md"
extracted_sha256: "928fef7e1d3d2f3658ae85e0037a7f78c7edf08018de982f41dcafcbc7c18b32"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/KubeletPSI.md"
---

---
title: KubeletPSI
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.33"
    toVersion: "1.33"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.34"
    toVersion: "1.35"
  - stage: stable
    defaultValue: true
    fromVersion: "1.36"
    locked: true
---
Enable kubelet to surface Pressure Stall Information (PSI) metrics in the Summary API and Prometheus metrics.
