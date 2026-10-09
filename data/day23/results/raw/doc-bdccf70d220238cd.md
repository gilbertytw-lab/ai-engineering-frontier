---
document_id: "doc-bdccf70d220238cd"
source_name: "reference/glossary/replica.md"
source_type: "text"
source_format: "md"
source_sha256: "3c4e24b2bc217bb0f47671f5e535764cb485556c5802bbc0ef43144d5909a3f3"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/replica.md"
extracted_sha256: "3c4e24b2bc217bb0f47671f5e535764cb485556c5802bbc0ef43144d5909a3f3"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/replica.md"
---

---
title: Replica
id: replica
full_link: 
short_description: >
  Replicas are copies of pods, ensuring availability, scalability, and fault tolerance by maintaining identical instances.
aka: 
tags:
- fundamental
- workload
---
A copy or duplicate of a {{< glossary_tooltip text="Pod" term_id="pod" >}} or
a set of pods. Replicas ensure high availability, scalability, and fault tolerance
by maintaining multiple identical instances of a pod.

<!--more-->
Replicas are commonly used in Kubernetes to achieve the desired application state and reliability.
They enable workload scaling and distribution across multiple nodes in a cluster.

By defining the number of replicas in a Deployment or ReplicaSet, Kubernetes ensures that
the specified number of instances are running, automatically adjusting the count as needed.

Replica management allows for efficient load balancing, rolling updates, and
self-healing capabilities in a Kubernetes cluster.
