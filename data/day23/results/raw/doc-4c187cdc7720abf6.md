---
document_id: "doc-4c187cdc7720abf6"
source_name: "reference/command-line-tools-reference/feature-gates/DRAOptionalNodeOperations.md"
source_type: "text"
source_format: "md"
source_sha256: "b34c333420b62afafd4075172a09728c04c5fde02596344367667b4ea550c0b3"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/DRAOptionalNodeOperations.md"
extracted_sha256: "b34c333420b62afafd4075172a09728c04c5fde02596344367667b4ea550c0b3"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/DRAOptionalNodeOperations.md"
---

---
title: DRAOptionalNodeOperations
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.37"
---
Enables support for optional node-local operations in Dynamic Resource
Allocation (DRA). This allows drivers to declare that specific node operations
(`NodePrepareResources` and/or `NodeUnprepareResources`) can be skipped for
their devices, enabling the `kubelet` to bypass unnecessary gRPC calls.

For more information, see
[Optional node operations](/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#optional-node-operations)
in the Dynamic Resource Allocation documentation.
