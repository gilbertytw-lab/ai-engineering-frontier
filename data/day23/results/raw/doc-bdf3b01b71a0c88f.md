---
document_id: "doc-bdf3b01b71a0c88f"
source_name: "reference/command-line-tools-reference/feature-gates/CRIContainerLogRotation.md"
source_type: "text"
source_format: "md"
source_sha256: "92c116eb4e512e420fc4ef428e6c89748e23b0a2fe41b92b974b25cc223ef455"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/CRIContainerLogRotation.md"
extracted_sha256: "92c116eb4e512e420fc4ef428e6c89748e23b0a2fe41b92b974b25cc223ef455"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/CRIContainerLogRotation.md"
---

---
# Removed from Kubernetes
title: CRIContainerLogRotation
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.10"
    toVersion: "1.10"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.11"
    toVersion: "1.20"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.21"
    toVersion: "1.22"    

removed: true
---
Enable container log rotation for CRI container runtime.
The default max size of a log file is 10MB and the default max number of
log files allowed for a container is 5.
These values can be configured in the kubelet config.
See [logging at node level](/docs/concepts/cluster-administration/logging/#logging-at-the-node-level)
for more details.
