---
document_id: "doc-f2de2b86dc10d6cc"
source_name: "reference/command-line-tools-reference/feature-gates/ConsistentListFromCache.md"
source_type: "text"
source_format: "md"
source_sha256: "d3cff6b4aeba78cd80e9b6804e15b190995c67fcfe1845b2feba3f0dbc44345c"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/ConsistentListFromCache.md"
extracted_sha256: "d3cff6b4aeba78cd80e9b6804e15b190995c67fcfe1845b2feba3f0dbc44345c"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/ConsistentListFromCache.md"
---

---
title: ConsistentListFromCache
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.28"
    toVersion: "1.30"
  - stage: beta
    defaultValue: true
    fromVersion: "1.31"
    toVersion: "1.33"
  - stage: stable
    defaultValue: true
    fromVersion: "1.34"

---
Enhance Kubernetes API server performance by serving consistent **list** requests
directly from its watch cache, improving scalability and response times.
To consistent list from cache Kubernetes requires a newer etcd version (v3.4.31+ or v3.5.13+),
that includes fixes to watch progress request feature.
If older etcd version is provided Kubernetes will automatically detect it and fallback to serving consistent reads from etcd.
Progress notifications ensure watch cache is consistent with etcd while reducing
the need for resource-intensive quorum reads from etcd.

See the Kubernetes documentation on [Semantics for **get** and **list**](/docs/reference/using-api/api-concepts/#semantics-for-get-and-list) for more details.
