---
document_id: "doc-65df5212bec579ee"
source_name: "reference/command-line-tools-reference/feature-gates/ElasticIndexedJob.md"
source_type: "text"
source_format: "md"
source_sha256: "9ada2f2dc99ae7f52dfd8eaab27761497124cee60517599a6e5ca3f269e5a2ea"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/ElasticIndexedJob.md"
extracted_sha256: "9ada2f2dc99ae7f52dfd8eaab27761497124cee60517599a6e5ca3f269e5a2ea"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/ElasticIndexedJob.md"
---

---
title: ElasticIndexedJob
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.27"
    toVersion: "1.30"
  - stage: stable
    defaultValue: true
    fromVersion: "1.31"
---
Enables Indexed Jobs to be scaled up or down by mutating both
`spec.completions` and `spec.parallelism` together such that `spec.completions == spec.parallelism`.
See docs on [elastic Indexed Jobs](/docs/concepts/workloads/controllers/job#elastic-indexed-jobs)
for more details.
