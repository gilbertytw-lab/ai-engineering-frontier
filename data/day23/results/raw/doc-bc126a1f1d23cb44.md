---
document_id: "doc-bc126a1f1d23cb44"
source_name: "reference/command-line-tools-reference/feature-gates/WinOverlay.md"
source_type: "text"
source_format: "md"
source_sha256: "99451bb054314409c925026a9ed07cbb073a33b2bfb2651873bfdd473a16e1fb"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/WinOverlay.md"
extracted_sha256: "99451bb054314409c925026a9ed07cbb073a33b2bfb2651873bfdd473a16e1fb"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/WinOverlay.md"
---

---
title: WinOverlay
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.14"
    toVersion: "1.19"
  - stage: beta
    defaultValue: true
    fromVersion: "1.20"
    toVersion: "1.33"
  - stage: stable
    locked: true
    defaultValue: true
    fromVersion: "1.34"

---
Allows kube-proxy to run in overlay mode for Windows.
