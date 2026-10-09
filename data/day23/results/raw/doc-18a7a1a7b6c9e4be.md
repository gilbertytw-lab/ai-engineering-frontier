---
document_id: "doc-18a7a1a7b6c9e4be"
source_name: "reference/glossary/aggregation-layer.md"
source_type: "text"
source_format: "md"
source_sha256: "3138ae20c2153dd4f65d320ed5e6f9e5e9af7de8cc09a587d6fd40f9e0635cba"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/aggregation-layer.md"
extracted_sha256: "3138ae20c2153dd4f65d320ed5e6f9e5e9af7de8cc09a587d6fd40f9e0635cba"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/aggregation-layer.md"
---

---
title: Aggregation Layer
id: aggregation-layer
full_link: /docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/
short_description: >
  The aggregation layer lets you install additional Kubernetes-style APIs in your cluster.

aka: 
tags:
- architecture
- extension
- operation
---
 The aggregation layer lets you install additional Kubernetes-style APIs in your cluster.

<!--more-->

When you've configured the {{< glossary_tooltip text="Kubernetes API Server" term_id="kube-apiserver" >}} to [support additional APIs](/docs/tasks/extend-kubernetes/configure-aggregation-layer/), you can add `APIService` objects to "claim" a URL path in the Kubernetes API.
