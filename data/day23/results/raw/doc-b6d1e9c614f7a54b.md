---
document_id: "doc-b6d1e9c614f7a54b"
source_name: "reference/command-line-tools-reference/feature-gates/DisableCloudProviders.md"
source_type: "text"
source_format: "md"
source_sha256: "8a3530c8f7afd8fea3ee7247099e542625c57509c0b852c3ada6fb887b729a43"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/DisableCloudProviders.md"
extracted_sha256: "8a3530c8f7afd8fea3ee7247099e542625c57509c0b852c3ada6fb887b729a43"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/DisableCloudProviders.md"
---

---
title: DisableCloudProviders
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.22"
    toVersion: "1.28"
  - stage: beta
    defaultValue: true
    fromVersion: "1.29"
    toVersion: "1.30"
  - stage: stable
    defaultValue: true
    fromVersion: "1.31"
    toVersion: "1.32"

removed: true
---
Enabling this feature gate deactivated functionality in `kube-apiserver`,
`kube-controller-manager` and `kubelet` that related to the `--cloud-provider`
command line argument.

In Kubernetes v1.31 and later, the only valid values for `--cloud-provider`
are the empty string (no cloud provider integration), or "external"
(integration via a separate cloud-controller-manager).
