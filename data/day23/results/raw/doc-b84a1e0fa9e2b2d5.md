---
document_id: "doc-b84a1e0fa9e2b2d5"
source_name: "reference/command-line-tools-reference/feature-gates/StatefulSetMinReadySeconds.md"
source_type: "text"
source_format: "md"
source_sha256: "9bfe897c018848c79f2b75902193106f9061461f715544cdea442614bf241f81"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/StatefulSetMinReadySeconds.md"
extracted_sha256: "9bfe897c018848c79f2b75902193106f9061461f715544cdea442614bf241f81"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/StatefulSetMinReadySeconds.md"
---

---
# Removed from Kubernetes
title: StatefulSetMinReadySeconds
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.22"
    toVersion: "1.22"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.23"
    toVersion: "1.24"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.25"
    toVersion: "1.26"    

removed: true
---
Allows `minReadySeconds` to be respected by
the StatefulSet controller.
