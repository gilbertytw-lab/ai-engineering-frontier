---
document_id: "doc-819edbe9a7eae459"
source_name: "reference/kubernetes-api/definitions/self-subject-access-review-v1-authorization.md"
source_type: "text"
source_format: "md"
source_sha256: "d28383d48a164be7503e85ef37323a3cf6a04afd161d60b48128bb049891be12"
source_snapshot: "data/day23/source/content/en/docs/reference/kubernetes-api/definitions/self-subject-access-review-v1-authorization.md"
extracted_sha256: "d28383d48a164be7503e85ef37323a3cf6a04afd161d60b48128bb049891be12"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/kubernetes-api/definitions/self-subject-access-review-v1-authorization.md"
---

---
api_metadata:
  apiVersion: "authorization.k8s.io/v1"
  import: "k8s.io/api/authorization/v1"
  kind: "SelfSubjectAccessReview"
content_type: "api_reference"
description: "SelfSubjectAccessReview checks whether or the current user can perform an action.  Not filling in a spec.namespace means &#34;in all namespaces&#34;.  Self is a special case, because users should always be able to check whether they can perform an action"
title: "SelfSubjectAccessReview"
weight: 450
auto_generated: true
---

<!--
The file is auto-generated from the Go source code of the component using a generic
[generator](https://github.com/kubernetes-sigs/reference-docs/). To learn how
to generate the reference documentation, please read
[Contributing to the reference documentation](/docs/contribute/generate-ref-docs/).
To update the reference content, please follow the
[Contributing upstream](/docs/contribute/generate-ref-docs/contribute-upstream/)
guide. You can file document formatting bugs against the
[reference-docs](https://github.com/kubernetes-sigs/reference-docs/) project.
-->

`apiVersion: authorization.k8s.io/v1`

`import "k8s.io/api/authorization/v1"`


## SelfSubjectAccessReview {#SelfSubjectAccessReview}

SelfSubjectAccessReview checks whether or the current user can perform an action.  Not filling in a spec.namespace means &#34;in all namespaces&#34;.  Self is a special case, because users should always be able to check whether they can perform an action

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "object-meta-v1-meta#ObjectMeta" >}}">ObjectMeta</a></em></td>
      <td>metadata is the standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</td>
    </tr>
    <tr>
      <td><code>spec</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#SelfSubjectAccessReviewSpec" >}}">SelfSubjectAccessReviewSpec</a></em></td>
      <td>spec holds information about the request being evaluated.  user and groups must be empty</td>
    </tr>
    <tr>
      <td><code>status</code><br/><em>SubjectAccessReviewStatus</em></td>
      <td>status is filled in by the server and indicates whether the request is allowed or not</td>
    </tr>
  </tbody>
</table>


## SelfSubjectAccessReviewSpec {#SelfSubjectAccessReviewSpec}

SelfSubjectAccessReviewSpec is a description of the access request.  Exactly one of resourceAttributes and nonResourceAttributes must be set

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>nonResourceAttributes</code><br/><em><a href="{{< ref "non-resource-attributes-v1-authorization#NonResourceAttributes" >}}">NonResourceAttributes</a></em></td>
      <td>nonResourceAttributes describes information for a non-resource access request</td>
    </tr>
    <tr>
      <td><code>resourceAttributes</code><br/><em><a href="{{< ref "resource-attributes-v1-authorization#ResourceAttributes" >}}">ResourceAttributes</a></em></td>
      <td>resourceAttributes describes information for a resource access request</td>
    </tr>
  </tbody>
</table>
