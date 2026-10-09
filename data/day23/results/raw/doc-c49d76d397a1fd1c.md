---
document_id: "doc-c49d76d397a1fd1c"
source_name: "reference/command-line-tools-reference/feature-gates/StreamingCollectionEncodingToJSON.md"
source_type: "text"
source_format: "md"
source_sha256: "bd7d7820e7b58d4a8bfecaa325dc1e962045021335e01ec0be7b83b06fdcd18c"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/StreamingCollectionEncodingToJSON.md"
extracted_sha256: "bd7d7820e7b58d4a8bfecaa325dc1e962045021335e01ec0be7b83b06fdcd18c"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/StreamingCollectionEncodingToJSON.md"
---

---
title: StreamingCollectionEncodingToJSON
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.33"
    toVersion: "1.33"
  - stage: stable
    locked: true
    defaultValue: true
    fromVersion: "1.34"

---
Allow the API server JSON encoder to encode collections item by item, instead of all at once.
