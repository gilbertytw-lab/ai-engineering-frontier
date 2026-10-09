---
document_id: "doc-9caac0a739d3f6bb"
source_name: "reference/command-line-tools-reference/feature-gates/KubeletCrashLoopBackOffMax.md"
source_type: "text"
source_format: "md"
source_sha256: "97301f1b436de0a8e5658a8a77ff2e0bfcabdbc505c00d0d354fe9494d5bc77a"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/KubeletCrashLoopBackOffMax.md"
extracted_sha256: "97301f1b436de0a8e5658a8a77ff2e0bfcabdbc505c00d0d354fe9494d5bc77a"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/KubeletCrashLoopBackOffMax.md"
---

---
title: KubeletCrashLoopBackOffMax
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.32"
    toVersion: "1.34"
  - stage: beta
    defaultValue: true
    fromVersion: "1.35"
---
Enables support for configurable per-node backoff maximums for restarting
containers in the `CrashLoopBackOff` state.
For more details, check the `crashLoopBackOff.maxContainerRestartPeriod` field in the
[kubelet config file](/docs/reference/config-api/kubelet-config.v1beta1/).
