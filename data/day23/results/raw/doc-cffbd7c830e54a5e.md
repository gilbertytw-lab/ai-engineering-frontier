---
document_id: "doc-cffbd7c830e54a5e"
source_name: "reference/glossary/volume.md"
source_type: "text"
source_format: "md"
source_sha256: "8a5e80a6b6e01fec4eb45bb0e7d9662c571b316aaa1074013549a5e0a7c9ca29"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/volume.md"
extracted_sha256: "8a5e80a6b6e01fec4eb45bb0e7d9662c571b316aaa1074013549a5e0a7c9ca29"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/volume.md"
---

---
title: Volume
id: volume
full_link: /docs/concepts/storage/volumes/
short_description: >
  A directory containing data, accessible to the containers in a pod.

aka:
tags:
- fundamental
---
 A directory containing data, accessible to the {{< glossary_tooltip text="containers" term_id="container" >}} in a {{< glossary_tooltip term_id="pod" >}}.

<!--more-->

A Kubernetes volume lives as long as the Pod that encloses it. Consequently, a volume outlives any containers that run within the Pod, and data in the volume is preserved across container restarts.

See [storage](/docs/concepts/storage/) for more information.
