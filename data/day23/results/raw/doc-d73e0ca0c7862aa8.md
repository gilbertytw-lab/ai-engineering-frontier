---
document_id: "doc-d73e0ca0c7862aa8"
source_name: "reference/command-line-tools-reference/feature-gates/PortForwardWebsockets.md"
source_type: "text"
source_format: "md"
source_sha256: "4f35f21036b7fcc7b40674d680a66525c422af57fa96bcc0e321dd0cc85af7b1"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/PortForwardWebsockets.md"
extracted_sha256: "4f35f21036b7fcc7b40674d680a66525c422af57fa96bcc0e321dd0cc85af7b1"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/PortForwardWebsockets.md"
---

---
title: PortForwardWebsockets
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.30"
    toVersion: "1.30"
  - stage: beta
    defaultValue: true
    fromVersion: "1.31"
---
Allow WebSocket streaming of the
portforward sub-protocol (`port-forward`) from clients requesting
version v2 (`v2.portforward.k8s.io`) of the sub-protocol.
