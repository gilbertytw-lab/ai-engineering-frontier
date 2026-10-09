---
document_id: "doc-97ae0af66217d7bf"
source_name: "reference/glossary/container-runtime.md"
source_type: "text"
source_format: "md"
source_sha256: "dd609adc1ead3a059d5f36461b359f927c7aea84562c53e9f1846c0661a43b6e"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/container-runtime.md"
extracted_sha256: "dd609adc1ead3a059d5f36461b359f927c7aea84562c53e9f1846c0661a43b6e"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/container-runtime.md"
---

---
title: Container Runtime
id: container-runtime
full_link: /docs/setup/production-environment/container-runtimes
short_description: >
 The container runtime is the software that is responsible for running containers.

aka:
tags:
- fundamental
- workload
---
 A fundamental component that empowers Kubernetes to run containers effectively.
 It is responsible for managing the execution and lifecycle of containers within the Kubernetes environment.

<!--more-->

Kubernetes supports container runtimes such as
{{< glossary_tooltip term_id="containerd" >}}, {{< glossary_tooltip term_id="cri-o" >}},
and any other implementation of the [Kubernetes CRI (Container Runtime
Interface)](https://github.com/kubernetes/community/blob/main/contributors/devel/sig-node/container-runtime-interface.md).
