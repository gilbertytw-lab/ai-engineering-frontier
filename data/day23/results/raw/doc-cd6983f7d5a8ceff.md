---
document_id: "doc-cd6983f7d5a8ceff"
source_name: "reference/glossary/daemonset.md"
source_type: "text"
source_format: "md"
source_sha256: "7e5deb2d7892b31becee07d644e5ce7da9569920cc8a0da81d8d629902b0f203"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/daemonset.md"
extracted_sha256: "7e5deb2d7892b31becee07d644e5ce7da9569920cc8a0da81d8d629902b0f203"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/daemonset.md"
---

---
title: DaemonSet
id: daemonset
full_link: /docs/concepts/workloads/controllers/daemonset
short_description: >
  Ensures a copy of a Pod is running across a set of nodes in a cluster.

aka: 
tags:
- fundamental
- core-object
- workload
---
 Ensures a copy of a {{< glossary_tooltip text="Pod" term_id="pod" >}} is running across a set of nodes in a {{< glossary_tooltip text="cluster" term_id="cluster" >}}.

<!--more--> 

Used to deploy system daemons such as log collectors and monitoring agents that typically must run on every {{< glossary_tooltip term_id="node" >}}.
