---
document_id: "doc-efc6bf63a22e7cc6"
source_name: "reference/command-line-tools-reference/feature-gates/StorageVersionAPI.md"
source_type: "text"
source_format: "md"
source_sha256: "decc95951c422fa2ed36b016fd31037df8f8a1fa28ba1c3ed84035d381b4ee3f"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/StorageVersionAPI.md"
extracted_sha256: "decc95951c422fa2ed36b016fd31037df8f8a1fa28ba1c3ed84035d381b4ee3f"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/StorageVersionAPI.md"
---

---
title: StorageVersionAPI
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.20"
---
Enable the
[storage version API](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#storageversion-v1alpha1-internal-apiserver-k8s-io).
