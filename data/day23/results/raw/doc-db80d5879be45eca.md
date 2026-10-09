---
document_id: "doc-db80d5879be45eca"
source_name: "reference/command-line-tools-reference/feature-gates/KubeletPodResourcesDynamicResources.md"
source_type: "text"
source_format: "md"
source_sha256: "59d4a16d4906f50571f07a4679ba3c4d86a1520c9f9687d61cd6a84538195712"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/KubeletPodResourcesDynamicResources.md"
extracted_sha256: "59d4a16d4906f50571f07a4679ba3c4d86a1520c9f9687d61cd6a84538195712"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/KubeletPodResourcesDynamicResources.md"
---

---
title: KubeletPodResourcesDynamicResources
content_type: feature_gate
_build:
  list: never
  render: false
  
stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.27"
    toVersion: "1.33"
  - stage: beta
    defaultValue: true
    fromVersion: "1.34"
    toVersion: "1.35"
  - stage: stable
    defaultValue: true
    fromVersion: "1.36"
---
Extend the kubelet's
[pod resources monitoring gRPC API](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/)
endpoints List and Get to include resources allocated in ResourceClaims
via [Dynamic Resource Allocation](/docs/concepts/resource-management/dynamic-resource-allocation/).

Below is an example of GPU metrics to show how this API is consumed by
[NVIDIA dcgm-exporter](https://github.com/NVIDIA/dcgm-exporter) to collect per pod GPU metrics allocated by
[NVIDIA DRA driver](https://github.com/NVIDIA/k8s-dra-driver-gpu):

```
DCGM_FI_PROF_PCIE_RX_BYTES{gpu="0",UUID="GPU-a4f34abc-7715-3560-dcea-7238b9611a45",pci_bus_id="00000009:01:00.0",device="nvidia0",modelName="NVIDIA GH200 96GB HBM3",Hostname="sc-starwars-xxxx",container="ctr",dra_claim_name="single-gpu",dra_claim_namespace="gpu-test3",dra_device_name="gpu-0",dra_driver_name="gpu.nvidia.com",dra_pool_name="sc-starwars-xxxx",namespace="gpu-test3",pod="pod1"} 23792

DCGM_FI_PROF_PCIE_RX_BYTES{gpu="0",UUID="GPU-a4f34abc-7715-3560-dcea-7238b9611a45",pci_bus_id="00000009:01:00.0",device="nvidia0",modelName="NVIDIA GH200 96GB HBM3",Hostname="sc-starwars-xxxx",container="ctr",dra_claim_name="single-gpu",dra_claim_namespace="gpu-test3",dra_device_name="gpu-0",dra_driver_name="gpu.nvidia.com",dra_pool_name="sc-starwars-xxxx",namespace="gpu-test3",pod="pod2"} 23792

with Pod DRA info:

container="ctr",
dra_claim_name="single-gpu",
dra_claim_namespace="gpu-test3",
dra_device_name="gpu-0",dra_driver_name="gpu.nvidia.com",
dra_pool_name="sc-starwars-xxxx",
namespace="gpu-test3",
pod="pod1"
```
