---
document_id: "doc-f28f28c37cde716d"
source_name: "reference/command-line-tools-reference/feature-gates/StrictCostEnforcementForWebhooks.md"
source_type: "text"
source_format: "md"
source_sha256: "c92c9a2ce322deafec5a0e0bb99fe14482da874b8510c953ed0439fb70efbc5c"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/StrictCostEnforcementForWebhooks.md"
extracted_sha256: "c92c9a2ce322deafec5a0e0bb99fe14482da874b8510c953ed0439fb70efbc5c"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/StrictCostEnforcementForWebhooks.md"
---

---
title: StrictCostEnforcementForWebhooks
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: false
    fromVersion: "1.31"
    toVersion: "1.31"
  - stage: stable
    defaultValue: true
    fromVersion: "1.32"
---
Apply strict CEL cost validation for `matchConditions` within
admission webhooks.
