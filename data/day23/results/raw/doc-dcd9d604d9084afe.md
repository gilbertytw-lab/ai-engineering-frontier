---
document_id: "doc-dcd9d604d9084afe"
source_name: "reference/glossary/persistent-volume.md"
source_type: "text"
source_format: "md"
source_sha256: "8ca22e5d2399bac495b3f065f4a357f2dd9b0683d92e57f60bfb51d044b20893"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/persistent-volume.md"
extracted_sha256: "8ca22e5d2399bac495b3f065f4a357f2dd9b0683d92e57f60bfb51d044b20893"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/persistent-volume.md"
---

---
title: Persistent Volume
id: persistent-volume
full_link: /docs/concepts/storage/persistent-volumes/
short_description: >
  API object that represents a piece of storage in the cluster.

aka: 
tags:
- core-object
- storage
---
An API object that represents a piece of storage in the cluster. Representation of as a general, pluggable storage
{{< glossary_tooltip text="resource" term_id="infrastructure-resource" >}} that can persist beyond the lifecycle of any
individual {{< glossary_tooltip text="Pod" term_id="pod" >}}.

<!--more--> 

PersistentVolumes (PVs) provide an API that abstracts details of how storage is provided from how it is consumed.
PVs are used directly in scenarios where storage can be created ahead of time (static provisioning).
For scenarios that require on-demand storage (dynamic provisioning), PersistentVolumeClaims (PVCs) are used instead.
