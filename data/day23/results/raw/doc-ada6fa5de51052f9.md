---
document_id: "doc-ada6fa5de51052f9"
source_name: "reference/command-line-tools-reference/feature-gates/ClearingNominatedNodeNameAfterBinding.md"
source_type: "text"
source_format: "md"
source_sha256: "d6dc0d1a0e27d89a91eec94a68ee48c4da994db1c58351c212385f237c0cabca"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/ClearingNominatedNodeNameAfterBinding.md"
extracted_sha256: "d6dc0d1a0e27d89a91eec94a68ee48c4da994db1c58351c212385f237c0cabca"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/ClearingNominatedNodeNameAfterBinding.md"
---

---
title: ClearingNominatedNodeNameAfterBinding
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.34"
    toVersion: "1.34"
  - stage: beta
    defaultValue: true
    fromVersion: "1.35"
---
Enable clearing `.status.nominatedNodeName` whenever Pods are bound to nodes.
