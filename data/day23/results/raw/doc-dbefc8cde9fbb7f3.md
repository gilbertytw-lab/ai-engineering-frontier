---
document_id: "doc-dbefc8cde9fbb7f3"
source_name: "reference/command-line-tools-reference/feature-gates/ConstrainedImpersonation.md"
source_type: "text"
source_format: "md"
source_sha256: "e5fb16511ee55d0b09be58b6401f5809586e3c2a531575c20bcee62433456bfe"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/ConstrainedImpersonation.md"
extracted_sha256: "e5fb16511ee55d0b09be58b6401f5809586e3c2a531575c20bcee62433456bfe"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/ConstrainedImpersonation.md"
---

---
title: ConstrainedImpersonation
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.35"
    toVersion: "1.35"
  - stage: beta
    defaultValue: true
    fromVersion: "1.36"
---
Enables impersonation that is constrained to specific requests instead of being all or nothing.
