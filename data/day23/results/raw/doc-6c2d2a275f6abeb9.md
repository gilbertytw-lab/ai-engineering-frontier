---
document_id: "doc-6c2d2a275f6abeb9"
source_name: "reference/glossary/cronjob.md"
source_type: "text"
source_format: "md"
source_sha256: "8d946574b6c6e32e5ea665f8eb2987df097e15ac1c776855464d874a7373513f"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/cronjob.md"
extracted_sha256: "8d946574b6c6e32e5ea665f8eb2987df097e15ac1c776855464d874a7373513f"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/cronjob.md"
---

---
title: CronJob
id: cronjob
full_link: /docs/concepts/workloads/controllers/cron-jobs/
short_description: >
  A repeating task (a Job) that runs on a regular schedule.

aka: 
tags:
- core-object
- workload
---
 Manages a [Job](/docs/concepts/workloads/controllers/job/) that runs on a periodic schedule.

<!--more-->

Similar to a line in a *crontab* file, a CronJob object specifies a schedule using the [cron](https://en.wikipedia.org/wiki/Cron) format.
