---
document_id: "doc-e2ad5514490ceff3"
source_name: "reference/glossary/podgroup.md"
source_type: "text"
source_format: "md"
source_sha256: "47d2c1e5d1eecc31678104a4b7a3ab5b4ef2037c08032577ba25b823fac99310"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/podgroup.md"
extracted_sha256: "47d2c1e5d1eecc31678104a4b7a3ab5b4ef2037c08032577ba25b823fac99310"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/podgroup.md"
---

---
title: PodGroup
id: podgroup
full_link: /docs/concepts/workloads/podgroup-api/
short_description: >
  A PodGroup represents a set of Pods with common scheduling policy and constraints.

aka:
tags:
- core-object
- workload
---
A PodGroup is a runtime object that represents a group of Pods scheduled
together as a single unit. While the
[Workload API](/docs/concepts/workloads/workload-api/) defines scheduling policy
templates, PodGroups are the runtime counterparts that carry both the policy and
the scheduling status for a specific instance of that group.
