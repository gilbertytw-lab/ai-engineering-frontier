---
document_id: "doc-dd44acae0d8e00e0"
source_name: "reference/glossary/secret.md"
source_type: "text"
source_format: "md"
source_sha256: "b6a52c816856d78c6d31b12a61315de566d9c6a33dd4ef4b97ce19e9ef24b57b"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/secret.md"
extracted_sha256: "b6a52c816856d78c6d31b12a61315de566d9c6a33dd4ef4b97ce19e9ef24b57b"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/secret.md"
---

---
title: Secret
id: secret
full_link: /docs/concepts/configuration/secret/
short_description: >
  Stores sensitive information, such as passwords, OAuth tokens, and ssh keys.

aka:
tags:
- core-object
- security
---
 Stores sensitive information, such as passwords, OAuth tokens, and SSH keys.

<!--more-->

Secrets give you more control over how sensitive information is used and reduces
the risk of accidental exposure. Secret values are encoded as base64 strings and
are stored unencrypted by default, but can be configured to be
[encrypted at rest](/docs/tasks/administer-cluster/encrypt-data/#ensure-all-secrets-are-encrypted).

A {{< glossary_tooltip text="Pod" term_id="pod" >}} can reference the Secret in
a variety of ways, such as in a volume mount or as an environment variable.
Secrets are designed for confidential data and
[ConfigMaps](/docs/tasks/configure-pod-container/configure-pod-configmap/) are
designed for non-confidential data.
