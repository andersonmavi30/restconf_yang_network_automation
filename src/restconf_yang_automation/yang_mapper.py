"""Transformation helpers for common YANG payloads."""

from __future__ import annotations

from typing import Any


def extract_openconfig_interfaces(payload: dict[str, Any]) -> list[dict[str, Any]]:
    """Extract a normalized interface list from OpenConfig payloads.

    Expected payload structure:
    {
      "openconfig-interfaces:interfaces": {
        "interface": [
          {"name": "GigabitEthernet1", "config": {"enabled": true}}
        ]
      }
    }
    """
    interfaces_root = payload.get("openconfig-interfaces:interfaces", {})
    interfaces = interfaces_root.get("interface", [])

    normalized: list[dict[str, Any]] = []
    for item in interfaces:
        config = item.get("config", {})
        normalized.append(
            {
                "name": item.get("name"),
                "description": config.get("description"),
                "enabled": config.get("enabled"),
                "type": config.get("type"),
            }
        )
    return normalized
