---
document_id: "doc-bc2d03aba19a5475"
source_name: "reference/glossary/resourceclaimtemplate.md"
source_type: "text"
source_format: "md"
source_sha256: "1d417f89817690fa9f429f09dbe76efb5e87088b93c4c254f784a7cc4e76080c"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/resourceclaimtemplate.md"
extracted_sha256: "1d417f89817690fa9f429f09dbe76efb5e87088b93c4c254f784a7cc4e76080c"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/resourceclaimtemplate.md"
---

---
title: ResourceClaimTemplate
id: resourceclaimtemplate
full_link: /docs/concepts/resource-management/dynamic-resource-allocation/dra-api/#resourceclaims-templates
short_description: >
  Defines a template for Kubernetes to create ResourceClaims. Used to provide
  per-Pod or per-PodGroup access to separate, similar resources.

tags:
- workload
---
 Defines a template that Kubernetes uses to create
{{< glossary_tooltip text="ResourceClaims" term_id="resourceclaim" >}}.
ResourceClaimTemplates are used in
[dynamic resource allocation (DRA)](/docs/concepts/resource-management/dynamic-resource-allocation/)
to provide _per-Pod or per-{{< glossary_tooltip text="PodGroup" term_id="podgroup" >}} access to separate, similar resources_.

<!--more-->

When a ResourceClaimTemplate is referenced in a workload specification,
Kubernetes automatically creates ResourceClaim objects based on the template.
Each ResourceClaim is bound to a specific Pod or PodGroup. When the Pod
terminates or the PodGroup is deleted, Kubernetes deletes the corresponding
ResourceClaim. PodGroup ResourceClaimTemplates require the
[`DRAWorkloadResourceClaims`](/docs/reference/command-line-tools-reference/feature-gates/#DRAWorkloadResourceClaims)
feature to be enabled.
