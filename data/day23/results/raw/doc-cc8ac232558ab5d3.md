---
document_id: "doc-cc8ac232558ab5d3"
source_name: "reference/glossary/cloud-controller-manager.md"
source_type: "text"
source_format: "md"
source_sha256: "f788ee206c01f1f756b841755fda588d60979afc98860f0bac921dece9a9e8ef"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/cloud-controller-manager.md"
extracted_sha256: "f788ee206c01f1f756b841755fda588d60979afc98860f0bac921dece9a9e8ef"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/cloud-controller-manager.md"
---

---
title: Cloud Controller Manager
id: cloud-controller-manager
full_link: /docs/concepts/architecture/cloud-controller/
short_description: >
  Control plane component that integrates Kubernetes with third-party cloud providers.
aka: 
tags:
- architecture
- operation
---
 A Kubernetes {{< glossary_tooltip text="control plane" term_id="control-plane" >}} component
that embeds cloud-specific control logic. The cloud controller manager lets you link your
cluster into your cloud provider's API, and separates out the components that interact
with that cloud platform from components that only interact with your cluster.

<!--more-->

By decoupling the interoperability logic between Kubernetes and the underlying cloud
infrastructure, the cloud-controller-manager component enables cloud providers to release
features at a different pace compared to the main Kubernetes project.
