---
document_id: "doc-aace4dbfdb70154b"
source_name: "reference/glossary/dockershim.md"
source_type: "text"
source_format: "md"
source_sha256: "efe463ad0f020c6af02cc4e8fc14a3a8a5eb64e07d312d451dc8b029e300b516"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/dockershim.md"
extracted_sha256: "efe463ad0f020c6af02cc4e8fc14a3a8a5eb64e07d312d451dc8b029e300b516"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/dockershim.md"
---

---
title: Dockershim
id: dockershim
full_link: /dockershim
short_description: >
   A component of Kubernetes v1.23 and earlier, which allows Kubernetes system components to communicate with Docker Engine.

aka:
tags:
- fundamental
---
The dockershim is a component of Kubernetes version 1.23 and earlier. It allows the {{< glossary_tooltip text="kubelet" term_id="kubelet" >}}
to communicate with {{< glossary_tooltip text="Docker Engine" term_id="docker" >}}.

<!--more-->

Starting with version 1.24, dockershim has been removed from Kubernetes. For more information, see [Dockershim FAQ](/dockershim).
