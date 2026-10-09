---
document_id: "doc-5aac8770cc3dba48"
source_name: "reference/setup-tools/kubeadm/generated/kubeadm_join/kubeadm_join_phase_wait-control-plane.md"
source_type: "text"
source_format: "md"
source_sha256: "a4db417f353ae6b4565321629cf3a863cfc3b5b29cc27dd70033ee77403301de"
source_snapshot: "data/day23/source/content/en/docs/reference/setup-tools/kubeadm/generated/kubeadm_join/kubeadm_join_phase_wait-control-plane.md"
extracted_sha256: "a4db417f353ae6b4565321629cf3a863cfc3b5b29cc27dd70033ee77403301de"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/setup-tools/kubeadm/generated/kubeadm_join/kubeadm_join_phase_wait-control-plane.md"
---

<!--
The file is auto-generated from the Go source code of the component using a generic
[generator](https://github.com/kubernetes-sigs/reference-docs/). To learn how
to generate the reference documentation, please read
[Contributing to the reference documentation](/docs/contribute/generate-ref-docs/).
To update the reference content, please follow the
[Contributing upstream](/docs/contribute/generate-ref-docs/contribute-upstream/)
guide. You can file document formatting bugs against the
[reference-docs](https://github.com/kubernetes-sigs/reference-docs/) project.
-->


### Synopsis


Wait for the control plane to start

```
kubeadm join phase wait-control-plane [flags]
```

### Options

   <table style="width: 100%; table-layout: fixed;">
<colgroup>
<col span="1" style="width: 10px;" />
<col span="1" />
</colgroup>
<tbody>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>help for wait-control-plane</p></td>
</tr>

</tbody>
</table>



### Options inherited from parent commands

   <table style="width: 100%; table-layout: fixed;">
<colgroup>
<col span="1" style="width: 10px;" />
<col span="1" />
</colgroup>
<tbody>

<tr>
<td colspan="2">--rootfs string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path.</p></td>
</tr>

</tbody>
</table>
