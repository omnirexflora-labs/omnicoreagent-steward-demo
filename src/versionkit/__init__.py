"""Parse and compare release versions such as "1.10.0"."""

from __future__ import annotations

from dataclasses import dataclass

__all__ = ["Version", "parse", "latest"]


@dataclass(frozen=True, order=True)
class Version:
    """A release version: major.minor.patch."""

    major: str
    minor: str
    patch: str

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"


def parse(text: str) -> Version:
    """Parse "1.10.0", "v1.10.0" or "1.10" into a Version."""
    text = text.strip().removeprefix("v")
    parts = text.split(".")
    if not 2 <= len(parts) <= 3 or not all(part.isdigit() for part in parts):
        raise ValueError(f"not a version: {text!r}")
    if len(parts) == 2:
        parts.append("0")
    return Version(*(int(part) for part in parts))


def latest(versions: list[str]) -> str:
    """The newest of the given versions, as written."""
    if not versions:
        raise ValueError("no versions given")
    return max(versions, key=parse)
