# Conventions

This document describes the software engineering conventions we follow in
developing the HCI.

## Python Comments

- Don't write obvious comments.
- Prefer the imperative mood for comments.

### Docstring Comments

The "top-level" docstring for a module, class, or function should almost always
be in the imperative mood.

### TODO Comments

- TODO comments *must* have an author.
- TODO comments *must* be accompanied by a link to a GitHub issue.

Here's an example:

```
# TODO(Liam): Fix the foo feature. Tracked in https://github.com/org/repo/issue/123.
```

### Lint Comments

If you ignore a lint rule, you *must* provide a justification for doing so.

Here's an example:

```
from .base import (  # noqa: F401 (We don't care about unused imports in this context.)
```