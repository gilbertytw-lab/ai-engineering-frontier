---
document_id: "doc-1bbfefd112e72a58"
source_name: "reference/command-line-tools-reference/feature-gates/DisableAllocatorDualWrite.md"
source_type: "text"
source_format: "md"
source_sha256: "c33eecb91e0fccb2cbef328289ddeeb4ab00eaf69a57bf5ac44fc9b5269dad34"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/DisableAllocatorDualWrite.md"
extracted_sha256: "c33eecb91e0fccb2cbef328289ddeeb4ab00eaf69a57bf5ac44fc9b5269dad34"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/DisableAllocatorDualWrite.md"
---

---
title: DisableAllocatorDualWrite
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.31"
    toVersion: "1.32"
  - stage: beta
    defaultValue: false
    fromVersion: "1.33"
    toVersion: "1.33"
  - stage: stable
    defaultValue: true
    fromVersion: "1.34"

---
You can enable the `MultiCIDRServiceAllocator` feature gate. The API server supports migration
from the old bitmap ClusterIP allocators to the new IPAddress allocators.

The API server performs a dual-write on both allocators. This feature gate disables the dual write
on the new Cluster IP allocators; you can enable this feature gate if you have completed the
relevant stage of the migration.
