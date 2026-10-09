---
document_id: "doc-05d77ba7128fcfb3"
source_name: "reference/command-line-tools-reference/feature-gates/SecurityContextDeny.md"
source_type: "text"
source_format: "md"
source_sha256: "28aadec256556b5bf63e2383fe472f962653a72fecc6385cf954dafaf8e6a2a6"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/SecurityContextDeny.md"
extracted_sha256: "28aadec256556b5bf63e2383fe472f962653a72fecc6385cf954dafaf8e6a2a6"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/SecurityContextDeny.md"
---

---
title: SecurityContextDeny
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.27"
    toVersion: "1.29"
removed: true
---
This gate signals that the `SecurityContextDeny` admission controller is deprecated.
