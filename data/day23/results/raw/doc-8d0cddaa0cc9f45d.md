---
document_id: "doc-8d0cddaa0cc9f45d"
source_name: "reference/glossary/job.md"
source_type: "text"
source_format: "md"
source_sha256: "291c47006c2b4b1783a224457383195f3cdb5ec3eec66372d5ce6fe525fc0077"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/job.md"
extracted_sha256: "291c47006c2b4b1783a224457383195f3cdb5ec3eec66372d5ce6fe525fc0077"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/job.md"
---

---
title: Job
id: job
full_link: /docs/concepts/workloads/controllers/job/
short_description: >
  A finite or batch task that runs to completion.

aka: 
tags:
- fundamental
- core-object
- workload
---
 A finite or batch task that runs to completion.

<!--more--> 

Creates one or more {{< glossary_tooltip term_id="pod" >}} objects and ensures that a specified number of them successfully terminate. As Pods successfully complete, the Job tracks the successful completions.
