---
document_id: "doc-57c533bddba86fb9"
source_name: "reference/command-line-tools-reference/feature-gates/SizeBasedListCostEstimate.md"
source_type: "text"
source_format: "md"
source_sha256: "4f47bacd753b09b2bfb4d35b007b9856dc84a1718959e77d3e947efb74f1ce7a"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/SizeBasedListCostEstimate.md"
extracted_sha256: "4f47bacd753b09b2bfb4d35b007b9856dc84a1718959e77d3e947efb74f1ce7a"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/SizeBasedListCostEstimate.md"
---

---
title: SizeBasedListCostEstimate
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.34"
---
Enables APF to use size of objects for estimating request cost.
