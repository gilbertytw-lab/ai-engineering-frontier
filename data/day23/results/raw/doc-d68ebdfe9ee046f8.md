---
document_id: "doc-d68ebdfe9ee046f8"
source_name: "reference/command-line-tools-reference/feature-gates/DisableCPUQuotaWithExclusiveCPUs.md"
source_type: "text"
source_format: "md"
source_sha256: "a8a26deaaf8d08540120953f66599f907133194ed4d42ae07e67f4f357c173cc"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/DisableCPUQuotaWithExclusiveCPUs.md"
extracted_sha256: "a8a26deaaf8d08540120953f66599f907133194ed4d42ae07e67f4f357c173cc"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/DisableCPUQuotaWithExclusiveCPUs.md"
---

---
title: DisableCPUQuotaWithExclusiveCPUs
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.33"
---

When the feature gate `DisableCPUQuotaWithExclusiveCPUs` is enabled (the default), then Kubernetes
does **not** enforce CPU quota for Pods that use the [Guaranteed](/docs/concepts/workloads/pods/pod-qos/#guaranteed)
{{< glossary_tooltip text="QoS class" term_id="qos-class" >}}.

You can disable the `DisableCPUQuotaWithExclusiveCPUs` feature gate to restore the legacy behavior.
