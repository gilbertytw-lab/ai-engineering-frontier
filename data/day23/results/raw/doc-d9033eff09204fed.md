---
document_id: "doc-d9033eff09204fed"
source_name: "reference/command-line-tools-reference/feature-gates/DRADeviceCompatibilityGroups.md"
source_type: "text"
source_format: "md"
source_sha256: "3ecf30975c3362dc741e2538f3f60a2cb8da400075c1d689672a140b4cb6f9ca"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/DRADeviceCompatibilityGroups.md"
extracted_sha256: "3ecf30975c3362dc741e2538f3f60a2cb8da400075c1d689672a140b4cb6f9ca"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/DRADeviceCompatibilityGroups.md"
---

---
title: DRADeviceCompatibilityGroups
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.37"
---
Enables support for [device compatibility groups](/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#device-compatibility-groups)
in DRA. Drivers can declare opaque compatibility groups on each
`consumesCounters` entry of a device in a ResourceSlice, and the scheduler
only co-allocates devices drawing from the same counter set when their
declared groups intersect. Requires `DRAPartitionableDevices` to be enabled.
