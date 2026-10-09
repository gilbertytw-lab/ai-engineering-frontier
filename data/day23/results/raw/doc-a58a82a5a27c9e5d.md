---
document_id: "doc-a58a82a5a27c9e5d"
source_name: "reference/command-line-tools-reference/feature-gates/GitRepoVolumeDriver.md"
source_type: "text"
source_format: "md"
source_sha256: "36f4ebba369f1d0be143d11756b8960b56e330e78f7e438055991865bfb5b4e1"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/GitRepoVolumeDriver.md"
extracted_sha256: "36f4ebba369f1d0be143d11756b8960b56e330e78f7e438055991865bfb5b4e1"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/GitRepoVolumeDriver.md"
---

---
title: GitRepoVolumeDriver
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: deprecated
    defaultValue: false
    fromVersion: "1.33"

---
This controls if the `gitRepo` volume plugin is supported or not.
The `gitRepo` volume plugin is disabled by default starting v1.33 release.
This provides a way for users to enable it.
