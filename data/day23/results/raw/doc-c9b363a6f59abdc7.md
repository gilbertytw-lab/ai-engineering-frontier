---
document_id: "doc-c9b363a6f59abdc7"
source_name: "reference/kubernetes-api/definitions/typed-local-object-reference-v1.md"
source_type: "text"
source_format: "md"
source_sha256: "b6588c87732925eb3ce9dd040267d30f1ee9690d6302bdfcb32b587c4e350fe9"
source_snapshot: "data/day23/source/content/en/docs/reference/kubernetes-api/definitions/typed-local-object-reference-v1.md"
extracted_sha256: "b6588c87732925eb3ce9dd040267d30f1ee9690d6302bdfcb32b587c4e350fe9"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/kubernetes-api/definitions/typed-local-object-reference-v1.md"
---

---
api_metadata:
  apiVersion: "v1"
  import: "k8s.io/api/core/v1"
  kind: "TypedLocalObjectReference"
content_type: "api_reference"
description: "TypedLocalObjectReference contains enough information to let you locate the typed referenced object inside the same namespace."
title: "TypedLocalObjectReference"
weight: 600
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

`apiVersion: v1`

`import "k8s.io/api/core/v1"`


## TypedLocalObjectReference {#TypedLocalObjectReference}

TypedLocalObjectReference contains enough information to let you locate the typed referenced object inside the same namespace.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiGroup</code><br/><em>string</em></td>
      <td>APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required.</td>
    </tr>
    <tr>
      <td><code>kind</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>Kind is the type of resource being referenced</td>
    </tr>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>Name is the name of resource being referenced</td>
    </tr>
  </tbody>
</table>
