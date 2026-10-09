---
document_id: "doc-70bef5a3e2f55c7d"
source_name: "reference/command-line-tools-reference/feature-gates/LocalStorageCapacityIsolationFSQuotaMonitoring.md"
source_type: "text"
source_format: "md"
source_sha256: "af40f50c5b95661b66c91a1564d0e783d0b2721033d06ac8b860297c901826c4"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/LocalStorageCapacityIsolationFSQuotaMonitoring.md"
extracted_sha256: "af40f50c5b95661b66c91a1564d0e783d0b2721033d06ac8b860297c901826c4"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/LocalStorageCapacityIsolationFSQuotaMonitoring.md"
---

---
title: LocalStorageCapacityIsolationFSQuotaMonitoring
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.15"
    toVersion: "1.30"
  - stage: beta 
    defaultValue: false
    fromVersion: "1.31"
---
When `LocalStorageCapacityIsolation` 
is enabled for 
[local ephemeral storage](/docs/concepts/configuration/manage-resources-containers/), 
the backing filesystem for [emptyDir volumes](/docs/concepts/storage/volumes/#emptydir) supports project quotas,
and `UserNamespacesSupport` is enabled, 
project quotas are used to monitor `emptyDir` volume storage consumption rather than using filesystem walk, ensuring better performance and accuracy.
