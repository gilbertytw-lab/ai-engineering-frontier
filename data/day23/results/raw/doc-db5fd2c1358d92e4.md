---
document_id: "doc-db5fd2c1358d92e4"
source_name: "reference/command-line-tools-reference/feature-gates/AdmissionWebhookMatchConditions.md"
source_type: "text"
source_format: "md"
source_sha256: "fc7001afc5df02fc0d48c303c56c765196e466a9c4ba1388a7a78e15be907231"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/AdmissionWebhookMatchConditions.md"
extracted_sha256: "fc7001afc5df02fc0d48c303c56c765196e466a9c4ba1388a7a78e15be907231"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/AdmissionWebhookMatchConditions.md"
---

---
title: AdmissionWebhookMatchConditions
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.27"
    toVersion: "1.27"
  - stage: beta
    defaultValue: true
    fromVersion: "1.28"
    toVersion: "1.29"
  - stage: stable
    defaultValue: true
    fromVersion: "1.30"
    toVersion: "1.32"

removed: true
---
Enable [match conditions](/docs/reference/access-authn-authz/extensible-admission-controllers/#matching-requests-matchconditions)
on mutating & validating admission webhooks.
