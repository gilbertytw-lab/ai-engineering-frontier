---
document_id: "doc-b6beb749e5b55d3b"
source_name: "reference/command-line-tools-reference/feature-gates/ComponentFlagz.md"
source_type: "text"
source_format: "md"
source_sha256: "45a6e0ff4c2f249caf76dabaf5fed15a1106ddcca0312d9baab37c5408ef7a92"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/ComponentFlagz.md"
extracted_sha256: "45a6e0ff4c2f249caf76dabaf5fed15a1106ddcca0312d9baab37c5408ef7a92"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/ComponentFlagz.md"
---

---
title: ComponentFlagz
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.32"
    toVersion: "1.35"
  - stage: beta
    defaultValue: true
    fromVersion: "1.36"
---
Enables the component's flagz endpoint.
See [zpages](/docs/reference/instrumentation/zpages/) for more information.
