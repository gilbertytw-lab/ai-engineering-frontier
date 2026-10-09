---
document_id: "doc-1bd4b1224b67afa8"
source_name: "tutorials/_index.md"
source_type: "text"
source_format: "md"
source_sha256: "16ecc6861d349ef27d97e730c92ab0406f2d096e7a30d8b498579847e03acc90"
source_snapshot: "data/day23/source/content/en/docs/tutorials/_index.md"
extracted_sha256: "16ecc6861d349ef27d97e730c92ab0406f2d096e7a30d8b498579847e03acc90"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/tutorials/_index.md"
---

---
title: Tutorials
main_menu: true
no_list: true
weight: 60
content_type: concept
---

<!-- overview -->

This section of the Kubernetes documentation contains tutorials.
A tutorial shows how to accomplish a goal that is larger than a single
[task](/docs/tasks/). Typically a tutorial has several sections,
each of which has a sequence of steps.
Before walking through each tutorial, you may want to bookmark the
[Standardized Glossary](/docs/reference/glossary/) page for later references.

<!-- body -->

## Basics

* [Kubernetes Basics](/docs/tutorials/kubernetes-basics/) is an in-depth interactive tutorial that helps you understand the Kubernetes system and try out some basic Kubernetes features.
* [Introduction to Kubernetes (edX)](https://www.edx.org/course/introduction-kubernetes-linuxfoundationx-lfs158x#)
* [Hello Minikube](/docs/tutorials/hello-minikube/)

## Configuration

* [Configuring Redis Using a ConfigMap](/docs/tutorials/configuration/configure-redis-using-configmap/)

## Authoring Pods

* [Adopting Sidecar Containers](/docs/tutorials/configuration/pod-sidecar-containers/)

## Stateless Applications

* [Exposing an External IP Address to Access an Application in a Cluster](/docs/tutorials/stateless-application/expose-external-ip-address/)
* [Example: Deploying PHP Guestbook application with Redis](/docs/tutorials/stateless-application/guestbook/)

## Stateful Applications

* [StatefulSet Basics](/docs/tutorials/stateful-application/basic-stateful-set/)
* [Example: WordPress and MySQL with Persistent Volumes](/docs/tutorials/stateful-application/mysql-wordpress-persistent-volume/)
* [Example: Deploying Cassandra with Stateful Sets](/docs/tutorials/stateful-application/cassandra/)
* [Running ZooKeeper, A CP Distributed System](/docs/tutorials/stateful-application/zookeeper/)

## Services

* [Connecting Applications with Services](/docs/tutorials/services/connect-applications-service/)
* [Using Source IP](/docs/tutorials/services/source-ip/)

## Security

* [Apply Pod Security Standards at Cluster level](/docs/tutorials/security/cluster-level-pss/)
* [Apply Pod Security Standards at Namespace level](/docs/tutorials/security/ns-level-pss/)
* [Restrict a Container's Access to Resources with AppArmor](/docs/tutorials/security/apparmor/)
* [Seccomp](/docs/tutorials/security/seccomp/)

## Cluster Management

* [Running Kubelet in Standalone Mode](/docs/tutorials/cluster-management/kubelet-standalone/)
* [Configuring Swap Memory on Kubernetes Nodes](/docs/tutorials/cluster-management/provision-swap-memory/)
* [Install Drivers and Allocate Devices with DRA](/docs/tutorials/cluster-management/install-use-dra/)
* [Explore Validating and Mutating Admission Policies](/docs/tutorials/cluster-management/admission-policies/)

## {{% heading "whatsnext" %}}

If you would like to write a tutorial, see
[Content Page Types](/docs/contribute/style/page-content-types/)
for information about the tutorial page type.
