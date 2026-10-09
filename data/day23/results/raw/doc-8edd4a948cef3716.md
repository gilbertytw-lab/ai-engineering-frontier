---
document_id: "doc-8edd4a948cef3716"
source_name: "reference/command-line-tools-reference/feature-gates/ExperimentalCriticalPodAnnotation.md"
source_type: "text"
source_format: "md"
source_sha256: "615db71556e60cd76cb74a82696d462af9ed2d425e9b92af7aa4aaa63279a64a"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/ExperimentalCriticalPodAnnotation.md"
extracted_sha256: "615db71556e60cd76cb74a82696d462af9ed2d425e9b92af7aa4aaa63279a64a"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/ExperimentalCriticalPodAnnotation.md"
---

---
# Removed from Kubernetes
title: ExperimentalCriticalPodAnnotation
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.5"
    toVersion: "1.12"
  - stage: deprecated
    defaultValue: false
    fromVersion: "1.13"
    toVersion: "1.16"

removed: true  
---
Enable annotating specific pods as *critical*
so that their [scheduling is guaranteed](/docs/tasks/administer-cluster/guaranteed-scheduling-critical-addon-pods/).
This feature is deprecated by Pod Priority and Preemption as of v1.13.
