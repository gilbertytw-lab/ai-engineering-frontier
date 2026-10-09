---
document_id: "doc-679a0441eaafc1de"
source_name: "reference/command-line-tools-reference/feature-gates/WinDSR.md"
source_type: "text"
source_format: "md"
source_sha256: "fe30bda964c685278589084313af5380a5639a3d6ad4a5a4149329df3e6986b2"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/WinDSR.md"
extracted_sha256: "fe30bda964c685278589084313af5380a5639a3d6ad4a5a4149329df3e6986b2"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/WinDSR.md"
---

---
title: WinDSR
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.14"
    toVersion: "1.32"
  - stage: beta
    defaultValue: true
    fromVersion: "1.33"
    toVersion: "1.33"
  - stage: stable
    locked: true
    defaultValue: true
    fromVersion: "1.34"

---
Allows kube-proxy to create DSR loadbalancers for Windows.
