---
document_id: "doc-b3b1cacf0346fcc8"
source_name: "reference/command-line-tools-reference/feature-gates/GRPCContainerProbeTLS.md"
source_type: "text"
source_format: "md"
source_sha256: "61d20541057ced9f8db5d328f8b9a3bad8b259599cdfabbd51185fcff08f965a"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/GRPCContainerProbeTLS.md"
extracted_sha256: "61d20541057ced9f8db5d328f8b9a3bad8b259599cdfabbd51185fcff08f965a"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/GRPCContainerProbeTLS.md"
---

---
title: GRPCContainerProbeTLS
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.37"
---
Enables TLS support for gRPC container probes. When enabled,
you can add the `mode` field to the `grpc` field in gRPC probes. Setting
`mode: TLS` on a liveness, readiness, or startup probe causes the kubelet
to connect over TLS (with `InsecureSkipVerify`).
See [Configure Liveness, Readiness and Startup Probes](/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#grpc-probe-tls).
