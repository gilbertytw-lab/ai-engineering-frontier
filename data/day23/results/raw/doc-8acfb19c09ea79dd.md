---
document_id: "doc-8acfb19c09ea79dd"
source_name: "reference/config-api/apiserver-webhookadmission.v1.md"
source_type: "text"
source_format: "md"
source_sha256: "daa6782dc533888c4d2b757a897d22257ea5bf8a5c7ed2e06f3565096849dab8"
source_snapshot: "data/day23/source/content/en/docs/reference/config-api/apiserver-webhookadmission.v1.md"
extracted_sha256: "daa6782dc533888c4d2b757a897d22257ea5bf8a5c7ed2e06f3565096849dab8"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/config-api/apiserver-webhookadmission.v1.md"
---

---
title: WebhookAdmission Configuration (v1)
content_type: tool-reference
package: apiserver.config.k8s.io/v1
auto_generated: true
---
<p>Package v1 is the v1 version of the API.</p>


## Resource Types 


- [WebhookAdmission](#apiserver-config-k8s-io-v1-WebhookAdmission)
  

## `WebhookAdmission`     {#apiserver-config-k8s-io-v1-WebhookAdmission}
    


<p>WebhookAdmission provides configuration for the webhook admission controller.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>apiserver.config.k8s.io/v1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>WebhookAdmission</code></td></tr>
    
  
<tr><td><code>kubeConfigFile</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>KubeConfigFile is the path to the kubeconfig file.</p>
</td>
</tr>
<tr><td><code>staticManifestsDir</code><br/>
<code>string</code>
</td>
<td>
   <p>StaticManifestsDir is the path to a directory containing static webhook
configurations to be loaded at startup. Files with extensions .yaml,
.yml, and .json are read. Only admissionregistration.k8s.io/v1
ValidatingWebhookConfiguration and MutatingWebhookConfiguration
resources are supported.
Using this field requires the ManifestBasedAdmissionControlConfig
feature gate to be enabled.</p>
</td>
</tr>
</tbody>
</table>
  
