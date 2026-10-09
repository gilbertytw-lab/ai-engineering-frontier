---
document_id: "doc-aae92d6b34ee172b"
source_name: "reference/command-line-tools-reference/feature-gates/DisableAcceleratorUsageMetrics.md"
source_type: "text"
source_format: "md"
source_sha256: "fb29d4027ce7f40edb7663f2d84b725665a3e5abc093ffe11b8827ca0fc1dc92"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/DisableAcceleratorUsageMetrics.md"
extracted_sha256: "fb29d4027ce7f40edb7663f2d84b725665a3e5abc093ffe11b8827ca0fc1dc92"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/DisableAcceleratorUsageMetrics.md"
---

---
title: DisableAcceleratorUsageMetrics
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.19"
    toVersion: "1.19"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.20"
    toVersion: "1.24"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.25"
    toVersion: "1.27"    

removed: true  
---
[Disable accelerator metrics collected by the kubelet](/docs/concepts/cluster-administration/system-metrics/#disable-accelerator-metrics).
