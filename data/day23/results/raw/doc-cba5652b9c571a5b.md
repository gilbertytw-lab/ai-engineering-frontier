---
document_id: "doc-cba5652b9c571a5b"
source_name: "reference/glossary/pod-disruption.md"
source_type: "text"
source_format: "md"
source_sha256: "8c6e0718fb1d7ba55906844d0dd1fa43560a268eeead9009dd0d142e5a6de228"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/pod-disruption.md"
extracted_sha256: "8c6e0718fb1d7ba55906844d0dd1fa43560a268eeead9009dd0d142e5a6de228"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/pod-disruption.md"
---

---
id: pod-disruption
title: Pod Disruption
full_link: /docs/concepts/workloads/pods/disruptions/
short_description: >
  The process by which Pods on Nodes are terminated either voluntarily or involuntarily.

aka:
related:
 - pod
 - container
tags:
 - operation
---

[Pod disruption](/docs/concepts/workloads/pods/disruptions/) is the process by which 
Pods on Nodes are terminated either voluntarily or involuntarily. 

<!--more--> 

Voluntary disruptions are started intentionally by application owners or cluster 
administrators. Involuntary disruptions are unintentional and can be triggered by 
unavoidable issues like Nodes running out of {{< glossary_tooltip text="resources" term_id="infrastructure-resource" >}},
or by accidental deletions.
