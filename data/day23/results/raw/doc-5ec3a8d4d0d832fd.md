---
document_id: "doc-5ec3a8d4d0d832fd"
source_name: "reference/command-line-tools-reference/feature-gates/DRAConsumableCapacity.md"
source_type: "text"
source_format: "md"
source_sha256: "b3264908f3c7a14a210a437c6980ff2bb887015024259c4ed72babb46e70e6bf"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/DRAConsumableCapacity.md"
extracted_sha256: "b3264908f3c7a14a210a437c6980ff2bb887015024259c4ed72babb46e70e6bf"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/DRAConsumableCapacity.md"
---

---
title: DRAConsumableCapacity
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.34"
    toVersion: "1.35"
  - stage: beta
    defaultValue: true
    fromVersion: "1.36"
---
Enables device sharing across multiple ResourceClaims or requests.

Additionally, if a device supports sharing, its resource (capacity) can be managed through a defined sharing policy.
