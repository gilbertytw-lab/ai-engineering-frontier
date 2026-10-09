---
document_id: "doc-e8fd10f8d1e0ca64"
source_name: "reference/glossary/api-group.md"
source_type: "text"
source_format: "md"
source_sha256: "2fd49f11021094cae1222a3212958891b264be11fc90e3eeb683552925ddb834"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/api-group.md"
extracted_sha256: "2fd49f11021094cae1222a3212958891b264be11fc90e3eeb683552925ddb834"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/api-group.md"
---

---
title: API Group
id: api-group
full_link: /docs/concepts/overview/kubernetes-api/#api-groups-and-versioning
short_description: >
  A set of related paths in the Kubernetes API.

aka:
tags:
- fundamental
- architecture
---
A set of related paths in Kubernetes API.

<!--more-->

You can enable or disable each API group by changing the configuration of your API server. You can also disable or enable paths to specific
{{< glossary_tooltip text="resources" term_id="api-resource" >}}. An API group makes it easier to extend the Kubernetes API.
The API group is specified in a REST path and in the `apiVersion` field of a serialized {{< glossary_tooltip text="object" term_id="object" >}}.

* Read [API Group](/docs/concepts/overview/kubernetes-api/#api-groups-and-versioning) for more information.
