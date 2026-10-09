---
document_id: "doc-2c406a7aa27d2de5"
source_name: "reference/glossary/limitrange.md"
source_type: "text"
source_format: "md"
source_sha256: "5a2fc9af1626bcef10760115700317ac7e7886e5c66e8c5bc6aa18ed400c05ff"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/limitrange.md"
extracted_sha256: "5a2fc9af1626bcef10760115700317ac7e7886e5c66e8c5bc6aa18ed400c05ff"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/limitrange.md"
---

---
title: LimitRange
id: limitrange
full_link:  /docs/concepts/policy/limit-range/
short_description: >
  Provides constraints to limit resource consumption per Containers or Pods in a namespace.

aka: 
tags:
- core-object
- fundamental
- architecture
related:
 - pod
 - container

---
Constraints resource consumption per {{< glossary_tooltip text="container" term_id="container" >}} or {{< glossary_tooltip text="Pod" term_id="pod" >}},
specified for a particular {{< glossary_tooltip text="namespace" term_id="namespace" >}}.

<!--more--> 

A [LimitRange](/docs/concepts/policy/limit-range/) either limits the quantity of {{< glossary_tooltip text="API resources" term_id="api-resource" >}}
that can be created (for a particular resource type),
or the amount of {{< glossary_tooltip text="infrastructure resources" term_id="infrastructure-resource" >}}
that may be requested/consumed by individual containers or Pods within a namespace.
