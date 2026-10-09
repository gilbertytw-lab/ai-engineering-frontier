---
document_id: "doc-22c31eb1c8d848ec"
source_name: "reference/command-line-tools-reference/feature-gates/AllowParsingUserUIDFromCertAuth.md"
source_type: "text"
source_format: "md"
source_sha256: "ba25e3d9ece8280f244912a43e42edb451be039f02bee513175ade72360f7b9b"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/AllowParsingUserUIDFromCertAuth.md"
extracted_sha256: "ba25e3d9ece8280f244912a43e42edb451be039f02bee513175ade72360f7b9b"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/AllowParsingUserUIDFromCertAuth.md"
---

---
title: AllowParsingUserUIDFromCertAuth
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.33"
    toVersion: "1.33"
  - stage: beta
    defaultValue: true
    fromVersion: "1.34"

---
When this feature is enabled, the subject name attribute `1.3.6.1.4.1.57683.2`
in an X.509 certificate will be parsed as the user UID during certificate authentication.
