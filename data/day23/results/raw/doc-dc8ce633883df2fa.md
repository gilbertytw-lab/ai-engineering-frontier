---
document_id: "doc-dc8ce633883df2fa"
source_name: "reference/glossary/cloud-provider.md"
source_type: "text"
source_format: "md"
source_sha256: "62663cb3467bd0b4a13a19e1021c5a883d78709329ee1b8ecfb9ed210b0d4e2b"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/cloud-provider.md"
extracted_sha256: "62663cb3467bd0b4a13a19e1021c5a883d78709329ee1b8ecfb9ed210b0d4e2b"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/cloud-provider.md"
---

---
title: Cloud Provider
id: cloud-provider
short_description: >
  An organization that offers a cloud computing platform.

aka:
- Cloud Service Provider
tags:
- community
---
 A business or other organization that offers a cloud computing platform.

<!--more-->

Cloud providers, sometimes called Cloud Service Providers (CSPs), offer
cloud computing platforms or services.

Many cloud providers offer managed infrastructure (also called
Infrastructure as a Service or IaaS).
With managed infrastructure the cloud provider is responsible for
servers, storage, and networking while you manage layers on top of that
such as running a Kubernetes cluster.

You can also find Kubernetes as a managed service; sometimes called
Platform as a Service, or PaaS. With managed Kubernetes, your
cloud provider is responsible for the Kubernetes control plane as well
as the {{< glossary_tooltip term_id="node" text="nodes" >}} and the
infrastructure they rely on: networking, storage, and possibly other
elements such as load balancers.
