---
document_id: "doc-feb04d8cfaed1bb6"
source_name: "reference/node/node-labels.md"
source_type: "text"
source_format: "md"
source_sha256: "41c62656853b063964f643bea82c9a09615ccf76207821448f1d688e6c268fc2"
source_snapshot: "data/day23/source/content/en/docs/reference/node/node-labels.md"
extracted_sha256: "41c62656853b063964f643bea82c9a09615ccf76207821448f1d688e6c268fc2"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/node/node-labels.md"
---

---
content_type: "reference"
title: Node Labels Populated By The Kubelet
weight: 40
---

Kubernetes {{< glossary_tooltip text="nodes" term_id="node" >}} come pre-populated
with a standard set of {{< glossary_tooltip text="labels" term_id="label" >}}.

You can also set your own labels on nodes, either through the kubelet configuration or
using the Kubernetes API.

## Preset labels

The preset labels that Kubernetes sets on nodes are:

* [`kubernetes.io/arch`](/docs/reference/labels-annotations-taints/#kubernetes-io-arch)
* [`kubernetes.io/hostname`](/docs/reference/labels-annotations-taints/#kubernetesiohostname)
* [`kubernetes.io/os`](/docs/reference/labels-annotations-taints/#kubernetes-io-os)
* [`node.kubernetes.io/instance-type`](/docs/reference/labels-annotations-taints/#nodekubernetesioinstance-type)
  (if known to the kubelet &ndash; Kubernetes may not have this information to set the label)
* [`topology.kubernetes.io/region`](/docs/reference/labels-annotations-taints/#topologykubernetesioregion)
  (if known to the kubelet &ndash; Kubernetes may not have this information to set the label)
* [`topology.kubernetes.io/zone`](/docs/reference/labels-annotations-taints/#topologykubernetesiozone)
  (if known to the kubelet &ndash; Kubernetes may not have this information to set the label)

{{<note>}}
The value of these labels is cloud provider specific and is not guaranteed to be reliable.
For example, the value of `kubernetes.io/hostname` may be the same as the node name in some environments
and a different value in other environments.
{{</note>}}

## {{% heading "whatsnext" %}}

- See [Well-Known Labels, Annotations and Taints](/docs/reference/labels-annotations-taints/) for a list of common labels.
- Learn how to [add a label to a node](/docs/tasks/configure-pod-container/assign-pods-nodes/#add-a-label-to-a-node).
