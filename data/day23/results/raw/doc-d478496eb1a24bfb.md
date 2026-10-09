---
document_id: "doc-d478496eb1a24bfb"
source_name: "reference/glossary/device.md"
source_type: "text"
source_format: "md"
source_sha256: "f628fb52ca831be69c8f951ebd1b48a7f8c55d02ad415b62924a9dc97527e26e"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/device.md"
extracted_sha256: "f628fb52ca831be69c8f951ebd1b48a7f8c55d02ad415b62924a9dc97527e26e"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/device.md"
---

---
title: Device
id: device
short_description: >
  Any resource that's directly or indirectly attached your cluster's nodes, like
  GPUs or circuit boards.

tags:
- extension
- fundamental
---
 One or more
{{< glossary_tooltip text="infrastructure resources" term_id="infrastructure-resource" >}}
that are directly or indirectly attached to your
{{< glossary_tooltip text="nodes" term_id="node" >}}.

<!--more-->

Devices might be commercial products like GPUs, or custom hardware like
[ASIC boards](https://en.wikipedia.org/wiki/Application-specific_integrated_circuit).
Attached devices usually require device drivers that let Kubernetes
{{< glossary_tooltip text="Pods" term_id="pod" >}} access the devices.
