---
document_id: "doc-aec03fc6fa3f0fd9"
source_name: "reference/glossary/kube-proxy.md"
source_type: "text"
source_format: "md"
source_sha256: "ac3185478aa7bf2d7057a38304d93d02654dd929522b56315b81455ad5544128"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/kube-proxy.md"
extracted_sha256: "ac3185478aa7bf2d7057a38304d93d02654dd929522b56315b81455ad5544128"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/kube-proxy.md"
---

---
title: kube-proxy
id: kube-proxy
full_link: /docs/reference/command-line-tools-reference/kube-proxy/
short_description: >
  `kube-proxy` is a network proxy that runs on each node in the cluster.

aka:
tags:
- fundamental
- networking
---
 kube-proxy is a network proxy that runs on each
{{< glossary_tooltip text="node" term_id="node" >}} in your cluster,
implementing part of the Kubernetes
{{< glossary_tooltip term_id="service">}} concept.

<!--more-->

[kube-proxy](/docs/reference/command-line-tools-reference/kube-proxy/)
maintains network rules on nodes. These network rules allow network
communication to your Pods from network sessions inside or outside of
your cluster.

kube-proxy uses the operating system packet filtering layer if there is one
and it's available. Otherwise, kube-proxy forwards the traffic itself.
