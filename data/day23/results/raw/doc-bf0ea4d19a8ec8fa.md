---
document_id: "doc-bf0ea4d19a8ec8fa"
source_name: "reference/command-line-tools-reference/feature-gates/CloudControllerManagerWatchBasedRoutesReconciliation.md"
source_type: "text"
source_format: "md"
source_sha256: "614cbc6ffadc9dd4df99263b69252e5ddc6b6d267d3ac8a5b6f8744bac75c22a"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/CloudControllerManagerWatchBasedRoutesReconciliation.md"
extracted_sha256: "614cbc6ffadc9dd4df99263b69252e5ddc6b6d267d3ac8a5b6f8744bac75c22a"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/CloudControllerManagerWatchBasedRoutesReconciliation.md"
---

---
title: CloudControllerManagerWatchBasedRoutesReconciliation
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.35"
---
Enables a watch-based route reconciliation mechanism (rather than reconciling at a fixed interval)
within the cloud-controller-manager library.
