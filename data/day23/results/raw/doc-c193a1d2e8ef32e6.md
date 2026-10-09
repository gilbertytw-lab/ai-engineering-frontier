---
document_id: "doc-c193a1d2e8ef32e6"
source_name: "reference/command-line-tools-reference/feature-gates/CSIMigrationAzureDiskComplete.md"
source_type: "text"
source_format: "md"
source_sha256: "0a464a0c43d050ee84391d5fe782c4ee5154094e4b2e412c1329bb8a6132c17b"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/CSIMigrationAzureDiskComplete.md"
extracted_sha256: "0a464a0c43d050ee84391d5fe782c4ee5154094e4b2e412c1329bb8a6132c17b"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/CSIMigrationAzureDiskComplete.md"
---

---
# Removed from Kubernetes
title: CSIMigrationAzureDiskComplete
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.17"
    toVersion: "1.20"
  - stage: deprecated
    fromVersion: "1.21"
    toVersion: "1.21"

removed: true
---
Stops registering the Azure-Disk in-tree
plugin in kubelet and volume controllers and enables shims and translation
logic to route volume operations from the Azure-Disk in-tree plugin to
AzureDisk CSI plugin. Requires CSIMigration and CSIMigrationAzureDisk feature
flags enabled and AzureDisk CSI plugin installed and configured on all nodes
in the cluster. This flag has been deprecated in favor of the
`InTreePluginAzureDiskUnregister` feature flag which prevents the registration
of in-tree AzureDisk plugin.
