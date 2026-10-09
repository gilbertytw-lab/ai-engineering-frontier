---
document_id: "doc-b09e3143dbdfa1c3"
source_name: "reference/setup-tools/kubeadm/generated/kubeadm_upgrade/kubeadm_upgrade_diff.md"
source_type: "text"
source_format: "md"
source_sha256: "e64f7b7004320fbc0bd39bdee49aae4da05598dc2102740e2844b375413d4e89"
source_snapshot: "data/day23/source/content/en/docs/reference/setup-tools/kubeadm/generated/kubeadm_upgrade/kubeadm_upgrade_diff.md"
extracted_sha256: "e64f7b7004320fbc0bd39bdee49aae4da05598dc2102740e2844b375413d4e89"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/setup-tools/kubeadm/generated/kubeadm_upgrade/kubeadm_upgrade_diff.md"
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


Show what differences would be applied to existing static pod manifests. See also: kubeadm upgrade apply --dry-run

```
kubeadm upgrade diff [version] [flags]
```

### Options

   <table style="width: 100%; table-layout: fixed;">
<colgroup>
<col span="1" style="width: 10px;" />
<col span="1" />
</colgroup>
<tbody>

<tr>
<td colspan="2">--config string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>Path to a kubeadm configuration file.</p></td>
</tr>

<tr>
<td colspan="2">-c, --context-lines int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 3</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>How many lines of context in the diff</p></td>
</tr>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>help for diff</p></td>
</tr>

<tr>
<td colspan="2">--kubeconfig string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "/etc/kubernetes/admin.conf"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>The kubeconfig file to use when talking to the cluster. If the flag is not set, a set of standard locations can be searched for an existing kubeconfig file.</p></td>
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
