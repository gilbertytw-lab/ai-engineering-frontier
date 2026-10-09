---
document_id: "doc-9eba32a80f45d45a"
source_name: "tasks/debug/debug-application/debug-statefulset.md"
source_type: "text"
source_format: "md"
source_sha256: "58b7fd144331cdbcc9a939f62076a94a554385eca92c7fde3287e56c693c89d3"
source_snapshot: "data/day23/source/content/en/docs/tasks/debug/debug-application/debug-statefulset.md"
extracted_sha256: "58b7fd144331cdbcc9a939f62076a94a554385eca92c7fde3287e56c693c89d3"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/tasks/debug/debug-application/debug-statefulset.md"
---

---
reviewers:
- bprashanth
- enisoc
- erictune
- foxish
- janetkuo
- kow3ns
- smarterclayton
title: Debug a StatefulSet
content_type: task
weight: 30
---

<!-- overview -->
This task shows you how to debug a StatefulSet.

## {{% heading "prerequisites" %}}

* You need to have a Kubernetes cluster, and the kubectl command-line tool must be configured to communicate with your cluster.
* You should have a StatefulSet running that you want to investigate.

<!-- steps -->

## Debugging a StatefulSet

In order to list all the pods which belong to a StatefulSet, which have a label `app.kubernetes.io/name=MyApp` set on them,
you can use the following:

```shell
kubectl get pods -l app.kubernetes.io/name=MyApp
```

If you find that any Pods listed are in `Unknown` or `Terminating` state for an extended period of time,
refer to the [Deleting StatefulSet Pods](/docs/tasks/run-application/delete-stateful-set/) task for
instructions on how to deal with them.
You can debug individual Pods in a StatefulSet using the
[Debugging Pods](/docs/tasks/debug/debug-application/debug-pods/) guide.

## {{% heading "whatsnext" %}}

Learn more about [debugging an init-container](/docs/tasks/debug/debug-application/debug-init-containers/).
