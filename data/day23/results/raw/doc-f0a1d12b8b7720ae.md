---
document_id: "doc-f0a1d12b8b7720ae"
source_name: "reference/glossary/kubelet.md"
source_type: "text"
source_format: "md"
source_sha256: "b4280161f9233614017ccf36fc74979dacc6b00f876591650be4552678b1188e"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/kubelet.md"
extracted_sha256: "b4280161f9233614017ccf36fc74979dacc6b00f876591650be4552678b1188e"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/kubelet.md"
---

---
title: Kubelet
id: kubelet
full_link: /docs/reference/command-line-tools-reference/kubelet
short_description: >
  An agent that runs on each node in the cluster. It makes sure that containers are running in a pod.

aka:
tags:
- fundamental
---
 An agent that runs on each {{< glossary_tooltip text="node" term_id="node" >}} in the cluster. It makes sure that {{< glossary_tooltip text="containers" term_id="container" >}} are running in a {{< glossary_tooltip text="Pod" term_id="pod" >}}.

<!--more-->


The [kubelet](/docs/reference/command-line-tools-reference/kubelet/) takes a set of PodSpecs that 
are provided through various mechanisms and ensures that the containers described in those 
PodSpecs are running and healthy. The kubelet doesn't manage containers which were not created by 
Kubernetes.
