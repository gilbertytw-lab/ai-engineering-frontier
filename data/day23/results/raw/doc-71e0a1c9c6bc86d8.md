---
document_id: "doc-71e0a1c9c6bc86d8"
source_name: "reference/command-line-tools-reference/feature-gates/WindowsGMSA.md"
source_type: "text"
source_format: "md"
source_sha256: "28b361997c1be0f7a6f075b5a71247101eca975c10b5e179fb38ee09ae285d30"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/WindowsGMSA.md"
extracted_sha256: "28b361997c1be0f7a6f075b5a71247101eca975c10b5e179fb38ee09ae285d30"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/WindowsGMSA.md"
---

---
# Removed from Kubernetes
title: WindowsGMSA
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.14"
    toVersion: "1.15"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.16"
    toVersion: "1.17"
  - stage: stable
    defaultValue: true
    fromVersion: "1.18"
    toVersion: "1.18"

removed: true
---
Enables passing of GMSA credential specs from pods to container runtimes.
