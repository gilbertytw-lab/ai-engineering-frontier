---
document_id: "doc-89fcb9bdf093e2e1"
source_name: "tasks/configure-pod-container/configure-projected-volume-storage.md"
source_type: "text"
source_format: "md"
source_sha256: "e044f30cdcc285229a2799c7ea3a5037559bd8ea47bbcd8c55d095969a465969"
source_snapshot: "data/day23/source/content/en/docs/tasks/configure-pod-container/configure-projected-volume-storage.md"
extracted_sha256: "e044f30cdcc285229a2799c7ea3a5037559bd8ea47bbcd8c55d095969a465969"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/tasks/configure-pod-container/configure-projected-volume-storage.md"
---

---
reviewers:
- jpeeler
- pmorie
title: Configure a Pod to Use a Projected Volume for Storage
content_type: task
weight: 100
---

<!-- overview -->
This page shows how to use a [`projected`](/docs/concepts/storage/volumes/#projected) Volume to mount
several existing volume sources into the same directory. Currently, `secret`, `configMap`, `downwardAPI`,
and `serviceAccountToken` volumes can be projected.

{{< note >}}
`serviceAccountToken` is not a volume type.
{{< /note >}}


## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}


<!-- steps -->
## Configure a projected volume for a pod

In this exercise, you create username and password {{< glossary_tooltip text="Secrets" term_id="secret" >}} from local files. You then create a Pod that runs one container, using a [`projected`](/docs/concepts/storage/volumes/#projected) Volume to mount the Secrets into the same shared directory.

Here is the configuration file for the Pod:

{{% code_sample file="pods/storage/projected.yaml" %}}

1. Create the Secrets:

    ```shell
    # Create files containing the username and password:
    echo -n "admin" > ./username.txt
    echo -n "1f2d1e2e67df" > ./password.txt

    # Package these files into secrets:
    kubectl create secret generic user --from-file=./username.txt
    kubectl create secret generic pass --from-file=./password.txt
    ```
1. Create the Pod:

    ```shell
    kubectl apply -f https://k8s.io/examples/pods/storage/projected.yaml
    ```
1. Verify that the Pod's container is running, and then watch for changes to
the Pod:

    ```shell
    kubectl get --watch pod test-projected-volume
    ```
    The output looks like this:
    ```
    NAME                    READY     STATUS    RESTARTS   AGE
    test-projected-volume   1/1       Running   0          14s
    ```
1. In another terminal, get a shell to the running container:

    ```shell
    kubectl exec -it test-projected-volume -- /bin/sh
    ```
1. In your shell, verify that the `projected-volume` directory contains your projected sources:

    ```shell
    ls /projected-volume/
    ```

## Clean up

Delete the Pod and the Secrets:

```shell
kubectl delete pod test-projected-volume
kubectl delete secret user pass
```



## {{% heading "whatsnext" %}}

* Learn more about [`projected`](/docs/concepts/storage/volumes/#projected) volumes.
* Read the [all-in-one volume](https://git.k8s.io/design-proposals-archive/node/all-in-one-volume.md) design document.
