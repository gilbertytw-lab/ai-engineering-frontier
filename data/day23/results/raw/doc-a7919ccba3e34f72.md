---
document_id: "doc-a7919ccba3e34f72"
source_name: "tasks/administer-cluster/coredns.md"
source_type: "text"
source_format: "md"
source_sha256: "3a925c8813a6d22c1c2ca47991782585ff327f6ceb7308867cc9d30435437fdd"
source_snapshot: "data/day23/source/content/en/docs/tasks/administer-cluster/coredns.md"
extracted_sha256: "3a925c8813a6d22c1c2ca47991782585ff327f6ceb7308867cc9d30435437fdd"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/tasks/administer-cluster/coredns.md"
---

---
reviewers:
- johnbelamaric
title: Using CoreDNS for Service Discovery
min-kubernetes-server-version: v1.9
content_type: task
weight: 380
---

<!-- overview -->
This page describes the CoreDNS upgrade process and how to install CoreDNS.


## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}


<!-- steps -->

## About CoreDNS

[CoreDNS](https://coredns.io) is a flexible, extensible DNS server
that is the default implementation of Kubernetes cluster DNS.
Like Kubernetes, the CoreDNS project is hosted by the
{{< glossary_tooltip text="CNCF" term_id="cncf" >}}.

## Installing CoreDNS

For manual deployment, see the documentation at the
[CoreDNS website](https://coredns.io/manual/installation/).

## Upgrading CoreDNS

You can check the version of CoreDNS that kubeadm installs for each version of
Kubernetes in the page
[CoreDNS version in Kubernetes](https://github.com/coredns/deployment/blob/master/kubernetes/CoreDNS-k8s_version.md).

CoreDNS can be upgraded manually in case you want to only upgrade CoreDNS
or use your own custom image.
There is a helpful [guideline and walkthrough](https://github.com/coredns/deployment/blob/master/kubernetes/Upgrading_CoreDNS.md)
available to ensure a smooth upgrade.
Make sure the existing CoreDNS configuration ("Corefile") is retained when
upgrading your cluster.

If you are upgrading your cluster using the `kubeadm` tool, `kubeadm`
can take care of retaining the existing CoreDNS configuration automatically.


## Tuning CoreDNS

When resource utilisation is a concern, it may be useful to tune the
configuration of CoreDNS. For more details, check out the
[documentation on scaling CoreDNS](https://github.com/coredns/deployment/blob/master/kubernetes/Scaling_CoreDNS.md).

## {{% heading "whatsnext" %}}

You can configure [CoreDNS](https://coredns.io) to support many use cases beyond
basic service name resolution by modifying the CoreDNS configuration ("Corefile").
For more information, see the [documentation](https://coredns.io/plugins/kubernetes/)
for the `kubernetes` CoreDNS plugin, or read the 
[Custom DNS Entries for Kubernetes](https://coredns.io/2017/05/08/custom-dns-entries-for-kubernetes/).
in the CoreDNS blog.
