---
document_id: "doc-39d16c34ddb8d3d7"
source_name: "reference/command-line-tools-reference/feature-gates/StrictCostEnforcementForVAP.md"
source_type: "text"
source_format: "md"
source_sha256: "d4fd0a969944960563ce87f8d56348d1dcd73fe646befad953f2e66b8c57344d"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/StrictCostEnforcementForVAP.md"
extracted_sha256: "d4fd0a969944960563ce87f8d56348d1dcd73fe646befad953f2e66b8c57344d"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/StrictCostEnforcementForVAP.md"
---

---
title: StrictCostEnforcementForVAP
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: false
    fromVersion: "1.30"
    toVersion: "1.31"
  - stage: stable
    defaultValue: true
    fromVersion: "1.32"
---
Apply strict CEL cost validation for ValidatingAdmissionPolicies.
