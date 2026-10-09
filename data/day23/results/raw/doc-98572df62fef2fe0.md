---
document_id: "doc-98572df62fef2fe0"
source_name: "reference/glossary/mixed-version-proxy.md"
source_type: "text"
source_format: "md"
source_sha256: "608e1b3fca41dc231f927424101126f90798cdd43ae6222f8da79dfe89ed6f8c"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/mixed-version-proxy.md"
extracted_sha256: "608e1b3fca41dc231f927424101126f90798cdd43ae6222f8da79dfe89ed6f8c"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/mixed-version-proxy.md"
---

---
title: Mixed Version Proxy (MVP)
id: mvp
full_link: /docs/concepts/architecture/mixed-version-proxy/
short_description: >
  Feature that lets a kube-apiserver proxy a resource request to a different peer API server. 
aka: ["MVP"]
tags:
- architecture
---
Feature to let a kube-apiserver proxy a resource request to a different peer API server.

<!--more-->

When a cluster has multiple API servers running different versions of Kubernetes, this
feature enables {{< glossary_tooltip text="resource" term_id="api-resource" >}}
requests to be served by the correct API server.

MVP is disabled by default and can be activated by enabling
the [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) named `UnknownVersionInteroperabilityProxy` when 
the {{< glossary_tooltip text="API Server" term_id="kube-apiserver" >}} is started.
