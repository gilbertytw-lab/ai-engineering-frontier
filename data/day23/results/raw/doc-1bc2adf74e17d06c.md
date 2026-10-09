---
document_id: "doc-1bc2adf74e17d06c"
source_name: "reference/command-line-tools-reference/feature-gates/KubeletFineGrainedAuthz.md"
source_type: "text"
source_format: "md"
source_sha256: "41806c0c988bdf317037792481adce9562ec6df114428e982f26fc2cf5d0da02"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/KubeletFineGrainedAuthz.md"
extracted_sha256: "41806c0c988bdf317037792481adce9562ec6df114428e982f26fc2cf5d0da02"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/KubeletFineGrainedAuthz.md"
---

---
title: KubeletFineGrainedAuthz
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.32"
    toVersion: "1.32"
  - stage: beta
    defaultValue: true
    fromVersion: "1.33"
    toVersion: "1.35"
  - stage: stable
    defaultValue: true
    fromVersion: "1.36"
---
Enable [fine-grained authorization](/docs/reference/access-authn-authz/kubelet-authn-authz/#fine-grained-authorization) 
for the kubelet's HTTP(s) API.
