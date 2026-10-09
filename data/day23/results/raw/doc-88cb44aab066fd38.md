---
document_id: "doc-88cb44aab066fd38"
source_name: "reference/setup-tools/kubeadm/kubeadm-join-phase.md"
source_type: "text"
source_format: "md"
source_sha256: "37a9b2ce7f0d3c43097f9a161df677ca34ec6438127045e12c0445e90dc1e9bd"
source_snapshot: "data/day23/source/content/en/docs/reference/setup-tools/kubeadm/kubeadm-join-phase.md"
extracted_sha256: "37a9b2ce7f0d3c43097f9a161df677ca34ec6438127045e12c0445e90dc1e9bd"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/setup-tools/kubeadm/kubeadm-join-phase.md"
---

---
title: kubeadm join phase
weight: 90
content_type: concept
---

`kubeadm join phase` enables you to invoke atomic steps of the join process.
Hence, you can let kubeadm do some of the work and you can fill in the gaps
if you wish to apply customization.

`kubeadm join phase` is consistent with the [kubeadm join workflow](/docs/reference/setup-tools/kubeadm/kubeadm-join/#join-workflow),
and behind the scene both use the same code.

## kubeadm join phase {#cmd-join-phase}

{{< tabs name="tab-phase" >}}
{{< tab name="phase" include="generated/kubeadm_join/kubeadm_join_phase.md" />}}
{{< /tabs >}}

## kubeadm join phase preflight {#cmd-join-phase-preflight}

Using this phase you can execute preflight checks on a joining node.

{{< tabs name="tab-preflight" >}}
{{< tab name="preflight" include="generated/kubeadm_join/kubeadm_join_phase_preflight.md" />}}
{{< /tabs >}}

## kubeadm join phase control-plane-prepare {#cmd-join-phase-control-plane-prepare}

Using this phase you can prepare a node for serving a control-plane.

{{< tabs name="tab-control-plane-prepare" >}}
{{< tab name="control-plane-prepare" include="generated/kubeadm_join/kubeadm_join_phase_control-plane-prepare.md" />}}
{{< tab name="all" include="generated/kubeadm_join/kubeadm_join_phase_control-plane-prepare_all.md" />}}
{{< tab name="download-certs" include="generated/kubeadm_join/kubeadm_join_phase_control-plane-prepare_download-certs.md" />}}
{{< tab name="certs" include="generated/kubeadm_join/kubeadm_join_phase_control-plane-prepare_certs.md" />}}
{{< tab name="kubeconfig" include="generated/kubeadm_join/kubeadm_join_phase_control-plane-prepare_kubeconfig.md" />}}
{{< tab name="control-plane" include="generated/kubeadm_join/kubeadm_join_phase_control-plane-prepare_control-plane.md" />}}
{{< /tabs >}}

## kubeadm join phase kubelet-start {#cmd-join-phase-kubelet-start}

Using this phase you can write the kubelet settings, certificates and (re)start the kubelet.

{{< tabs name="tab-kubelet-start" >}}
{{< tab name="kubelet-start" include="generated/kubeadm_join/kubeadm_join_phase_kubelet-start.md" />}}
{{< /tabs >}}

## kubeadm join phase etcd-join {#cmd-join-phase-etcd-join}

Join the new etcd member to the etcd cluster.

{{< tabs name="tab-etcd-join" >}}
{{< tab name="etcd-join" include="generated/kubeadm_join/kubeadm_join_phase_etcd-join.md" />}}
{{< /tabs >}}

## kubeadm join phase control-plane-join {#cmd-join-phase-control-plane-join}

Using this phase you can join a node as a control-plane instance.

{{< tabs name="tab-control-plane-join" >}}
{{< tab name="control-plane-join" include="generated/kubeadm_join/kubeadm_join_phase_control-plane-join.md" />}}
{{< tab name="all" include="generated/kubeadm_join/kubeadm_join_phase_control-plane-join_all.md" />}}
{{< tab name="mark-control-plane" include="generated/kubeadm_join/kubeadm_join_phase_control-plane-join_mark-control-plane.md" />}}
{{< /tabs >}}

## kubeadm join phase wait-control-plane {#cmd-join-wait-control-plane}

Wait for the control plane components to start.

{{< tabs name="tab-wait-control-plane" >}}
{{< tab name="wait-control-plane" include="generated/kubeadm_join/kubeadm_join_phase_wait-control-plane.md" />}}
{{< /tabs >}}

## {{% heading "whatsnext" %}}

* [kubeadm init](/docs/reference/setup-tools/kubeadm/kubeadm-init/) to bootstrap a Kubernetes control-plane node
* [kubeadm join](/docs/reference/setup-tools/kubeadm/kubeadm-join/) to connect a node to the cluster
* [kubeadm reset](/docs/reference/setup-tools/kubeadm/kubeadm-reset/) to revert any changes made to this host by `kubeadm init` or `kubeadm join`
* [kubeadm alpha](/docs/reference/setup-tools/kubeadm/kubeadm-alpha/) to try experimental functionality
