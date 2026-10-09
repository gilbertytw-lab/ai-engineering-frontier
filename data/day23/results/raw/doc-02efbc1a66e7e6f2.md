---
document_id: "doc-02efbc1a66e7e6f2"
source_name: "reference/kubernetes-api/definitions/non-resource-attributes-v1-authorization.md"
source_type: "text"
source_format: "md"
source_sha256: "5553d50995cdd755e121cf515d177157480288bfb4842e2c55eba391f119b7c5"
source_snapshot: "data/day23/source/content/en/docs/reference/kubernetes-api/definitions/non-resource-attributes-v1-authorization.md"
extracted_sha256: "5553d50995cdd755e121cf515d177157480288bfb4842e2c55eba391f119b7c5"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/kubernetes-api/definitions/non-resource-attributes-v1-authorization.md"
---

---
api_metadata:
  apiVersion: "authorization.k8s.io/v1"
  import: "k8s.io/api/authorization/v1"
  kind: "NonResourceAttributes"
content_type: "api_reference"
description: "NonResourceAttributes includes the authorization attributes available for non-resource requests to the Authorizer interface"
title: "NonResourceAttributes"
weight: 290
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

`apiVersion: authorization.k8s.io/v1`

`import "k8s.io/api/authorization/v1"`


## NonResourceAttributes {#NonResourceAttributes}

NonResourceAttributes includes the authorization attributes available for non-resource requests to the Authorizer interface

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>path</code><br/><em>string</em></td>
      <td>path is the URL path of the request</td>
    </tr>
    <tr>
      <td><code>verb</code><br/><em>string</em></td>
      <td>verb is the standard HTTP verb</td>
    </tr>
  </tbody>
</table>
