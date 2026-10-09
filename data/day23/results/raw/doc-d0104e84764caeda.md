---
document_id: "doc-d0104e84764caeda"
source_name: "reference/glossary/preemption.md"
source_type: "text"
source_format: "md"
source_sha256: "659c651f8afbe6006c2895e5cb56fcb22e407f3d547b5891a7e4845c2d5a9b72"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/preemption.md"
extracted_sha256: "659c651f8afbe6006c2895e5cb56fcb22e407f3d547b5891a7e4845c2d5a9b72"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/preemption.md"
---

---
title: Preemption
id: preemption
full_link: /docs/concepts/scheduling-eviction/pod-priority-preemption/#preemption
short_description: >
  Preemption logic in Kubernetes helps a pending Pod to find a suitable Node by evicting low priority Pods existing on that Node.

aka:
tags:
- operation
---
 Preemption logic in Kubernetes helps a pending {{< glossary_tooltip term_id="pod" >}} to find a suitable {{< glossary_tooltip term_id="node" >}} by evicting low priority Pods existing on that Node.

<!--more-->

If a Pod cannot be scheduled, the scheduler tries to [preempt](/docs/concepts/scheduling-eviction/pod-priority-preemption/#preemption) lower priority Pods to make scheduling of the pending Pod possible.
