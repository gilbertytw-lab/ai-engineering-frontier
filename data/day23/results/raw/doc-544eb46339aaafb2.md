---
document_id: "doc-544eb46339aaafb2"
source_name: "tasks/tools/included/optional-kubectl-configs-zsh.md"
source_type: "text"
source_format: "md"
source_sha256: "12adfd8a47948022b85e9b6aa9d7fee9550fc6fa7d04a120acd63ab6820e9041"
source_snapshot: "data/day23/source/content/en/docs/tasks/tools/included/optional-kubectl-configs-zsh.md"
extracted_sha256: "12adfd8a47948022b85e9b6aa9d7fee9550fc6fa7d04a120acd63ab6820e9041"
conversion_method: "programmatic"
converter_version: "0.3.0"
source_url: "https://github.com/kubernetes/website/blob/77db41e9c776b614fdb31de4cc6c8e9a70673817/content/en/docs/tasks/tools/included/optional-kubectl-configs-zsh.md"
---

---
title: "zsh auto-completion"
description: "Some optional configuration for zsh auto-completion."
headless: true
_build:
  list: never
  render: never
  publishResources: false
---

The kubectl completion script for Zsh can be generated with the command `kubectl completion zsh`. Sourcing the completion script in your shell enables kubectl autocompletion.

To do so in all your shell sessions, add the following to your `~/.zshrc` file:

```zsh
source <(kubectl completion zsh)
```

If you have an alias for kubectl, kubectl autocompletion will automatically work with it.

After reloading your shell, kubectl autocompletion should be working.

If you get an error like `2: command not found: compdef`, then add the following to the beginning of your `~/.zshrc` file:

```zsh
autoload -Uz compinit
compinit
```
