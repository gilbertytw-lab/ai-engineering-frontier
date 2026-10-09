---
document_id: "doc-4da034ab4b52f6ac"
source_name: "reference/scheduling/policies.md"
source_type: "text"
source_format: "md"
source_sha256: "45ffc2dc20b1db3be1121be8d78a7cbd32d432cd166a3fa3f718fbb889947984"
source_snapshot: "data/day23/source/content/en/docs/reference/scheduling/policies.md"
extracted_sha256: "45ffc2dc20b1db3be1121be8d78a7cbd32d432cd166a3fa3f718fbb889947984"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/scheduling/policies.md"
---

---
title: Scheduling Policies
content_type: concept
sitemap:
  priority: 0.2 # Scheduling priorities are deprecated
weight: 30
---

<!-- overview -->

In Kubernetes versions before v1.23, a scheduling policy can be used to specify the *predicates* and *priorities* process. For example, you can set a scheduling policy by
running `kube-scheduler --policy-config-file <filename>` or `kube-scheduler --policy-configmap <ConfigMap>`.

This scheduling policy is not supported since Kubernetes v1.23. Associated flags `policy-config-file`, `policy-configmap`, `policy-configmap-namespace` and `use-legacy-policy-config` are also not supported. Instead, use the [Scheduler Configuration](/docs/reference/scheduling/config/) to achieve similar behavior.

## {{% heading "whatsnext" %}}

* Learn about [scheduling](/docs/concepts/scheduling-eviction/kube-scheduler/)
* Learn about [kube-scheduler Configuration](/docs/reference/scheduling/config/)
* Read the [kube-scheduler configuration reference (v1)](/docs/reference/config-api/kube-scheduler-config.v1/)
