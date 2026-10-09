---
document_id: "doc-5dcfdb3fade3c1bf"
source_name: "reference/command-line-tools-reference/feature-gates/KMSv2KDF.md"
source_type: "text"
source_format: "md"
source_sha256: "987c535300b62f9c923a56d891812c77a667b1924a9e23b0c142f90153e7df32"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/KMSv2KDF.md"
extracted_sha256: "987c535300b62f9c923a56d891812c77a667b1924a9e23b0c142f90153e7df32"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/KMSv2KDF.md"
---

---
title: KMSv2KDF
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: false
    fromVersion: "1.28"  
    toVersion: "1.28"
  - stage: stable
    defaultValue: true
    fromVersion: "1.29"
    toVersion: "1.31"

removed: true
---
Enables KMS v2 to generate single use data encryption keys.
See [Using a KMS Provider for data encryption](/docs/tasks/administer-cluster/kms-provider) for more details.
If the `KMSv2` feature gate is not enabled in your cluster, the value of the `KMSv2KDF` feature gate has no effect.
