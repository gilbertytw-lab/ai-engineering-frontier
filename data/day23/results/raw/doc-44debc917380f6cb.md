---
document_id: "doc-44debc917380f6cb"
source_name: "reference/command-line-tools-reference/feature-gates/PreferSameTrafficDistribution.md"
source_type: "text"
source_format: "md"
source_sha256: "3aaa93b7ad3987b1ce660b974b0c3bb99b3835dd383101f1765d5fccdc94c6c7"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/PreferSameTrafficDistribution.md"
extracted_sha256: "3aaa93b7ad3987b1ce660b974b0c3bb99b3835dd383101f1765d5fccdc94c6c7"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/PreferSameTrafficDistribution.md"
---

---
title: PreferSameTrafficDistribution
content_type: feature_gate

_build:
  list: never
  render: false

stages:
- stage: alpha 
  defaultValue: false
  fromVersion: "1.33"
  toVersion: "1.33"
- stage: beta
  defaultValue: true
  fromVersion: "1.34"
  toVersion: "1.34"
- stage: stable
  defaultValue: true
  locked: true
  fromVersion: "1.35"
---
Allows usage of the values `PreferSameZone` and `PreferSameNode` in
the Service [`trafficDistribution`](/docs/reference/networking/virtual-ips/#traffic-distribution)
field.
