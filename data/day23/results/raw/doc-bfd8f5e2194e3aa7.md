---
document_id: "doc-bfd8f5e2194e3aa7"
source_name: "concepts/security/pod-security-policy.md"
source_type: "text"
source_format: "md"
source_sha256: "dc3a62de40d3c99493f5af99867a686a8fd7f58aa2b33556c815ab6757e80a8b"
source_snapshot: "data/day23/source/content/en/docs/concepts/security/pod-security-policy.md"
extracted_sha256: "dc3a62de40d3c99493f5af99867a686a8fd7f58aa2b33556c815ab6757e80a8b"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/concepts/security/pod-security-policy.md"
---

---
title: Pod Security Policies
content_type: concept
weight: 30
---

<!-- overview -->

{{% alert title="Removed feature" color="warning" %}}
PodSecurityPolicy was [deprecated](/blog/2021/04/08/kubernetes-1-21-release-announcement/#podsecuritypolicy-deprecation)
in Kubernetes v1.21, and removed from Kubernetes in v1.25.
{{% /alert %}}

Instead of using PodSecurityPolicy, you can enforce similar restrictions on Pods using
either or both:

- [Pod Security Admission](/docs/concepts/security/pod-security-admission/)
- a 3rd party admission plugin, that you deploy and configure yourself

For a migration guide, see [Migrate from PodSecurityPolicy to the Built-In PodSecurity Admission Controller](/docs/tasks/configure-pod-container/migrate-from-psp/).
For more information on the removal of this API,
see [PodSecurityPolicy Deprecation: Past, Present, and Future](/blog/2021/04/06/podsecuritypolicy-deprecation-past-present-and-future/).

If you are not running Kubernetes v{{< skew currentVersion >}}, check the documentation for
your version of Kubernetes.
