---
document_id: "doc-9e009c35ed5d2aa5"
source_name: "reference/command-line-tools-reference/feature-gates/SELinuxMountReadWriteOncePod.md"
source_type: "text"
source_format: "md"
source_sha256: "e8db489953ff727ebbdc6aa033a3762f0b9197caea4ac420c991f298af1a9512"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/SELinuxMountReadWriteOncePod.md"
extracted_sha256: "e8db489953ff727ebbdc6aa033a3762f0b9197caea4ac420c991f298af1a9512"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/SELinuxMountReadWriteOncePod.md"
---

---
title: SELinuxMountReadWriteOncePod
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.25"
    toVersion: "1.26"
  - stage: beta
    defaultValue: false
    fromVersion: "1.27"
    toVersion: "1.27"
  - stage: beta
    defaultValue: true
    fromVersion: "1.28"
    toVersion: "1.35"
  - stage: stable
    defaultValue: true
    fromVersion: "1.36"
---
Speeds up container startup by allowing kubelet to mount volumes
for a Pod directly with the correct SELinux label instead of changing each file on the volumes
recursively. The initial implementation focused on ReadWriteOncePod volumes.
