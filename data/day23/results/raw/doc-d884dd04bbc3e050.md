---
document_id: "doc-d884dd04bbc3e050"
source_name: "reference/command-line-tools-reference/feature-gates/NodeLease.md"
source_type: "text"
source_format: "md"
source_sha256: "a2e9631f5f1a75b6155970054b17ac850e3ec1ba8db85e357c06e29b93b27940"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/NodeLease.md"
extracted_sha256: "a2e9631f5f1a75b6155970054b17ac850e3ec1ba8db85e357c06e29b93b27940"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/NodeLease.md"
---

---
# Removed from Kubernetes
title: NodeLease
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.12"
    toVersion: "1.13"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.14"
    toVersion: "1.16"
  - stage: stable
    defaultValue: true
    fromVersion: "1.17"
    toVersion: "1.23"

removed: true
---
Enable the new Lease API to report node heartbeats, which could be used as a node health signal.
