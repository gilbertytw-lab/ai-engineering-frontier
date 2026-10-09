---
document_id: "doc-f0c540f38b2fece5"
source_name: "reference/command-line-tools-reference/feature-gates/CSIMigrationGCEComplete.md"
source_type: "text"
source_format: "md"
source_sha256: "c4382dde005211ec840fe546e36b481b593667b4a078d118ad9265c9c031e044"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/CSIMigrationGCEComplete.md"
extracted_sha256: "c4382dde005211ec840fe546e36b481b593667b4a078d118ad9265c9c031e044"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/CSIMigrationGCEComplete.md"
---

---
# Removed from Kubernetes
title: CSIMigrationGCEComplete
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
Stops registering the GCE-PD in-tree plugin in
kubelet and volume controllers and enables shims and translation logic to
route volume operations from the GCE-PD in-tree plugin to PD CSI plugin.
Requires CSIMigration and CSIMigrationGCE feature flags enabled and PD CSI
plugin installed and configured on all nodes in the cluster. This flag has
been deprecated in favor of the `InTreePluginGCEUnregister` feature flag which
prevents the registration of in-tree GCE PD plugin.
