---
document_id: "doc-a5f87faa7a4e02c9"
source_name: "reference/glossary/sysctl.md"
source_type: "text"
source_format: "md"
source_sha256: "03e9e21d076db069d2ca2a2b098401be6a9239f3c9da3e7aa6041322d40d7533"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/sysctl.md"
extracted_sha256: "03e9e21d076db069d2ca2a2b098401be6a9239f3c9da3e7aa6041322d40d7533"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/sysctl.md"
---

---
title: sysctl
id: sysctl
full_link: /docs/tasks/administer-cluster/sysctl-cluster/
short_description: >
  An interface for getting and setting Unix kernel parameters

aka:
tags:
- tool
---
 `sysctl` is a semi-standardized interface for reading or changing the
 attributes of the running Unix kernel.

<!--more-->

On Unix-like systems, `sysctl` is both the name of the tool that administrators
use to view and modify these settings, and also the system call that the tool
uses.

{{< glossary_tooltip text="Container" term_id="container" >}} runtimes and
network plugins may rely on `sysctl` values being set a certain way.
