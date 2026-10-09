---
document_id: "doc-18572db7b86abc4c"
source_name: "reference/glossary/spec.md"
source_type: "text"
source_format: "md"
source_sha256: "18a95bc19c8c0af0a99ee8b7ecb2546a46123bef6c081c08dc590506b9b7dd79"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/spec.md"
extracted_sha256: "18a95bc19c8c0af0a99ee8b7ecb2546a46123bef6c081c08dc590506b9b7dd79"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/spec.md"
---

---
title: Spec
id: spec
full_link: /docs/concepts/overview/working-with-objects/#object-spec-and-status
short_description: >
  Field in Kubernetes manifests that defines the desired state or configuration.

aka:
tags:
- fundamental
- architecture
---
  Defines how each object, like Pods or Services, should be configured and its desired state.

<!--more-->
Almost every Kubernetes object includes two nested object fields that govern the object's configuration: the object spec and the object status. For objects that have a spec, you have to set this when you create the object, providing a description of the characteristics you want the {{< glossary_tooltip text="resource" term_id="api-resource" >}} to have: its desired state.

It varies for different objects like Pods, StatefulSets, and Services, detailing settings such as containers, volumes, replicas, ports,
and other specifications unique to each object type. This field encapsulates what state Kubernetes should maintain for the defined
object.
