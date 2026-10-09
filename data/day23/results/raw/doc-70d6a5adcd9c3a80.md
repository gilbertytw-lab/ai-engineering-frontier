---
document_id: "doc-70d6a5adcd9c3a80"
source_name: "reference/glossary/garbage-collection.md"
source_type: "text"
source_format: "md"
source_sha256: "aeb1483848bab6ba3eaaa484f03a9a3ead60c50aa977fa8bff604ef03a144364"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/garbage-collection.md"
extracted_sha256: "aeb1483848bab6ba3eaaa484f03a9a3ead60c50aa977fa8bff604ef03a144364"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/garbage-collection.md"
---

---
title: Garbage Collection
id: garbage-collection
full_link: /docs/concepts/architecture/garbage-collection/
short_description: >
  A collective term for the various mechanisms Kubernetes uses to clean up cluster
  resources.

aka: 
tags:
- fundamental
- operation
---

Garbage collection is a collective term for the various mechanisms Kubernetes uses to clean up
cluster resources. 

<!--more-->

Kubernetes uses garbage collection to clean up resources like
[unused containers and images](/docs/concepts/architecture/garbage-collection/#containers-images),
[failed Pods](/docs/concepts/workloads/pods/pod-lifecycle/#pod-garbage-collection),
[objects owned by the targeted resource](/docs/concepts/overview/working-with-objects/owners-dependents/),
[completed Jobs](/docs/concepts/workloads/controllers/ttlafterfinished/), and resources
that have expired or failed.
