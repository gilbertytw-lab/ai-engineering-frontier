---
document_id: "doc-6ef0c5865fc0e24b"
source_name: "reference/command-line-tools-reference/feature-gates/WindowsRunAsUserName.md"
source_type: "text"
source_format: "md"
source_sha256: "2f62607cbfcea3b69df5a9bfc93717aba8b6eac0a773f5b0371cc1ad15e1896c"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/WindowsRunAsUserName.md"
extracted_sha256: "2f62607cbfcea3b69df5a9bfc93717aba8b6eac0a773f5b0371cc1ad15e1896c"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/WindowsRunAsUserName.md"
---

---
# Removed from Kubernetes
title: WindowsRunAsUserName
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.16"
    toVersion: "1.16"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.17"
    toVersion: "1.17"
  - stage: stable
    defaultValue: true
    fromVersion: "1.18"
    toVersion: "1.20"

removed: true
---
Enable support for running applications in Windows containers with as a
non-default user. See [Configuring RunAsUserName](/docs/tasks/configure-pod-container/configure-runasusername)
for more details.
