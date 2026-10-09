---
document_id: "doc-06a5af3b23c53b9c"
source_name: "reference/command-line-tools-reference/feature-gates/ExcludeAdmissionWebhookVirtualResources.md"
source_type: "text"
source_format: "md"
source_sha256: "1c9d86109529aabf25e48d3fea437925b5437eaab4cde7d82db9e1c5a5cb5929"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/ExcludeAdmissionWebhookVirtualResources.md"
extracted_sha256: "1c9d86109529aabf25e48d3fea437925b5437eaab4cde7d82db9e1c5a5cb5929"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/ExcludeAdmissionWebhookVirtualResources.md"
---

---
title: ExcludeAdmissionWebhookVirtualResources
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.37"
---
Exclude non-persisted (virtual) authentication and authorization resources,
such as `TokenReview` and `SubjectAccessReview`, from admission webhooks.
This matches the set of resources that ValidatingAdmissionPolicy and
MutatingAdmissionPolicy already exclude, and prevents a misbehaving webhook
from blocking the cluster's own authentication and authorization requests.
Disable this feature gate to restore the previous behavior of dispatching
admission webhooks for these resources.
