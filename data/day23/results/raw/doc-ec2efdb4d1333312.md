---
document_id: "doc-ec2efdb4d1333312"
source_name: "reference/glossary/horizontal-pod-autoscaler.md"
source_type: "text"
source_format: "md"
source_sha256: "61687e8e89fa218ebf99fb8524d34a4df3fdd7fa7dec033510195c74e6c99566"
source_snapshot: "data/day23/source/content/en/docs/reference/glossary/horizontal-pod-autoscaler.md"
extracted_sha256: "61687e8e89fa218ebf99fb8524d34a4df3fdd7fa7dec033510195c74e6c99566"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/glossary/horizontal-pod-autoscaler.md"
---

---
title: Horizontal Pod Autoscaler
id: horizontal-pod-autoscaler
full_link: docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
short_description: >
  Object that automatically scales the number of pod replicas based on targeted resource utilization or custom metric targets.

aka: 
- HPA
tags:
- operation
---
An {{< glossary_tooltip text="object" term_id="object" >}} that automatically scales the number of {{< glossary_tooltip term_id="pod" >}} replicas,
based on targeted {{< glossary_tooltip text="resource" term_id="infrastructure-resource" >}} utilization or custom metric targets.

<!--more--> 

HorizontalPodAutoscaler (HPA) is typically used with {{< glossary_tooltip text="Deployments" term_id="deployment" >}}, or {{< glossary_tooltip text="ReplicaSets" term_id="replica-set" >}}. It cannot be applied to objects that cannot be scaled, for example {{< glossary_tooltip text="DaemonSets" term_id="daemonset" >}}.
