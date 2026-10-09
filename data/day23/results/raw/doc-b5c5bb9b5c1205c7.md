---
document_id: "doc-b5c5bb9b5c1205c7"
source_name: "reference/kubernetes-api/definitions/typed-local-object-reference-v1beta1-scheduling.md"
source_type: "text"
source_format: "md"
source_sha256: "a70b55b253aa7b7110102ac0e18b75e4b805e072d62c66fbcca51d05d7d68c8a"
source_snapshot: "data/day23/source/content/en/docs/reference/kubernetes-api/definitions/typed-local-object-reference-v1beta1-scheduling.md"
extracted_sha256: "a70b55b253aa7b7110102ac0e18b75e4b805e072d62c66fbcca51d05d7d68c8a"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/kubernetes-api/definitions/typed-local-object-reference-v1beta1-scheduling.md"
---

---
api_metadata:
  apiVersion: "scheduling.k8s.io/v1beta1"
  import: "k8s.io/api/scheduling/v1beta1"
  kind: "TypedLocalObjectReference"
content_type: "api_reference"
description: "TypedLocalObjectReference allows to reference typed object inside the same namespace."
title: "TypedLocalObjectReference"
weight: 610
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

`apiVersion: scheduling.k8s.io/v1beta1`

`import "k8s.io/api/scheduling/v1beta1"`


## TypedLocalObjectReference {#TypedLocalObjectReference}

TypedLocalObjectReference allows to reference typed object inside the same namespace.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiGroup</code><br/><em>string</em></td>
      <td>apiGroup is the group for the resource being referenced. If apiGroup is empty, the specified Kind must be in the core API group. For any other third-party types, setting apiGroup is required. It must be a DNS subdomain.</td>
    </tr>
    <tr>
      <td><code>kind</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>kind is the type of resource being referenced. It must be a path segment name.</td>
    </tr>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>name is the name of resource being referenced. It must be a path segment name.</td>
    </tr>
  </tbody>
</table>
