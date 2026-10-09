---
document_id: "doc-e8ae2cb2ad4e1d38"
source_name: "reference/command-line-tools-reference/feature-gates/DRAListTypeAttributes.md"
source_type: "text"
source_format: "md"
source_sha256: "8555c20287bbabb61febaf95dbcf256e635202cb96fe6dcccca2e88e4936065c"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/DRAListTypeAttributes.md"
extracted_sha256: "8555c20287bbabb61febaf95dbcf256e635202cb96fe6dcccca2e88e4936065c"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/DRAListTypeAttributes.md"
---

---
title: DRAListTypeAttributes
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.36"
---
Enables list-type attribute fields (`bools`, `ints`, `strings`, `versions`) for devices
in `ResourceSlice`, allowing a device to advertise multiple values for a single attribute.

When enabled, `matchAttribute` uses set-intersection semantics (the sets of attribute
values across all selected devices must have a non-empty intersection), and
`distinctAttribute` uses pairwise-disjoint semantics (the sets must share no values).
Scalar attributes remain backward-compatible, treated as singleton sets.

Also adds the `includes()` helper function to CEL device selector expressions, which
works on both scalar and list-type attributes.

For more information, see
[List type attributes](/docs/concepts/resource-management/dynamic-resource-allocation/dra-api/#list-type-attributes)
in the Dynamic Resource Allocation documentation.
