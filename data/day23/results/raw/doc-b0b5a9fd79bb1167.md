---
document_id: "doc-b0b5a9fd79bb1167"
source_name: "reference/glossary/kubernetes-api.md"
source_type: "text"
source_format: "md"
source_sha256: "92d9da0909314221bd6a5817382caf74f24882894ac414740cd105013dd77f8e"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/kubernetes-api.md"
extracted_sha256: "92d9da0909314221bd6a5817382caf74f24882894ac414740cd105013dd77f8e"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/kubernetes-api.md"
---

---
title: Kubernetes API
id: kubernetes-api
full_link: /docs/concepts/overview/kubernetes-api/
short_description: >
  The application that serves Kubernetes functionality through a RESTful interface and stores the state of the cluster.

aka: 
tags:
- fundamental
- architecture
---
 The application that serves Kubernetes functionality through a RESTful interface and stores the state of the cluster.

<!--more--> 

Kubernetes resources and "records of intent" are all stored as API objects, and modified via RESTful calls to the API. The API allows configuration to be managed in a declarative way. Users can interact with the Kubernetes API directly, or via tools like `kubectl`. The core Kubernetes API is flexible and can also be extended to support custom resources.
