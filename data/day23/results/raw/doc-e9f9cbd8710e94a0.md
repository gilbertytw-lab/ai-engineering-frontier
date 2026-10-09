---
document_id: "doc-e9f9cbd8710e94a0"
source_name: "reference/kubernetes-api/definitions/fields-v1-v1-meta.md"
source_type: "text"
source_format: "md"
source_sha256: "6cd7323aee6625af5183b8af358a8125d9b2b02a63d02cfa80c2167ca27b0ada"
source_snapshot: "data/day23/source/content/en/docs/reference/kubernetes-api/definitions/fields-v1-v1-meta.md"
extracted_sha256: "6cd7323aee6625af5183b8af358a8125d9b2b02a63d02cfa80c2167ca27b0ada"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/kubernetes-api/definitions/fields-v1-v1-meta.md"
---

---
api_metadata:
  apiVersion: "meta/v1"
  import: "k8s.io/apimachinery/pkg/apis/meta/v1"
  kind: "FieldsV1"
content_type: "api_reference"
description: "FieldsV1 stores a set of fields in a data structure like a Trie, in JSON format.\n\nEach key is either a &#39;.&#39; representing the field itself, and will always map to an empty set, or a string representing a sub-field or item. The string will follow one of these four formats: &#39;f:&lt;name&gt;&#39;, where &lt;name&gt; is the name of a field in a struct, or key in a map &#39;v:&lt;value&gt;&#39;, where &lt;value&gt; is the exact json formatted value of a list item &#39;i:&lt;index&gt;&#39;, where &lt;index&gt; is position of a item in a list &#39;k:&lt;keys&gt;&#39;, where &lt;keys&gt; is a map of  a list item&#39;s key fields to their unique values If a key maps to an empty Fields value, the field that key represents is part of the set.\n\nThe exact format is defined in sigs.k8s.io/structured-merge-diff"
title: "FieldsV1"
weight: 130
auto_generated: true
---

<!--
The file is auto-generated from the Go source code of the component using a generic
[generator](https://github.com/kubernetes-sigs/reference-docs/). To learn how
to generate the reference documentation, please read
[Contributing to the reference documentation](/docs/contribute/generate-ref-docs/).
To update the reference content, please follow the
[Contributing upstream](/docs/contribute/generate-ref-docs/contribute-upstream/)
guide. You can file document formatting bugs against the
[reference-docs](https://github.com/kubernetes-sigs/reference-docs/) project.
-->

`apiVersion: meta/v1`

`import "k8s.io/apimachinery/pkg/apis/meta/v1"`


## FieldsV1 {#FieldsV1}

FieldsV1 stores a set of fields in a data structure like a Trie, in JSON format.

Each key is either a &#39;.&#39; representing the field itself, and will always map to an empty set, or a string representing a sub-field or item. The string will follow one of these four formats: &#39;f:&lt;name&gt;&#39;, where &lt;name&gt; is the name of a field in a struct, or key in a map &#39;v:&lt;value&gt;&#39;, where &lt;value&gt; is the exact json formatted value of a list item &#39;i:&lt;index&gt;&#39;, where &lt;index&gt; is position of a item in a list &#39;k:&lt;keys&gt;&#39;, where &lt;keys&gt; is a map of  a list item&#39;s key fields to their unique values If a key maps to an empty Fields value, the field that key represents is part of the set.

The exact format is defined in sigs.k8s.io/structured-merge-diff

<hr>
