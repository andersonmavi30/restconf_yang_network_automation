"""RESTCONF client for network automation."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


class RestconfError(RuntimeError):
    """RESTCONF execution error."""


@dataclass(slots=True)
class RestconfClient:
    """Client for RESTCONF read/write operations."""

    base_url: str
    username: str
    password: str
    verify_tls: bool = False
    timeout: int = 20

    @property
    def _headers(self) -> dict[str, str]:
        return {
            "Accept": "application/yang-data+json",
            "Content-Type": "application/yang-data+json",
            "Authorization": f"Basic {self._basic_auth_token()}",
        }

    def _basic_auth_token(self) -> str:
        import base64

        raw = f"{self.username}:{self.password}".encode("utf-8")
        return base64.b64encode(raw).decode("utf-8")

    def _build_url(self, resource_path: str) -> str:
        clean_path = resource_path.strip().lstrip("/")
        if clean_path.startswith("restconf/"):
            return f"{self.base_url.rstrip('/')}/{clean_path}"
        return f"{self.base_url.rstrip('/')}/restconf/data/{clean_path}"

    def _request(self, method: str, resource_path: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
        url = self._build_url(resource_path)
        data = json.dumps(payload).encode("utf-8") if payload is not None else None
        req = Request(url=url, data=data, headers=self._headers, method=method)
        try:
            with urlopen(req, timeout=self.timeout) as response:
                body = response.read().decode("utf-8")
        except HTTPError as exc:
            raise RestconfError(f"RESTCONF {method} failed at {url}: {exc.read().decode('utf-8')}") from exc
        except URLError as exc:
            raise RestconfError(f"Unable to connect to {url}: {exc.reason}") from exc

        if not body:
            return {}
        return json.loads(body)

    def get_data(self, resource_path: str) -> dict[str, Any]:
        """Fetch a resource from /restconf/data and return parsed JSON."""
        return self._request("GET", resource_path)

    def patch_data(self, resource_path: str, payload: dict[str, Any]) -> None:
        """Apply PATCH to a YANG-modeled resource."""
        self._request("PATCH", resource_path, payload=payload)
