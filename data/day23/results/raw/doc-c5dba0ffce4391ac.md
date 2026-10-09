---
document_id: "doc-c5dba0ffce4391ac"
source_name: "reference/command-line-tools-reference/feature-gates/ReadWriteOncePod.md"
source_type: "text"
source_format: "md"
source_sha256: "38614fbb04c9b965ca8a66028dd5506227377d1cd94e672726e5cc6c38cf53a5"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/ReadWriteOncePod.md"
extracted_sha256: "38614fbb04c9b965ca8a66028dd5506227377d1cd94e672726e5cc6c38cf53a5"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/ReadWriteOncePod.md"
---

---
title: ReadWriteOncePod
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.22"
    toVersion: "1.26"
  - stage: beta
    defaultValue: true
    fromVersion: "1.27"  
    toVersion: "1.28" 
  - stage: stable
    defaultValue: true
    fromVersion: "1.29" 
    toVersion: "1.30"

removed: true
---
Enables the usage of `ReadWriteOncePod` PersistentVolume
access mode.
