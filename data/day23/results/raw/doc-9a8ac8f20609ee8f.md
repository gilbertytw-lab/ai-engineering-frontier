---
document_id: "doc-9a8ac8f20609ee8f"
source_name: "reference/command-line-tools-reference/feature-gates/ResourceHealthStatus.md"
source_type: "text"
source_format: "md"
source_sha256: "ed9a453258a65a5577bec8d87277aad69f9d4f311b05c66f44bf2b4d33a80bcd"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/ResourceHealthStatus.md"
extracted_sha256: "ed9a453258a65a5577bec8d87277aad69f9d4f311b05c66f44bf2b4d33a80bcd"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/ResourceHealthStatus.md"
---

---
title: ResourceHealthStatus
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.31"
    toVersion: "1.35"
  - stage: beta
    defaultValue: true
    fromVersion: "1.36"
---
Enable the `allocatedResourcesStatus` field within the `.status` for a Pod. The field
reports additional details for each container in the Pod,
with the health information for each device assigned to the Pod.

Starting in v1.36 (beta), the health report includes an optional `message` field that
provides additional human-readable context about the health status, such as error details
or failure reasons.

This feature applies to devices managed by both [Device Plugins](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/#device-plugin-and-unhealthy-devices) and [Dynamic Resource Allocation](/docs/concepts/resource-management/dynamic-resource-allocation/dra-observability/#device-health-monitoring). See [Device plugin and unhealthy devices](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/#device-plugin-and-unhealthy-devices) for more details.
