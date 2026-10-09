---
document_id: "doc-7dacc6818b933d8f"
source_name: "reference/command-line-tools-reference/feature-gates/WatchBookmark.md"
source_type: "text"
source_format: "md"
source_sha256: "8b24407ccc8cc43d71ccb598f1d7162caa249e30337cf65ac27b4a83f601cab6"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/WatchBookmark.md"
extracted_sha256: "8b24407ccc8cc43d71ccb598f1d7162caa249e30337cf65ac27b4a83f601cab6"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/WatchBookmark.md"
---

---
title: WatchBookmark
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
    toVersion: "1.16" 
  - stage: stable
    defaultValue: true
    fromVersion: "1.17"  
    toVersion: "1.32"

removed: true
---
Enable support for watch bookmark events.
