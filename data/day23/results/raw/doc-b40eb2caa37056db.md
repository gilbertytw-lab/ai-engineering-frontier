---
document_id: "doc-b40eb2caa37056db"
source_name: "reference/command-line-tools-reference/feature-gates/KubeletCredentialProviders.md"
source_type: "text"
source_format: "md"
source_sha256: "7c1a4ee2531682736e4dcc337499488a6c0dec2d9c94b8ffc536e93139cb3283"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/KubeletCredentialProviders.md"
extracted_sha256: "7c1a4ee2531682736e4dcc337499488a6c0dec2d9c94b8ffc536e93139cb3283"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/KubeletCredentialProviders.md"
---

---
title: KubeletCredentialProviders
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.20"
    toVersion: "1.23"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.24"
    toVersion: "1.25"
  - stage: stable
    defaultValue: true
    fromVersion: "1.26"
    toVersion: "1.28"

removed: true
---
Enable kubelet exec credential providers for
image pull credentials.
