---
document_id: "doc-54dea7afb67696f0"
source_name: "reference/command-line-tools-reference/feature-gates/ControllerManagerLeaderMigration.md"
source_type: "text"
source_format: "md"
source_sha256: "60545a3cc40a5bd2854b9f56fe330914a8f43365bc767ab9103a6d9005c7542d"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/ControllerManagerLeaderMigration.md"
extracted_sha256: "60545a3cc40a5bd2854b9f56fe330914a8f43365bc767ab9103a6d9005c7542d"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/ControllerManagerLeaderMigration.md"
---

---
# Removed from Kubernetes
title: ControllerManagerLeaderMigration
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
    toVersion: "1.23"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.24"
    toVersion: "1.26"

removed: true  
---
Enables Leader Migration for
[kube-controller-manager](/docs/tasks/administer-cluster/controller-manager-leader-migration/#initial-leader-migration-configuration) and
[cloud-controller-manager](/docs/tasks/administer-cluster/controller-manager-leader-migration/#deploy-cloud-controller-manager)
which allows a cluster operator to live migrate
controllers from the kube-controller-manager into an external controller-manager
(e.g. the cloud-controller-manager) in an HA cluster without downtime.
