---
document_id: "doc-492dcac6646d7ee0"
source_name: "reference/glossary/pod-security-policy.md"
source_type: "text"
source_format: "md"
source_sha256: "fe6be36833dd323afcb50a8dfc88764d80e7cb0d52f2cab4787c73280364b563"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/pod-security-policy.md"
extracted_sha256: "fe6be36833dd323afcb50a8dfc88764d80e7cb0d52f2cab4787c73280364b563"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/pod-security-policy.md"
---

---
title: Pod Security Policy
id: pod-security-policy
full_link: /docs/concepts/security/pod-security-policy/
short_description: >
  Removed API that enforced Pod security restrictions.
aka: 
tags:
- security
---
A former Kubernetes API that enforced security restrictions during {{< glossary_tooltip term_id="pod" >}} creation and updates.

<!--more--> 

PodSecurityPolicy was deprecated as of Kubernetes v1.21, and removed in v1.25.
As an alternative, use [Pod Security Admission](/docs/concepts/security/pod-security-admission/) or a 3rd party admission plugin.
