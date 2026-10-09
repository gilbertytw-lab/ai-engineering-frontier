---
document_id: "doc-f486abf8f9fdd112"
source_name: "reference/command-line-tools-reference/feature-gates/CustomResourceFieldSelectors.md"
source_type: "text"
source_format: "md"
source_sha256: "6f9e73ba13930e440e9010bd5d7f663287009c43fd2191d497eb061506e2f53e"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/CustomResourceFieldSelectors.md"
extracted_sha256: "6f9e73ba13930e440e9010bd5d7f663287009c43fd2191d497eb061506e2f53e"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/CustomResourceFieldSelectors.md"
---

---
title: CustomResourceFieldSelectors
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.30"  
    toVersion: "1.30"
  - stage: beta
    defaultValue: true
    fromVersion: "1.31" 
    toVersion: "1.31"
  - stage: stable
    defaultValue: true
    fromVersion: "1.32" 
---

Enable `selectableFields` in the
{{< glossary_tooltip term_id="CustomResourceDefinition" text="CustomResourceDefinition" >}} API to allow filtering
of custom resource **list**, **watch** and **deletecollection** requests.
