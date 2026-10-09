---
document_id: "doc-f648720bcddf173d"
source_name: "reference/command-line-tools-reference/feature-gates/AnyVolumeDataSource.md"
source_type: "text"
source_format: "md"
source_sha256: "f7bc49e20deb5b2fff9d225f13255910d125de4f7f546658b3620fd0840f1ff5"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/AnyVolumeDataSource.md"
extracted_sha256: "f7bc49e20deb5b2fff9d225f13255910d125de4f7f546658b3620fd0840f1ff5"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/AnyVolumeDataSource.md"
---

---
title: AnyVolumeDataSource
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.18"
    toVersion: "1.23"
  - stage: beta
    defaultValue: true
    fromVersion: "1.24"
    toVersion: "1.32"
  - stage: stable
    defaultValue: true
    fromVersion: "1.33"
    locked: true
---
Enable use of any custom resource as the `DataSource` of a
{{< glossary_tooltip text="PVC" term_id="persistent-volume-claim" >}}.
