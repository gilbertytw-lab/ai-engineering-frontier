---
document_id: "doc-b3d056f14aac1bcc"
source_name: "reference/glossary/etcd.md"
source_type: "text"
source_format: "md"
source_sha256: "192b430705c8f32688fdf65fad9ad32381ec2ba4a836da38d94e913999b45aef"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/etcd.md"
extracted_sha256: "192b430705c8f32688fdf65fad9ad32381ec2ba4a836da38d94e913999b45aef"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/etcd.md"
---

---
title: etcd
id: etcd
full_link: /docs/tasks/administer-cluster/configure-upgrade-etcd/
short_description: >
  Consistent and highly-available key value store used as backing store of Kubernetes for all cluster data.

aka: 
tags:
- architecture
- storage
---
 Consistent and highly-available key value store used as Kubernetes' backing store for all cluster data.

<!--more-->

If your Kubernetes cluster uses etcd as its backing store, make sure you have a
[back up](/docs/tasks/administer-cluster/configure-upgrade-etcd/#backing-up-an-etcd-cluster) plan
for the data.

You can find in-depth information about etcd in the official [documentation](https://etcd.io/docs/).
