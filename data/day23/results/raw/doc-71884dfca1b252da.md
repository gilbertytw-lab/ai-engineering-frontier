---
document_id: "doc-71884dfca1b252da"
source_name: "reference/kubernetes-api/definitions/event-source-v1.md"
source_type: "text"
source_format: "md"
source_sha256: "8669ebf935e39888e7d9b1efbe1260802a90c8692effe32bd4b828c7483cca88"
source_snapshot: "data/day23/source/content/en/docs/reference/kubernetes-api/definitions/event-source-v1.md"
extracted_sha256: "8669ebf935e39888e7d9b1efbe1260802a90c8692effe32bd4b828c7483cca88"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/kubernetes-api/definitions/event-source-v1.md"
---

---
api_metadata:
  apiVersion: "v1"
  import: "k8s.io/api/core/v1"
  kind: "EventSource"
content_type: "api_reference"
description: "EventSource contains information for an event."
title: "EventSource"
weight: 90
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


## EventSource {#EventSource}

EventSource contains information for an event.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>component</code><br/><em>string</em></td>
      <td>Component from which the event is generated.</td>
    </tr>
    <tr>
      <td><code>host</code><br/><em>string</em></td>
      <td>Node name on which the event is generated.</td>
    </tr>
  </tbody>
</table>
