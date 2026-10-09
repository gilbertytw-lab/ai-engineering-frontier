---
document_id: "doc-ef2414fee51eac31"
source_name: "reference/command-line-tools-reference/feature-gates/LegacyServiceAccountTokenNoAutoGeneration.md"
source_type: "text"
source_format: "md"
source_sha256: "81519b171e2a8aba567290d91734aef65df5e3481f02c6bc4cad11acf23abdd8"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/LegacyServiceAccountTokenNoAutoGeneration.md"
extracted_sha256: "81519b171e2a8aba567290d91734aef65df5e3481f02c6bc4cad11acf23abdd8"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/LegacyServiceAccountTokenNoAutoGeneration.md"
---

---
title: LegacyServiceAccountTokenNoAutoGeneration
content_type: feature_gate
_build:
  list: never
  render: false

stages:
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
Stop auto-generation of Secret-based
[service account tokens](/docs/concepts/security/service-accounts/#get-a-token).
