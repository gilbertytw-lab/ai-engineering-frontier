---
document_id: "doc-0e75b8d8ef5be410"
source_name: "reference/glossary/node-pressure-eviction.md"
source_type: "text"
source_format: "md"
source_sha256: "9b89c64100d30a3d321a7db5c0e0b743bdef8c980d46f399f4a9ac5258b0dab7"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/node-pressure-eviction.md"
extracted_sha256: "9b89c64100d30a3d321a7db5c0e0b743bdef8c980d46f399f4a9ac5258b0dab7"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/node-pressure-eviction.md"
---

---
title: Node-pressure eviction
id: node-pressure-eviction
full_link: /docs/concepts/scheduling-eviction/node-pressure-eviction/
short_description: >
  Node-pressure eviction is the process by which the kubelet proactively fails
  pods to reclaim resources on nodes.
aka:
- kubelet eviction
tags:
- operation
---
Node-pressure eviction is the process by which the {{<glossary_tooltip term_id="kubelet" text="kubelet">}} proactively terminates
pods to reclaim {{< glossary_tooltip text="resource" term_id="infrastructure-resource" >}}
on nodes.

<!--more-->

The kubelet monitors resources like CPU, memory, disk space, and filesystem 
inodes on your cluster's nodes. When one or more of these resources reach
specific consumption levels, the kubelet can proactively fail one or more pods
on the node to reclaim resources and prevent starvation. 

Node-pressure eviction is not the same as [API-initiated eviction](/docs/concepts/scheduling-eviction/api-eviction/).
