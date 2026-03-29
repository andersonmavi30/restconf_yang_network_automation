"""Domain models for RESTCONF + YANG automation."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Device:
    """Represents a network device in the automation inventory."""

    name: str
    base_url: str
    username: str
    password: str
    verify_tls: bool = False
    timeout: int = 20
