---
document_id: "doc-69071ff376ae5cbe"
source_name: "reference/setup-tools/kubeadm/generated/kubeadm_config/kubeadm_config_print_join-defaults.md"
source_type: "text"
source_format: "md"
source_sha256: "15a191d9af85b42a83e30829d8033944ebcafdfedfba408ec7375214cb686d3e"
source_snapshot: "data/day23/source/content/en/docs/reference/setup-tools/kubeadm/generated/kubeadm_config/kubeadm_config_print_join-defaults.md"
extracted_sha256: "15a191d9af85b42a83e30829d8033944ebcafdfedfba408ec7375214cb686d3e"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/setup-tools/kubeadm/generated/kubeadm_config/kubeadm_config_print_join-defaults.md"
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


Print default join configuration, that can be used for 'kubeadm join'

### Synopsis



This command prints objects such as the default join configuration that is used for 'kubeadm join'.

Note that sensitive values like the Bootstrap Token fields are replaced with placeholder values like "abcdef.0123456789abcdef" in order to pass validation but
not perform the real computation for creating a token.


```
kubeadm config print join-defaults [flags]
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>help for join-defaults</p></td>
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
<td colspan="2">--kubeconfig string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "/etc/kubernetes/admin.conf"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file.</p></td>
</tr>

<tr>
<td colspan="2">--rootfs string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>The path to the 'real' host root filesystem. This will cause kubeadm to chroot into the provided path.</p></td>
</tr>

</tbody>
</table>
