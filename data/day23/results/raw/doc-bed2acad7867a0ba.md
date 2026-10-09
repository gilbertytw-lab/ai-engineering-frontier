---
document_id: "doc-bed2acad7867a0ba"
source_name: "reference/glossary/event.md"
source_type: "text"
source_format: "md"
source_sha256: "f00b5fa6ceb0c3f877380ba46b96a7ffa95424b892aaf0dc93fcf816a0085af5"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/event.md"
extracted_sha256: "f00b5fa6ceb0c3f877380ba46b96a7ffa95424b892aaf0dc93fcf816a0085af5"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/event.md"
---

---
title: Event
id: event
full_link: /docs/reference/kubernetes-api/cluster-resources/event-v1/
short_description: >
   Kubernetes objects that describe some state change in the cluster.
aka: 
tags:
- core-object
- fundamental
---
A Kubernetes {{< glossary_tooltip text="object" term_id="object" >}} that describes state changes
or notable occurrences in the cluster.

<!--more-->
Events have a limited retention time and triggers and messages may evolve with time.
Event consumers should not rely on the timing of an event with a given reason reflecting a consistent underlying trigger,
or the continued existence of events with that reason.

Events should be treated as informative, best-effort, supplemental data.

In Kubernetes, [auditing](/docs/tasks/debug/debug-cluster/audit/) generates a different kind of
Event record (API group `audit.k8s.io`).
