---
document_id: "doc-eeab514bc9a2c98d"
source_name: "reference/command-line-tools-reference/feature-gates/ShardedListAndWatch.md"
source_type: "text"
source_format: "md"
source_sha256: "28a4960410ec889f5d8c553fdf9b5bc4f903222074a6e7fb667028478700b8b2"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/ShardedListAndWatch.md"
extracted_sha256: "28a4960410ec889f5d8c553fdf9b5bc4f903222074a6e7fb667028478700b8b2"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/ShardedListAndWatch.md"
---

---
title: ShardedListAndWatch
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.36"
---
Enable support for the `shardSelector` parameter on **list** and **watch** requests,
allowing clients to receive a filtered subset of objects based on hash ranges of
metadata fields (such as UID). See
[Sharded list and watch](/docs/reference/using-api/api-concepts/#sharded-list-and-watch)
for more details.
