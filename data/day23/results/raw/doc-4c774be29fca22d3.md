---
document_id: "doc-4c774be29fca22d3"
source_name: "reference/glossary/cdi.md"
source_type: "text"
source_format: "md"
source_sha256: "073f5f8391463c1ebf1920b6875dcb2c7ece59250aa1e0fcbfdc6382d6f46198"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/cdi.md"
extracted_sha256: "073f5f8391463c1ebf1920b6875dcb2c7ece59250aa1e0fcbfdc6382d6f46198"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/cdi.md"
---

---
title: Container Device Interface (CDI)
id: cdi
full_link: /docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/
short_description: >
  A CNCF specification for describing device configuration that container runtimes
  apply when creating containers.

aka:
tags:
- extension
---
The Container Device Interface (CDI) is a specification for how to configure
devices inside containers. Kubernetes uses CDI together with device plugins and
with Dynamic Resource Allocation so that workloads receive device setup such as
bind mounts or environment variables from the runtime.

<!--more-->

* [Device Plugins](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/)
* [Container Device Interface](https://github.com/cncf-tags/container-device-interface)
  specification repository
