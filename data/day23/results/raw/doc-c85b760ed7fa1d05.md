---
document_id: "doc-c85b760ed7fa1d05"
source_name: "reference/glossary/endpoint-slice.md"
source_type: "text"
source_format: "md"
source_sha256: "a7fe967de150e734fd4fface36de1e57a07d5a9f7dcae5afaf184055b98bc808"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/endpoint-slice.md"
extracted_sha256: "a7fe967de150e734fd4fface36de1e57a07d5a9f7dcae5afaf184055b98bc808"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/endpoint-slice.md"
---

---
title: EndpointSlice
id: endpoint-slice
full_link: /docs/concepts/services-networking/endpoint-slices/
short_description: >
  EndpointSlices track the IP addresses of Pods for Services.

aka:
tags:
- networking
---
EndpointSlices track the IP addresses of backend endpoints.
EndpointSlices are normally associated with a
{{< glossary_tooltip text="Service" term_id="service" >}} and the backend endpoints typically represent
{{< glossary_tooltip text="Pods" term_id="pod" >}}.

<!--more-->
One Service can be backed by multiple Pods. Kubernetes represents the backing endpoints of a Service
with a set of EndpointSlices that are associated with that Service.
The backing endpoints are usually, but not always, pods running in the cluster.

The control plane usually manages EndpointSlices for you automatically. However,
EndpointSlices can be defined manually for {{< glossary_tooltip text="Services" term_id="service" >}} without
{{< glossary_tooltip text="selectors" term_id="selector" >}} specified.
