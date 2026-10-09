---
document_id: "doc-0faf5c25249cb6ee"
source_name: "reference/command-line-tools-reference/feature-gates-removed/index.md"
source_type: "text"
source_format: "md"
source_sha256: "1660f03fe813789c76c655e55062ffeb9bc0cc2cb196e9273cf10be7e59c820f"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates-removed/index.md"
extracted_sha256: "1660f03fe813789c76c655e55062ffeb9bc0cc2cb196e9273cf10be7e59c820f"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates-removed/index.md"
---

---
title: Feature Gates (removed)
weight: 15
content_type: concept
---

<!-- overview -->

This page contains list of feature gates that have been removed. The information on this page is for reference.
A removed feature gate is different from a GA'ed or deprecated one in that a removed one is
no longer recognized as a valid feature gate.
However, a GA'ed or a deprecated feature gate is still recognized by the corresponding Kubernetes
components although they are unable to cause any behavior differences in a cluster.

For feature gates that are still recognized by the Kubernetes components, please refer to
the [Alpha/Beta feature gate table](/docs/reference/command-line-tools-reference/feature-gates/#feature-gates-for-alpha-or-beta-features)
or the [Graduated/Deprecated feature gate table](/docs/reference/command-line-tools-reference/feature-gates/#feature-gates-for-graduated-or-deprecated-features)

### Feature gates that are removed

In the following table:

- The "From" column contains the Kubernetes release when a feature is introduced
  or its release stage is changed.
- The "To" column, if not empty, contains the last Kubernetes release in which
  you can still use a feature gate. If the feature stage is either "Deprecated"
  or "GA", the "To" column is the Kubernetes release when the feature is removed.

<!-- Want to edit this table? See https://k8s.io/docs/contribute/new-content/new-features/#ready-for-review-feature-gates -->
{{< feature-gate-table show-removed="true" caption="Feature Gates Removed" sortable="true" >}}

## Descriptions for removed feature gates

<!-- Want to edit this list? See https://k8s.io/docs/contribute/new-content/new-features/#ready-for-review-feature-gates -->
{{< feature-gate-list show-removed="true" >}}
