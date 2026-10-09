---
document_id: "doc-b1c901bb29b97f2c"
source_name: "reference/kubernetes-api/definitions/local-object-reference-v1.md"
source_type: "text"
source_format: "md"
source_sha256: "07471c74df3fbf456887cc33f7b18a96ca6954fa9b27bfcf24d1b8edcefbd981"
source_snapshot: "data/day23/source/content/en/docs/reference/kubernetes-api/definitions/local-object-reference-v1.md"
extracted_sha256: "07471c74df3fbf456887cc33f7b18a96ca6954fa9b27bfcf24d1b8edcefbd981"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/kubernetes-api/definitions/local-object-reference-v1.md"
---

---
api_metadata:
  apiVersion: "v1"
  import: "k8s.io/api/core/v1"
  kind: "LocalObjectReference"
content_type: "api_reference"
description: "LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace."
title: "LocalObjectReference"
weight: 200
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


## LocalObjectReference {#LocalObjectReference}

LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code><br/><em>string</em></td>
      <td>Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names</td>
    </tr>
  </tbody>
</table>
