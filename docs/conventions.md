# Conventions

This document describes the software engineering conventions we follow in
developing the HCI. Lint rules enforce most of our conventions automatically, but
there are still some conventions to be aware of.

## Python Comments

- Prefer the [imperative mood](https://en.wikipedia.org/wiki/Imperative_mood) for
  comments.

### Docstring Comments

The "top-level" docstring for a module, class, or function should almost always
be in the [imperative mood](https://en.wikipedia.org/wiki/Imperative_mood).

### TODO Comments

- Try to avoid writing these "I'll do it later" comments.
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