---
document_id: "doc-8a61dccd9974fa51"
source_name: "reference/glossary/docker.md"
source_type: "text"
source_format: "md"
source_sha256: "7cdb9cdd85141d96b7fab07880c582db80c4493a416f8019f99d962396788828"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/docker.md"
extracted_sha256: "7cdb9cdd85141d96b7fab07880c582db80c4493a416f8019f99d962396788828"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/docker.md"
---

---
title: Docker
id: docker
full_link: https://docs.docker.com/engine/
short_description: >
  Docker is a software technology providing operating-system-level virtualization also known as containers.

aka:
tags:
- fundamental
---
Docker (specifically, Docker Engine) is a software technology providing operating-system-level virtualization also known as {{< glossary_tooltip text="containers" term_id="container" >}}.

<!--more-->

Docker uses the resource isolation features of the Linux kernel such as cgroups and kernel namespaces, and a union-capable file system such as OverlayFS and others to allow independent containers to run within a single Linux instance, avoiding the overhead of starting and maintaining virtual machines (VMs).
