---
document_id: "doc-defd1703d006cc4e"
source_name: "reference/command-line-tools-reference/feature-gates/DefaultPodSysctls.md"
source_type: "text"
source_format: "md"
source_sha256: "bae6345955a65010dbb151ce4f970dc4c4a1c656848d4bd0ca2b7c5ea5a533d7"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/DefaultPodSysctls.md"
extracted_sha256: "bae6345955a65010dbb151ce4f970dc4c4a1c656848d4bd0ca2b7c5ea5a533d7"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/DefaultPodSysctls.md"
---

---
title: DefaultPodSysctls
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.37"
---

Enables the `defaultPodSysctls` field in [KubeletConfiguration](/docs/reference/config-api/kubelet-config.v1beta1/), allowing Node administrators to specify a default set of namespaced kernel parameters (sysctls) that the `kubelet` applies to all Pods on the Node. See [Setting Sysctls for All Pods](/docs/tasks/administer-cluster/sysctl-cluster/#setting-sysctls-for-all-pods) for more details.
