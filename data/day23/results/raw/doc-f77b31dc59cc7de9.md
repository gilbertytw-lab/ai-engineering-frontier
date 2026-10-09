---
document_id: "doc-f77b31dc59cc7de9"
source_name: "concepts/scheduling-eviction/_index.md"
source_type: "text"
source_format: "md"
source_sha256: "2b5b7f4720b5c66bc7eea4646b3a9eb36baec1d92004c622858bd78a30ffaa94"
source_snapshot: "data/day23/source/content/en/docs/concepts/scheduling-eviction/_index.md"
extracted_sha256: "2b5b7f4720b5c66bc7eea4646b3a9eb36baec1d92004c622858bd78a30ffaa94"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/concepts/scheduling-eviction/_index.md"
---

---
title: "Scheduling, Preemption and Eviction"
weight: 95
content_type: concept
no_list: true
---

In Kubernetes, scheduling refers to making sure that {{<glossary_tooltip text="Pods" term_id="pod">}}
are matched to {{<glossary_tooltip text="Nodes" term_id="node">}} so that the
{{<glossary_tooltip text="kubelet" term_id="kubelet">}} can run them. Preemption
is the process of terminating Pods with lower {{<glossary_tooltip text="Priority" term_id="pod-priority">}}
so that Pods with higher Priority can schedule on Nodes. Eviction is the process
of terminating one or more Pods on Nodes.

## Scheduling

* [Kubernetes Scheduler](/docs/concepts/scheduling-eviction/kube-scheduler/)
* [Assigning Pods to Nodes](/docs/concepts/scheduling-eviction/assign-pod-node/)
* [Pod Overhead](/docs/concepts/scheduling-eviction/pod-overhead/)
* [Pod Topology Spread Constraints](/docs/concepts/scheduling-eviction/topology-spread-constraints/)
* [Taints and Tolerations](/docs/concepts/scheduling-eviction/taint-and-toleration/)
* [Scheduling Framework](/docs/concepts/scheduling-eviction/scheduling-framework)
* [Scheduler Performance Tuning](/docs/concepts/scheduling-eviction/scheduler-perf-tuning/)
* [Resource Bin Packing for Extended Resources](/docs/concepts/scheduling-eviction/resource-bin-packing/)
* [Pod Scheduling Readiness](/docs/concepts/scheduling-eviction/pod-scheduling-readiness/)
* [PodGroup Scheduling](/docs/concepts/scheduling-eviction/podgroup-scheduling/)
* [Gang Scheduling](/docs/concepts/scheduling-eviction/gang-scheduling/)
* [Topology-aware Scheduling](/docs/concepts/scheduling-eviction/topology-aware-scheduling/)
* [Workload-aware preemption](/docs/concepts/scheduling-eviction/workload-aware-preemption/)
* [Descheduler](https://github.com/kubernetes-sigs/descheduler#descheduler-for-kubernetes)
* [Node Declared Features](/docs/concepts/scheduling-eviction/node-declared-features/)

## Pod Disruption

{{<glossary_definition term_id="pod-disruption" length="all">}}

* [Pod Priority and Preemption](/docs/concepts/scheduling-eviction/pod-priority-preemption/)
* [Node-pressure Eviction](/docs/concepts/scheduling-eviction/node-pressure-eviction/)
* [API-initiated Eviction](/docs/concepts/scheduling-eviction/api-eviction/)
