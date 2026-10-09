---
document_id: "doc-8fb46e3c7e575da5"
source_name: "reference/command-line-tools-reference/feature-gates/CSIMigrationRBD.md"
source_type: "text"
source_format: "md"
source_sha256: "1dfef01ce9da993a2db4abfbbd8b171867352a27d51bae89fadd6de1aceedf57"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/CSIMigrationRBD.md"
extracted_sha256: "1dfef01ce9da993a2db4abfbbd8b171867352a27d51bae89fadd6de1aceedf57"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/CSIMigrationRBD.md"
---

---
title: CSIMigrationRBD
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.23"
    toVersion: "1.27"
  - stage: deprecated
    defaultValue: false
    fromVersion: "1.28"
    toVersion: "1.30"

removed: true
---
Enables shims and translation logic to route volume
operations from the RBD in-tree plugin to Ceph RBD CSI plugin. Requires
CSIMigration and csiMigrationRBD feature flags enabled and Ceph CSI plugin
installed and configured in the cluster.

This feature gate was deprecated in favor of the `InTreePluginRBDUnregister` feature gate,
which prevents the registration of in-tree RBD plugin.
