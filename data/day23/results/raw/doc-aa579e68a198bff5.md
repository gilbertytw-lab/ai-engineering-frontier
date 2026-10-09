---
document_id: "doc-aa579e68a198bff5"
source_name: "reference/setup-tools/kubeadm/kubeadm-kubeconfig.md"
source_type: "text"
source_format: "md"
source_sha256: "eff11bbba158d0fce99c6a78482ab8a5bf33d54783cca24718ee45297b8facd0"
source_snapshot: "data/day23/source/content/en/docs/reference/setup-tools/kubeadm/kubeadm-kubeconfig.md"
extracted_sha256: "eff11bbba158d0fce99c6a78482ab8a5bf33d54783cca24718ee45297b8facd0"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/setup-tools/kubeadm/kubeadm-kubeconfig.md"
---

---
title: kubeadm kubeconfig
content_type: concept
weight: 90
---

`kubeadm kubeconfig` provides utilities for managing kubeconfig files.

For examples on how to use `kubeadm kubeconfig user` see
[Generating kubeconfig files for additional users](/docs/tasks/administer-cluster/kubeadm/kubeadm-certs#kubeconfig-additional-users).

## kubeadm kubeconfig {#cmd-kubeconfig}

{{< tabs name="tab-kubeconfig" >}}
{{< tab name="overview" include="generated/kubeadm_kubeconfig/_index.md" />}}
{{< /tabs >}}

## kubeadm kubeconfig user {#cmd-kubeconfig-user}

This command can be used to output a kubeconfig file for an additional user.

{{< tabs name="tab-kubeconfig-user" >}}
{{< tab name="user" include="generated/kubeadm_kubeconfig/kubeadm_kubeconfig_user.md" />}}
{{< /tabs >}}
