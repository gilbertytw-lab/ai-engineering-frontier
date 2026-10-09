---
document_id: "doc-bc63cfeae5b3b216"
source_name: "reference/glossary/rbac.md"
source_type: "text"
source_format: "md"
source_sha256: "4e732c1bf6c9b20c51870774e78f9ec6de63b8cd5d387b9a2a424e534f3f0ab8"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/rbac.md"
extracted_sha256: "4e732c1bf6c9b20c51870774e78f9ec6de63b8cd5d387b9a2a424e534f3f0ab8"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/rbac.md"
---

---
title: RBAC (Role-Based Access Control)
id: rbac
full_link: /docs/reference/access-authn-authz/rbac/
short_description: >
  Manages authorization decisions, allowing admins to dynamically configure access policies through the Kubernetes API.

aka: 
tags:
- security
- fundamental
---
 Manages authorization decisions, allowing admins to dynamically configure access policies through the {{< glossary_tooltip text="Kubernetes API" term_id="kubernetes-api" >}}.

<!--more--> 

RBAC utilizes four kinds of Kubernetes objects:

Role
: Defines permission rules in a specific namespace.

ClusterRole
: Defines permission rules cluster-wide.

RoleBinding
: Grants the permissions defined in a role to a set of users in a specific namespace.

ClusterRoleBinding
: Grants the permissions defined in a role to a set of users cluster-wide.

For more information, see [RBAC](/docs/reference/access-authn-authz/rbac/).
