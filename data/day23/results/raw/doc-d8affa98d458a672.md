---
document_id: "doc-d8affa98d458a672"
source_name: "reference/command-line-tools-reference/feature-gates/CoordinatedLeaderElection.md"
source_type: "text"
source_format: "md"
source_sha256: "47f80b2d5bc533c177d1198939752619c628500b522a40f891f3dbe6df14a826"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/CoordinatedLeaderElection.md"
extracted_sha256: "47f80b2d5bc533c177d1198939752619c628500b522a40f891f3dbe6df14a826"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/CoordinatedLeaderElection.md"
---

---
title: CoordinatedLeaderElection
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.31"
    toVersion: "1.32"
  - stage: beta
    defaultValue: false
    fromVersion: "1.33"
---
Enables the behaviors supporting the LeaseCandidate API, and also enables
coordinated leader election for the Kubernetes control plane, deterministically.
