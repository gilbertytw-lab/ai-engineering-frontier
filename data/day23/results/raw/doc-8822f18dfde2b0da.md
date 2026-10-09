---
document_id: "doc-8822f18dfde2b0da"
source_name: "reference/kubernetes-api/definitions/non-resource-rule-v1-authorization.md"
source_type: "text"
source_format: "md"
source_sha256: "dcb8b28f943cc9f5daf63cf2c2c6e9a47a770114e6a22af3c5f7b20c7b30d424"
source_snapshot: "data/day23/source/content/en/docs/reference/kubernetes-api/definitions/non-resource-rule-v1-authorization.md"
extracted_sha256: "dcb8b28f943cc9f5daf63cf2c2c6e9a47a770114e6a22af3c5f7b20c7b30d424"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/kubernetes-api/definitions/non-resource-rule-v1-authorization.md"
---

---
api_metadata:
  apiVersion: "authorization.k8s.io/v1"
  import: "k8s.io/api/authorization/v1"
  kind: "NonResourceRule"
content_type: "api_reference"
description: "NonResourceRule holds information that describes a rule for the non-resource"
title: "NonResourceRule"
weight: 300
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


## NonResourceRule {#NonResourceRule}

NonResourceRule holds information that describes a rule for the non-resource

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>nonResourceURLs</code><br/><em>string array</em></td>
      <td>nonResourceURLs is a set of partial urls that a user should have access to.  *s are allowed, but only as the full, final step in the path.  "*" means all.</td>
    </tr>
    <tr>
      <td><code>verbs</code>&nbsp;<strong>*</strong><br/><em>string array</em></td>
      <td>verbs is a list of kubernetes non-resource API verbs, like: get, post, put, delete, patch, head, options.  "*" means all.</td>
    </tr>
  </tbody>
</table>
