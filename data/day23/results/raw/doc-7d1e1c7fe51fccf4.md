---
document_id: "doc-7d1e1c7fe51fccf4"
source_name: "reference/glossary/priority-class.md"
source_type: "text"
source_format: "md"
source_sha256: "9f851a2cead1c2f72ad83c4e731c45d48e2ac3338ab06287cfab97176e96b9fd"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/priority-class.md"
extracted_sha256: "9f851a2cead1c2f72ad83c4e731c45d48e2ac3338ab06287cfab97176e96b9fd"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/priority-class.md"
---

---
title: PriorityClass
id: priority-class
full_link: /docs/concepts/scheduling-eviction/pod-priority-preemption/#priorityclass
short_description: >
  A mapping from a class name to the scheduling priority that a Pod should have.
aka:
tags:
- core-object
---
A PriorityClass is a named class for the scheduling priority that should be assigned to a Pod
in that class.

<!--more-->

A [PriorityClass](/docs/concepts/scheduling-eviction/pod-priority-preemption/#how-to-use-priority-and-preemption)
is a non-namespaced object mapping a name to an integer priority, used for a Pod. The name is
specified in the `metadata.name` field, and the priority value in the `value` field. Priorities range from
-2147483648 to 1000000000 inclusive. Higher values indicate higher priority.
