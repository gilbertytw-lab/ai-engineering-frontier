---
document_id: "doc-78be408f2eb0fd7c"
source_name: "reference/command-line-tools-reference/feature-gates/CloudDualStackNodeIPs.md"
source_type: "text"
source_format: "md"
source_sha256: "bf4fe2540be7cb7bda27fcd39ac069cdb359ba4af23f448afca6fa6887d237ce"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/CloudDualStackNodeIPs.md"
extracted_sha256: "bf4fe2540be7cb7bda27fcd39ac069cdb359ba4af23f448afca6fa6887d237ce"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/CloudDualStackNodeIPs.md"
---

---
title: CloudDualStackNodeIPs
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.27"
    toVersion: "1.28"
  - stage: beta
    defaultValue: true
    fromVersion: "1.29"
    toVersion: "1.29"
  - stage: stable
    defaultValue: true
    fromVersion: "1.30"
    toVersion: "1.31"

removed: true
---
Enables dual-stack `kubelet --node-ip` with external cloud providers.
See [Configure IPv4/IPv6 dual-stack](/docs/concepts/services-networking/dual-stack/#configure-ipv4-ipv6-dual-stack)
for more details.
