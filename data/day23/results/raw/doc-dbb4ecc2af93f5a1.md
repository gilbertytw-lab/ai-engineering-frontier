---
document_id: "doc-dbb4ecc2af93f5a1"
source_name: "reference/glossary/pod-priority.md"
source_type: "text"
source_format: "md"
source_sha256: "f7294061a9a2a871f89ba288209706fe21cafb6639d6121b8ce8827a128cb037"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/pod-priority.md"
extracted_sha256: "f7294061a9a2a871f89ba288209706fe21cafb6639d6121b8ce8827a128cb037"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/pod-priority.md"
---

---
title: Pod Priority
id: pod-priority
full_link: /docs/concepts/scheduling-eviction/pod-priority-preemption/#pod-priority
short_description: >
  Pod Priority indicates the importance of a Pod relative to other Pods.

aka:
tags:
- operation
---
 Pod Priority indicates the importance of a {{< glossary_tooltip term_id="pod" >}} relative to other Pods.

<!--more-->

[Pod Priority](/docs/concepts/scheduling-eviction/pod-priority-preemption/#pod-priority) gives the ability to set scheduling priority of a Pod to be higher and lower than other Pods — an important feature for production clusters workload.
