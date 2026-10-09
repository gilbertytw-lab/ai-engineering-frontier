---
document_id: "doc-9ad40e16d4a9fd22"
source_name: "reference/node/device-plugin-api-versions.md"
source_type: "text"
source_format: "md"
source_sha256: "90d5796e50e37758505c7bbcca3902febc9ede6705a5ef60ed6bda8ba71ecec2"
source_snapshot: "data/day23/source/content/en/docs/reference/node/device-plugin-api-versions.md"
extracted_sha256: "90d5796e50e37758505c7bbcca3902febc9ede6705a5ef60ed6bda8ba71ecec2"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/node/device-plugin-api-versions.md"
---

---
content_type: "reference"
title: Kubelet Device Manager API Versions
weight: 50
---

This page provides details of version compatibility between the Kubernetes
[device plugin API](https://github.com/kubernetes/kubelet/tree/master/pkg/apis/deviceplugin),
and different versions of Kubernetes itself.

## Compatibility matrix

|                 |  `v1alpha1` | `v1beta1`   |
|-----------------|-------------|-------------|
| Kubernetes 1.21 |  -          | ✓           |
| Kubernetes 1.22 |  -          | ✓           |
| Kubernetes 1.23 |  -          | ✓           |
| Kubernetes 1.24 |  -          | ✓           |
| Kubernetes 1.25 |  -          | ✓           |
| Kubernetes 1.26 |  -          | ✓           |

Key:

* `✓` Exactly the same features / API objects in both device plugin API and
   the Kubernetes version.
* `+` The device plugin API has features or API objects that may not be present in the
  Kubernetes cluster, either because the device plugin API has added additional new API
  calls, or that the server has removed an old API call. However, everything they have in
  common (most other APIs) will work. Note that alpha APIs may vanish or
  change significantly between one minor release and the next.
* `-` The Kubernetes cluster has features the device plugin API can't use,
  either because server has added additional API calls, or that device plugin API has
  removed an old API call. However, everything they share in common (most APIs) will work.
