---
document_id: "doc-1986c3bcbee7eda2"
source_name: "reference/command-line-tools-reference/feature-gates/MemoryManager.md"
source_type: "text"
source_format: "md"
source_sha256: "305f834638f4edbeaecf874efa52b4eadbc60f1c933f5c21d70761800584f8af"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/MemoryManager.md"
extracted_sha256: "305f834638f4edbeaecf874efa52b4eadbc60f1c933f5c21d70761800584f8af"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/MemoryManager.md"
---

---
title: MemoryManager
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.21"
    toVersion: "1.21"
  - stage: beta
    defaultValue: true
    fromVersion: "1.22"
    toVersion: "1.31"
  - stage: stable
    defaultValue: true
    fromVersion: "1.32"
---
Allows setting memory affinity for a container based on
NUMA topology.
