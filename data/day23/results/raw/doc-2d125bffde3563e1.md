---
document_id: "doc-2d125bffde3563e1"
source_name: "tasks/administer-cluster/network-policy-provider/kube-router-network-policy.md"
source_type: "text"
source_format: "md"
source_sha256: "c3403079ce6f867daa6a35cdfde1278121e5aaee74a6fa33d82d8e0c91174762"
source_snapshot: "data/day23/source/content/en/docs/tasks/administer-cluster/network-policy-provider/kube-router-network-policy.md"
extracted_sha256: "c3403079ce6f867daa6a35cdfde1278121e5aaee74a6fa33d82d8e0c91174762"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/tasks/administer-cluster/network-policy-provider/kube-router-network-policy.md"
---

---
reviewers:
- murali-reddy
title: Use Kube-router for NetworkPolicy
content_type: task
weight: 40
---

<!-- overview -->
This page shows how to use [Kube-router](https://github.com/cloudnativelabs/kube-router) for NetworkPolicy.


## {{% heading "prerequisites" %}}

You need to have a Kubernetes cluster running. If you do not already have a cluster, you can create one by using any of the cluster installers like Kops, Bootkube, Kubeadm etc.


<!-- steps -->
## Installing Kube-router addon
The Kube-router Addon comes with a Network Policy Controller that watches Kubernetes API server for any NetworkPolicy and pods updated and configures iptables rules and ipsets to allow or block traffic as directed by the policies. Please follow the [trying Kube-router with cluster installers](https://www.kube-router.io/docs/user-guide/#try-kube-router-with-cluster-installers) guide to install Kube-router addon.


## {{% heading "whatsnext" %}}

Once you have installed the Kube-router addon, you can follow the [Declare Network Policy](/docs/tasks/administer-cluster/declare-network-policy/) to try out Kubernetes NetworkPolicy.
