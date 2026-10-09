---
document_id: "doc-8a0aaece7ec1b0cc"
source_name: "reference/glossary/configmap.md"
source_type: "text"
source_format: "md"
source_sha256: "bc9bcbba306a03efd6f003c192795e0cf0c858eb03683899ba1c3da94401a540"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/configmap.md"
extracted_sha256: "bc9bcbba306a03efd6f003c192795e0cf0c858eb03683899ba1c3da94401a540"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/configmap.md"
---

---
title: ConfigMap
id: configmap
full_link: /docs/concepts/configuration/configmap/
short_description: >
  An API object used to store non-confidential data in key-value pairs. Can be consumed as environment variables, command-line arguments, or configuration files in a volume.

aka: 
tags:
- core-object
---
 An API object used to store non-confidential data in key-value pairs.
{{< glossary_tooltip text="Pods" term_id="pod" >}} can consume ConfigMaps as
environment variables, command-line arguments, or as configuration files in a
{{< glossary_tooltip text="volume" term_id="volume" >}}.

<!--more--> 

A ConfigMap allows you to decouple environment-specific configuration from your {{< glossary_tooltip text="container images" term_id="image" >}}, so that your applications are easily portable.
