---
document_id: "doc-f16cf0e15e5fe06b"
source_name: "reference/glossary/pod-lifecycle.md"
source_type: "text"
source_format: "md"
source_sha256: "9d4f2e66ab5e34d4bba366a26cb189fc273ea7ae712c430d13abe7e00dec6acc"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/pod-lifecycle.md"
extracted_sha256: "9d4f2e66ab5e34d4bba366a26cb189fc273ea7ae712c430d13abe7e00dec6acc"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/pod-lifecycle.md"
---

---
title: Pod Lifecycle
id: pod-lifecycle
full-link: /docs/concepts/workloads/pods/pod-lifecycle/
related:
 - pod
 - container
tags:
 - fundamental
short_description: >
  The sequence of states through which a Pod passes during its lifetime.
 
---
 The sequence of states through which a Pod passes during its lifetime.

<!--more--> 

The [Pod Lifecycle](/docs/concepts/workloads/pods/pod-lifecycle/) is defined by the states or phases of a Pod. There are five possible Pod phases: Pending, Running, Succeeded, Failed, and Unknown. A high-level description of the Pod state is summarized in the [PodStatus](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#podstatus-v1-core) `phase` field.
