---
document_id: "doc-ed5fccb0b7c892cd"
source_name: "reference/command-line-tools-reference/feature-gates/StrictIPCIDRValidation.md"
source_type: "text"
source_format: "md"
source_sha256: "eac7780edc757b08c958886bef6a13bb7284b5449075e1deefbb2cc8034b579a"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/StrictIPCIDRValidation.md"
extracted_sha256: "eac7780edc757b08c958886bef6a13bb7284b5449075e1deefbb2cc8034b579a"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/StrictIPCIDRValidation.md"
---

---
title: StrictIPCIDRValidation
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.33"
    toVersion: "1.35"
  - stage: beta
    defaultValue: true
    fromVersion: "1.36"
---
Use stricter validation for fields containing IP addresses and CIDR values.

In particular, with this feature gate enabled, octets within IPv4 addresses are
not allowed to have any leading `0`s, and IPv4-mapped IPv6 values (e.g.
`::ffff:192.168.0.1`) are forbidden. These sorts of values can potentially cause
security problems when different components interpret the same string as
referring to different IP addresses (as in CVE-2021-29923).

This tightening applies only to fields in build-in API kinds, and not to
custom resource kinds, values in Kubernetes configuration files, or
command-line arguments.
