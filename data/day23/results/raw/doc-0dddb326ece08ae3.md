---
document_id: "doc-0dddb326ece08ae3"
source_name: "reference/command-line-tools-reference/feature-gates/InOrderInformers.md"
source_type: "text"
source_format: "md"
source_sha256: "450c57043eba49a67312de52ee8bead569e66b287f1e8db45f1427db171080c0"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/InOrderInformers.md"
extracted_sha256: "450c57043eba49a67312de52ee8bead569e66b287f1e8db45f1427db171080c0"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/InOrderInformers.md"
---

---
title: InOrderInformers
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: true
    fromVersion: "1.33"
    toVersion: "1.33"
  - stage: beta
    defaultValue: true
    fromVersion: "1.34"
---
Force the informers to deliver watch stream events in order instead of out of order.
