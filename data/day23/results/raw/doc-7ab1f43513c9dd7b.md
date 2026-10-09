---
document_id: "doc-7ab1f43513c9dd7b"
source_name: "reference/command-line-tools-reference/feature-gates/HPAContainerMetrics.md"
source_type: "text"
source_format: "md"
source_sha256: "5d94ebea28d37c7ddb8b2b6d22e778d7b2d89a345189e3f892ff800e0d6ca642"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/HPAContainerMetrics.md"
extracted_sha256: "5d94ebea28d37c7ddb8b2b6d22e778d7b2d89a345189e3f892ff800e0d6ca642"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/HPAContainerMetrics.md"
---

---
title: HPAContainerMetrics
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.20"
    toVersion: "1.26"
  - stage: beta
    defaultValue: true
    fromVersion: "1.27"
    toVersion: "1.29"
  - stage: stable
    defaultValue: true
    fromVersion: "1.30"
    toVersion: "1.31"

removed: true
---
Allow {{< glossary_tooltip text="HorizontalPodAutoscalers" term_id="horizontal-pod-autoscaler" >}}
to scale based on metrics from individual containers within target pods.
