---
document_id: "doc-5a78fd1a2ea91da4"
source_name: "reference/setup-tools/kubeadm/generated/kubeadm_join/kubeadm_join_phase_control-plane-join.md"
source_type: "text"
source_format: "md"
source_sha256: "49c470b2025d949a0c20b1a2cc14d0fd6f8124668d4a1f7e2e287350694f9346"
source_snapshot: "data/day23/source/content/en/docs/reference/setup-tools/kubeadm/generated/kubeadm_join/kubeadm_join_phase_control-plane-join.md"
extracted_sha256: "49c470b2025d949a0c20b1a2cc14d0fd6f8124668d4a1f7e2e287350694f9346"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/setup-tools/kubeadm/generated/kubeadm_join/kubeadm_join_phase_control-plane-join.md"
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


Join a machine as a control plane instance

```
kubeadm join phase control-plane-join [flags]
```

### Examples

```
  # Joins a machine as a control plane instance
  kubeadm join phase control-plane-join all
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>help for control-plane-join</p></td>
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
