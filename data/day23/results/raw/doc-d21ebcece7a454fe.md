---
document_id: "doc-d21ebcece7a454fe"
source_name: "reference/command-line-tools-reference/feature-gates/APISelfSubjectReview.md"
source_type: "text"
source_format: "md"
source_sha256: "50266678adbc9c4ecd6e5fac7322a0f3b7917e91ed651b9a7d46b5fbf9822372"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/APISelfSubjectReview.md"
extracted_sha256: "50266678adbc9c4ecd6e5fac7322a0f3b7917e91ed651b9a7d46b5fbf9822372"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/APISelfSubjectReview.md"
---

---
# Removed from Kubernetes
title: APISelfSubjectReview
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.26"
    toVersion: "1.26"
  - stage: beta
    defaultValue: true
    fromVersion: "1.27"  
    toVersion: "1.27" 
  - stage: stable
    defaultValue: true
    fromVersion: "1.28"  
    toVersion: "1.29"
removed: true
---
Activate the `SelfSubjectReview` API which allows users
to see the requesting subject's authentication information.
See [API access to authentication information for a client](/docs/reference/access-authn-authz/authentication/#self-subject-review)
for more details.
