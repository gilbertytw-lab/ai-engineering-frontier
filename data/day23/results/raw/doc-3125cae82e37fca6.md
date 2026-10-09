---
document_id: "doc-3125cae82e37fca6"
source_name: "reference/glossary/app-container.md"
source_type: "text"
source_format: "md"
source_sha256: "5938778e5f3244a015dd286f79d0b78619d93d792a0889aadd80d3a97261202f"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/app-container.md"
extracted_sha256: "5938778e5f3244a015dd286f79d0b78619d93d792a0889aadd80d3a97261202f"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/app-container.md"
---

---
title: App Container
id: app-container
full_link:
short_description: >
  A container used to run part of a workload. Compare with init container.

aka:
tags:
- workload
---
 Application containers (or app containers) are the {{< glossary_tooltip text="containers" term_id="container" >}} in a {{< glossary_tooltip text="pod" term_id="pod" >}} that are started after any {{< glossary_tooltip text="init containers" term_id="init-container" >}} have completed.

<!--more-->

An init container lets you separate initialization details that are important for the overall 
{{< glossary_tooltip text="workload" term_id="workload" >}}, and that don't need to keep running
once the application container has started.
If a pod doesn't have any init containers configured, all the containers in that pod are app containers.
