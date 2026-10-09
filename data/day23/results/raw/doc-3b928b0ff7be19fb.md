---
document_id: "doc-3b928b0ff7be19fb"
source_name: "reference/command-line-tools-reference/feature-gates/SidecarContainers.md"
source_type: "text"
source_format: "md"
source_sha256: "963af783c6d33f2ab4a5955b74cd42fb110aa3452d596c4906680537d30bff71"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/SidecarContainers.md"
extracted_sha256: "963af783c6d33f2ab4a5955b74cd42fb110aa3452d596c4906680537d30bff71"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/SidecarContainers.md"
---

---
title: SidecarContainers
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.28"
    toVersion: "1.28"
  - stage: beta
    defaultValue: true
    fromVersion: "1.29"
    toVersion: "1.32"
  - stage: stable
    defaultValue: true
    locked: true
    fromVersion: "1.33"
---
Allow setting the `restartPolicy` of an init container to
`Always` so that the container becomes a sidecar container (restartable init containers).
See [Sidecar containers and restartPolicy](/docs/concepts/workloads/pods/sidecar-containers/)
for more details.
