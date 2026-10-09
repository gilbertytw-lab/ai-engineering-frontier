---
document_id: "doc-053a8586f57bdeba"
source_name: "reference/command-line-tools-reference/feature-gates/DeclarativeValidation.md"
source_type: "text"
source_format: "md"
source_sha256: "6a3465881e15f134afdfd2b173b5e6763086461f4baff77e31c5d3e37c3c6b7b"
source_snapshot: "data/day23/source/content/en/docs/reference/command-line-tools-reference/feature-gates/DeclarativeValidation.md"
extracted_sha256: "6a3465881e15f134afdfd2b173b5e6763086461f4baff77e31c5d3e37c3c6b7b"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/reference/command-line-tools-reference/feature-gates/DeclarativeValidation.md"
---

---
title: DeclarativeValidation
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.33"
    toVersion: "1.35"
  - stage: stable
    defaultValue: true
    locked: true
    fromVersion: "1.36"
---
Reports differences between declarative validation of in-tree Kubernetes APIs and the
equivalent hand-written validation.

When enabled, rules marked `+k8s:alpha` or `+k8s:beta` run alongside the hand-written
validation, and the API server logs any discrepancy and counts it in the
`declarative_validation_mismatch_total` metric.

This gate controls only reporting, not which result the API server returns. Enforcement
is:

- No prefix: always enforced.
- `+k8s:beta`: enforced when the
  [`DeclarativeValidationBeta` feature gate](/docs/reference/command-line-tools-reference/feature-gates/#DeclarativeValidationBeta)
  is enabled (the default).
- `+k8s:alpha`: never enforced.

This feature gate only operates on the `kube-apiserver` component.
