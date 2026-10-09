---
document_id: "doc-cd0ef987c13c0cd3"
source_name: "reference/glossary/controller.md"
source_type: "text"
source_format: "md"
source_sha256: "3901685470e210e2040a6ca6472e4951f9bfbc65282914355408f4081dd4457b"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/controller.md"
extracted_sha256: "3901685470e210e2040a6ca6472e4951f9bfbc65282914355408f4081dd4457b"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/controller.md"
---

---
title: Controller
id: controller
full_link: /docs/concepts/architecture/controller/
short_description: >
  A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state.

aka: 
tags:
- architecture
- fundamental
---
In Kubernetes, controllers are control loops that watch the state of your
{{< glossary_tooltip term_id="cluster" text="cluster">}}, then make or request
changes where needed.
Each controller tries to move the current cluster state closer to the desired
state.

<!--more-->

Controllers watch the shared state of your cluster through the
{{< glossary_tooltip text="apiserver" term_id="kube-apiserver" >}} (part of the
{{< glossary_tooltip term_id="control-plane" >}}).

Some controllers also run inside the control plane, providing control loops that
are core to Kubernetes' operations. For example: the deployment controller, the
daemonset controller, the namespace controller, and the persistent volume
controller (and others) all run within the
{{< glossary_tooltip term_id="kube-controller-manager" >}}.
