---
document_id: "doc-66b1dd1e7bdb504f"
source_name: "reference/kubernetes-api/definitions/time-v1-meta.md"
source_type: "text"
source_format: "md"
source_sha256: "f83729f37f71373f4013a4b82b807b0108a75fd294ef607ff6c1352a7c3451f8"
source_snapshot: "data/day23/source/content/en/docs/reference/kubernetes-api/definitions/time-v1-meta.md"
extracted_sha256: "f83729f37f71373f4013a4b82b807b0108a75fd294ef607ff6c1352a7c3451f8"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/kubernetes-api/definitions/time-v1-meta.md"
---

---
api_metadata:
  apiVersion: "meta/v1"
  import: "k8s.io/apimachinery/pkg/apis/meta/v1"
  kind: "Time"
content_type: "api_reference"
description: "Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers."
title: "Time"
weight: 570
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


## Time {#Time}

Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers.

<hr>
