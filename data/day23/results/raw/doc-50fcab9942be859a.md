---
document_id: "doc-50fcab9942be859a"
source_name: "reference/command-line-tools-reference/feature-gates/AppArmorFields.md"
source_type: "text"
source_format: "md"
source_sha256: "9dee5c59084124c25b96b00ebf2d0fb6c579bbeb2886a7b78554c152970b84ac"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/AppArmorFields.md"
extracted_sha256: "9dee5c59084124c25b96b00ebf2d0fb6c579bbeb2886a7b78554c152970b84ac"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/AppArmorFields.md"
---

---
title: AppArmorFields
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.30"
    toVersion: "1.30"
  - stage: stable
    defaultValue: true
    fromVersion: "1.31"
    toVersion: "1.32"

removed: true
---
Enable AppArmor related security context settings.

For more information about AppArmor and Kubernetes, read the
[AppArmor](/docs/concepts/security/linux-kernel-security-constraints/#apparmor) section
within
[security features in the Linux kernel](/docs/concepts/security/linux-kernel-security-constraints/#linux-security-features).
