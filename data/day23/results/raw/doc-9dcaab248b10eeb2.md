---
document_id: "doc-9dcaab248b10eeb2"
source_name: "reference/command-line-tools-reference/feature-gates/RetryGenerateName.md"
source_type: "text"
source_format: "md"
source_sha256: "728bb1f18e3cbc7fe6b593790d7654175497f8ad9e03b083e44422b41658e6df"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/RetryGenerateName.md"
extracted_sha256: "728bb1f18e3cbc7fe6b593790d7654175497f8ad9e03b083e44422b41658e6df"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/RetryGenerateName.md"
---

---
title: RetryGenerateName
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.30"
    toVersion: "1.30"
  - stage: beta
    defaultValue: true
    fromVersion: "1.31"
    toVersion: "1.31"
  - stage: stable
    defaultValue: true
    fromVersion: "1.32"
---
Enables retrying of object creation when the
{{< glossary_tooltip text="API server" term_id="kube-apiserver" >}}
is expected to generate a [name](/docs/concepts/overview/working-with-objects/names/#names).

When this feature is enabled, requests using `generateName` are retried automatically in case the
control plane detects a name conflict with an existing object, up to a limit of 8 total attempts.
