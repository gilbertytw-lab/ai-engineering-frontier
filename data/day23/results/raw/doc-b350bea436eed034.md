---
document_id: "doc-b350bea436eed034"
source_name: "reference/command-line-tools-reference/feature-gates/PodOverhead.md"
source_type: "text"
source_format: "md"
source_sha256: "891a30e6abf3cdeac37a28b654ca85f80813c9c818bae1791846c76c1e0129ec"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/PodOverhead.md"
extracted_sha256: "891a30e6abf3cdeac37a28b654ca85f80813c9c818bae1791846c76c1e0129ec"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/PodOverhead.md"
---

---
# Removed from Kubernetes
title: PodOverhead
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.16"
    toVersion: "1.17"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.18"
    toVersion: "1.23"
  - stage: stable
    defaultValue: true
    fromVersion: "1.24"
    toVersion: "1.25"

removed: true
---
Enable the [PodOverhead](/docs/concepts/scheduling-eviction/pod-overhead/)
feature to account for pod overheads.
