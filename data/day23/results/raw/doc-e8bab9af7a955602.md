---
document_id: "doc-e8bab9af7a955602"
source_name: "reference/command-line-tools-reference/feature-gates/StreamingProxyRedirects.md"
source_type: "text"
source_format: "md"
source_sha256: "1988e1bfd0d16dd27ae7eff1c4e2ba60c215b7e6dd1f63b08c793a09aa8b79d0"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/StreamingProxyRedirects.md"
extracted_sha256: "1988e1bfd0d16dd27ae7eff1c4e2ba60c215b7e6dd1f63b08c793a09aa8b79d0"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/StreamingProxyRedirects.md"
---

---
# Removed from Kubernetes
title: StreamingProxyRedirects
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: beta 
    defaultValue: false
    fromVersion: "1.5"
    toVersion: "1.5"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.6"
    toVersion: "1.17"    
  - stage: deprecated 
    defaultValue: true
    fromVersion: "1.18"
    toVersion: "1.21"
  - stage: deprecated 
    defaultValue: false
    fromVersion: "1.22"
    toVersion: "1.24"

removed: true
---
Instructs the API server to intercept (and follow) redirects from the
backend (kubelet) for streaming requests. Examples of streaming requests include the `exec`,
`attach` and `port-forward` requests.
