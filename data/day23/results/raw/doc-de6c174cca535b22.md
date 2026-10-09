---
document_id: "doc-de6c174cca535b22"
source_name: "tasks/administer-cluster/network-policy-provider/antrea-network-policy.md"
source_type: "text"
source_format: "md"
source_sha256: "76b92b0d32e904711022c8823c9ca4cdd3b7bdc0b4f62260601480d942309292"
source_snapshot: "data/day23/source/content/en/docs/tasks/administer-cluster/network-policy-provider/antrea-network-policy.md"
extracted_sha256: "76b92b0d32e904711022c8823c9ca4cdd3b7bdc0b4f62260601480d942309292"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/tasks/administer-cluster/network-policy-provider/antrea-network-policy.md"
---

---
title: Use Antrea for NetworkPolicy
content_type: task
weight: 10
---

<!-- overview -->
This page shows how to install and use Antrea CNI plugin on Kubernetes.
For background on Project Antrea, read the [Introduction to Antrea](https://antrea.io/docs/).

## {{% heading "prerequisites" %}}

You need to have a Kubernetes cluster. Follow the
[kubeadm getting started guide](/docs/reference/setup-tools/kubeadm/) to bootstrap one.

<!-- steps -->

## Deploying Antrea with kubeadm

Follow [Getting Started](https://github.com/vmware-tanzu/antrea/blob/main/docs/getting-started.md) guide to deploy Antrea for kubeadm.

## {{% heading "whatsnext" %}}

Once your cluster is running, you can follow the [Declare Network Policy](/docs/tasks/administer-cluster/declare-network-policy/) to try out Kubernetes NetworkPolicy.
