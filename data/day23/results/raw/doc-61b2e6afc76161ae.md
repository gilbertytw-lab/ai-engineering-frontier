---
document_id: "doc-61b2e6afc76161ae"
source_name: "reference/command-line-tools-reference/feature-gates/MinimizeIPTablesRestore.md"
source_type: "text"
source_format: "md"
source_sha256: "900876a5e3667681bfb4091d94823dbb00815b1d8c4e8c1c1597b3877ea66dd4"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/MinimizeIPTablesRestore.md"
extracted_sha256: "900876a5e3667681bfb4091d94823dbb00815b1d8c4e8c1c1597b3877ea66dd4"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/MinimizeIPTablesRestore.md"
---

---
title: MinimizeIPTablesRestore
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.26"
    toVersion: "1.26"
  - stage: beta
    defaultValue: true
    fromVersion: "1.27"  
    toVersion: "1.27" 
  - stage: stable
    defaultValue: true
    fromVersion: "1.28" 
    toVersion: "1.29" 
removed: true
---
Enables new performance improvement logics
in the kube-proxy iptables mode.
