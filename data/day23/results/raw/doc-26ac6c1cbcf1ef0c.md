---
document_id: "doc-26ac6c1cbcf1ef0c"
source_name: "reference/command-line-tools-reference/feature-gates/LogarithmicScaleDown.md"
source_type: "text"
source_format: "md"
source_sha256: "00c50e48fe42b01f3ba5e1fe1869df6e18f5b0a0c73521248f4d6774f1ed5fb3"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/LogarithmicScaleDown.md"
extracted_sha256: "00c50e48fe42b01f3ba5e1fe1869df6e18f5b0a0c73521248f4d6774f1ed5fb3"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/LogarithmicScaleDown.md"
---

---
title: LogarithmicScaleDown
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.21"
    toVersion: "1.21"
  - stage: beta
    defaultValue: true
    fromVersion: "1.22"
    toVersion: "1.30"
  - stage: stable
    defaultValue: true
    fromVersion: "1.31"
---
Enable semi-random selection of pods to evict on controller scaledown
based on logarithmic bucketing of pod timestamps.
