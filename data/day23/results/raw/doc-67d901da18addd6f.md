---
document_id: "doc-67d901da18addd6f"
source_name: "reference/command-line-tools-reference/feature-gates/StorageVersionMigrator.md"
source_type: "text"
source_format: "md"
source_sha256: "409d4bf2b868d71a2a9e8d644c8e2289df6945e0225d73c14c27e4a291e252c7"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/StorageVersionMigrator.md"
extracted_sha256: "409d4bf2b868d71a2a9e8d644c8e2289df6945e0225d73c14c27e4a291e252c7"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/StorageVersionMigrator.md"
---

---
title: StorageVersionMigrator
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.30"
    toVersion: "1.34"
  - stage: beta 
    defaultValue: false
    fromVersion: "1.35"
---
Enables the migration of the [storage
version](/docs/concepts/overview/working-with-objects/storage-version) of a
resource. 
