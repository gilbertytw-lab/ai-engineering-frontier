---
document_id: "doc-de4d9332ef21d7ea"
source_name: "reference/command-line-tools-reference/feature-gates/ConsistentHTTPGetHandlers.md"
source_type: "text"
source_format: "md"
source_sha256: "abf8e341f5136eed4cf99d566f0178f3f10cb0e28c635561eabeee7c32d750f9"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/ConsistentHTTPGetHandlers.md"
extracted_sha256: "abf8e341f5136eed4cf99d566f0178f3f10cb0e28c635561eabeee7c32d750f9"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/ConsistentHTTPGetHandlers.md"
---

---
title: ConsistentHTTPGetHandlers
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: stable
    defaultValue: true
    fromVersion: "1.25"  
    toVersion: "1.30"

removed: true
---
Normalize HTTP get URL and Header passing for lifecycle
handlers with probers.
