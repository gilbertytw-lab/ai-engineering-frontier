---
document_id: "doc-a8de6a890945a7df"
source_name: "reference/glossary/cel.md"
source_type: "text"
source_format: "md"
source_sha256: "a244706bc04d9b39aa8057285e8f6f0057d4db22034a2219a4ec908d7138a1c9"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/cel.md"
extracted_sha256: "a244706bc04d9b39aa8057285e8f6f0057d4db22034a2219a4ec908d7138a1c9"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/cel.md"
---

---
title: Common Expression Language
id: cel
full_link: https://cel.dev
short_description: >
  An expression language that's designed to be safe for executing user code.
tags:
- extension
- fundamental
aka:
- CEL
---
 A general-purpose expression language that's designed to be fast, portable, and
safe to execute.

<!--more-->

In Kubernetes, CEL can be used to run queries and perform fine-grained
filtering. For example, you can use CEL expressions with
[dynamic admission control](/docs/reference/access-authn-authz/extensible-admission-controllers/)
to filter for specific fields in requests, and with
[dynamic resource allocation (DRA)](/docs/concepts/resource-management/dynamic-resource-allocation/)
to select resources based on specific attributes.
