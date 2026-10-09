---
document_id: "doc-2d5df58b3a909b2b"
source_name: "reference/command-line-tools-reference/feature-gates/KMSv2.md"
source_type: "text"
source_format: "md"
source_sha256: "5302a8b9826e670a73d57f6614ac795ee6ac38366e41bbe95b13166e6cd1d14a"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/KMSv2.md"
extracted_sha256: "5302a8b9826e670a73d57f6614ac795ee6ac38366e41bbe95b13166e6cd1d14a"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/KMSv2.md"
---

---
title: KMSv2
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.25"
    toVersion: "1.26"
  - stage: beta
    defaultValue: true
    fromVersion: "1.27"  
    toVersion: "1.28" 
  - stage: stable
    defaultValue: true
    fromVersion: "1.29"
    toVersion: "1.31"

removed: true
---
Enables KMS v2 API for encryption at rest. See
[Using a KMS Provider for data encryption](/docs/tasks/administer-cluster/kms-provider)
for more details.
