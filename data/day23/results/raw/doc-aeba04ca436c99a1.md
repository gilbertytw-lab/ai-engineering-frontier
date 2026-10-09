---
document_id: "doc-aeba04ca436c99a1"
source_name: "reference/glossary/service-account.md"
source_type: "text"
source_format: "md"
source_sha256: "8b8fc738efadc3e6e93c6390a0174805e1cf535b277ae1bdf67c608cad4eb47c"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/service-account.md"
extracted_sha256: "8b8fc738efadc3e6e93c6390a0174805e1cf535b277ae1bdf67c608cad4eb47c"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/service-account.md"
---

---
title: ServiceAccount
id: service-account
full_link: /docs/tasks/configure-pod-container/configure-service-account/
short_description: >
  Provides an identity for processes that run in a Pod.

aka: 
tags:
- fundamental
- core-object
---
 Provides an identity for processes that run in a {{< glossary_tooltip text="Pod" term_id="pod" >}}.

<!--more--> 

When processes inside Pods access the cluster, they are authenticated by the API server as a particular service account, for example, `default`. When you create a Pod, if you do not specify a service account, it is automatically assigned the default service account in the same {{< glossary_tooltip text="Namespace" term_id="namespace" >}}.
