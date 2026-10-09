---
document_id: "doc-feee8400a3d87c8b"
source_name: "reference/command-line-tools-reference/feature-gates/ServiceAccountNodeAudienceRestriction.md"
source_type: "text"
source_format: "md"
source_sha256: "34b7155bc7538f2c1515b7fee50b1bcc4ef5afc4cd821389629a396a488bd5f6"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/ServiceAccountNodeAudienceRestriction.md"
extracted_sha256: "34b7155bc7538f2c1515b7fee50b1bcc4ef5afc4cd821389629a396a488bd5f6"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/ServiceAccountNodeAudienceRestriction.md"
---

---
title: ServiceAccountNodeAudienceRestriction
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: false
    fromVersion: "1.32"
    toVersion: "1.32"
  - stage: beta
    defaultValue: true
    fromVersion: "1.33"  

---
This gate is used to restrict the audience for which the kubelet can request a service account token for. 
