---
document_id: "doc-c4f2e4c4bda5ace9"
source_name: "reference/glossary/pod-disruption-budget.md"
source_type: "text"
source_format: "md"
source_sha256: "d04da29d0ebabac2b8fa686a0e566590a7eee7cf3dfd94a34fa7408bc2d896ae"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/pod-disruption-budget.md"
extracted_sha256: "d04da29d0ebabac2b8fa686a0e566590a7eee7cf3dfd94a34fa7408bc2d896ae"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/pod-disruption-budget.md"
---

---
id: pod-disruption-budget
title: Pod Disruption Budget
full-link: /docs/concepts/workloads/pods/disruptions/
short_description: >
 An object that limits the number of Pods of a replicated application that are down simultaneously from voluntary disruptions.

aka:
 - PDB
related:
 - pod
 - container
tags:
 - operation
---

 A [Pod Disruption Budget](/docs/concepts/workloads/pods/disruptions/) allows an 
 application owner to create an object for a replicated application, that ensures 
 a certain number or percentage of {{< glossary_tooltip text="Pods" term_id="pod" >}}
 with an assigned label will not be voluntarily evicted at any point in time.

<!--more--> 

Involuntary disruptions cannot be prevented by PDBs; however they 
do count against the budget.
