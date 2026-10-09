---
document_id: "doc-410b1bfd0d9f77d6"
source_name: "reference/command-line-tools-reference/feature-gates/RemainingItemCount.md"
source_type: "text"
source_format: "md"
source_sha256: "bbd015107850ceea24f0030bc1982b215e1108fbd2c3ba5ef23c063531db1d43"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/RemainingItemCount.md"
extracted_sha256: "bbd015107850ceea24f0030bc1982b215e1108fbd2c3ba5ef23c063531db1d43"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/RemainingItemCount.md"
---

---
title: RemainingItemCount
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.15"
    toVersion: "1.15"
  - stage: beta
    defaultValue: true
    fromVersion: "1.16"
    toVersion: "1.28"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.29"   
    toVersion: "1.32"

removed: true
---
Allow the API servers to show a count of remaining
items in the response to a
[chunking list request](/docs/reference/using-api/api-concepts/#retrieving-large-results-sets-in-chunks).
