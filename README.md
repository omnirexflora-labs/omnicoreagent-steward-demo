# versionkit

Parse and compare release versions.

```python
from versionkit import latest, parse

parse("v1.10")                      # Version 1.10.0
latest(["1.9.0", "1.10.0"])         # "1.10.0"
```

## Develop

```bash
uv sync
uv run pytest -q
```

This repository is maintained with the help of the
[OmniCoreAgent steward](https://github.com/omnirexflora-labs/omnicoreagent/tree/main/apps/steward):
an agent that reproduces failures in a sandbox, opens pull requests behind a
person's approval, and cannot merge.
