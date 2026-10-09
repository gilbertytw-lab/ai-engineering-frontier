---
document_id: "doc-ab02fd7e3af40dd4"
source_name: "reference/glossary/kube-scheduler.md"
source_type: "text"
source_format: "md"
source_sha256: "b27e62dc2876a209aa5c6de76a0bf240c49960b824f9e4d86d4d8836b334ff2a"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/kube-scheduler.md"
extracted_sha256: "b27e62dc2876a209aa5c6de76a0bf240c49960b824f9e4d86d4d8836b334ff2a"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/kube-scheduler.md"
---

---
title: kube-scheduler
id: kube-scheduler
full_link: /docs/reference/command-line-tools-reference/kube-scheduler/
short_description: >
  Control plane component that watches for newly created pods with no assigned node, and selects a node for them to run on.

aka: 
tags:
- architecture
---
Control plane component that watches for newly created
{{< glossary_tooltip term_id="pod" text="Pods" >}} with no assigned
{{< glossary_tooltip term_id="node" text="node">}}, and selects a node for them
to run on.

<!--more-->

Factors taken into account for scheduling decisions include:
individual and collective {{< glossary_tooltip text="resource" term_id="infrastructure-resource" >}}
requirements, hardware/software/policy constraints, affinity and anti-affinity specifications,
data locality, inter-workload interference, and deadlines.
