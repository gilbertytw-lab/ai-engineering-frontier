---
document_id: "doc-1db6a6fcccbd5c9c"
source_name: "reference/command-line-tools-reference/feature-gates/UserNamespacesSupport.md"
source_type: "text"
source_format: "md"
source_sha256: "bb3ad71fd99b99af013648c9bc246d07f67dc4d2b3d41a1b4287c6f39c6dd2a6"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/UserNamespacesSupport.md"
extracted_sha256: "bb3ad71fd99b99af013648c9bc246d07f67dc4d2b3d41a1b4287c6f39c6dd2a6"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/UserNamespacesSupport.md"
---

---
title: UserNamespacesSupport
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.28"
    toVersion: "1.29"
  - stage: beta
    defaultValue: false
    fromVersion: "1.30"
    toVersion: "1.32"
  - stage: beta
    defaultValue: true
    fromVersion: "1.33"
    toVersion: "1.35"
  - stage: stable
    locked: true
    defaultValue: true
    fromVersion: "1.36"

---
Enable user namespace support for Pods.
