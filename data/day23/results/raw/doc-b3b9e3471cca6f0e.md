---
document_id: "doc-b3b9e3471cca6f0e"
source_name: "reference/glossary/replication-controller.md"
source_type: "text"
source_format: "md"
source_sha256: "b0e51341fd83c219d28b3badaaa2e3b255d0c0deb50a832ebcee59d5d8ddf182"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/replication-controller.md"
extracted_sha256: "b0e51341fd83c219d28b3badaaa2e3b255d0c0deb50a832ebcee59d5d8ddf182"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/replication-controller.md"
---

---
title: ReplicationController
id: replication-controller
full_link: 
short_description: >
  A (deprecated) API object that manages a replicated application.

aka: 
tags:
- workload
- core-object
---
A workload management {{< glossary_tooltip text="object" term_id="object" >}}
that manages a replicated application, ensuring that
a specific number of instances of a {{< glossary_tooltip text="Pod" term_id="pod" >}} are running.

<!--more-->

The control plane ensures that the defined number of Pods are running, even if some
Pods fail, if you delete Pods manually, or if too many are started by mistake.

{{< note >}}
ReplicationController is deprecated. See
{{< glossary_tooltip text="Deployment" term_id="deployment" >}}, which is similar.
{{< /note >}}
