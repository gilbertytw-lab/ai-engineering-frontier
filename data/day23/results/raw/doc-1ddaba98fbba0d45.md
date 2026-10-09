---
document_id: "doc-1ddaba98fbba0d45"
source_name: "reference/glossary/watch.md"
source_type: "text"
source_format: "md"
source_sha256: "1e038fe1a1db127b822aad09b90698694cf61b8585fc4d95d083c47182c5ecb0"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/watch.md"
extracted_sha256: "1e038fe1a1db127b822aad09b90698694cf61b8585fc4d95d083c47182c5ecb0"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/watch.md"
---

---
title: Watch
id: watch
full_link: /docs/reference/using-api/api-concepts/#api-verbs
short_description: >
  A verb that is used to track changes to an object in Kubernetes as a stream.

aka:
tags:
- API verb
- fundamental
---
A verb that is used to track changes to an object in Kubernetes as a stream.
It is used for the efficient detection of changes.

<!--more-->

A verb that is used to track changes to an object in Kubernetes as a stream. Watches allow
efficient detection of changes; for example, a
{{< glossary_tooltip term_id="controller" text="controller">}} that needs to know whenever a
ConfigMap has changed can use a watch rather than polling.

See [Efficient Detection of Changes in API Concepts](/docs/reference/using-api/api-concepts/#efficient-detection-of-changes) for more information.
