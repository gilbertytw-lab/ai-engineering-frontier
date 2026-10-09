---
document_id: "doc-efea4159cfb7cc60"
source_name: "reference/command-line-tools-reference/feature-gates/KubeletTracing.md"
source_type: "text"
source_format: "md"
source_sha256: "366f02a2aeb14292287d5a4ed5ff7c6fe3f36f451b490ec596d4228c8134546a"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/KubeletTracing.md"
extracted_sha256: "366f02a2aeb14292287d5a4ed5ff7c6fe3f36f451b490ec596d4228c8134546a"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/KubeletTracing.md"
---

---
title: KubeletTracing
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.25"
    toVersion: "1.26"
  - stage: beta
    defaultValue: true
    fromVersion: "1.27"
    toVersion: "1.33"
  - stage: stable
    locked: true
    defaultValue: true
    fromVersion: "1.34"
---
Add support for distributed tracing in the kubelet.
When enabled, kubelet CRI interface and authenticated http servers are instrumented to generate
OpenTelemetry trace spans.
See [Traces for Kubernetes System Components](/docs/concepts/cluster-administration/system-traces) for more details.
