"""Core package for RESTCONF + YANG network automation."""

from .client import RestconfClient, RestconfError
from .models import Device
from .yang_mapper import extract_openconfig_interfaces

__all__ = [
    "Device",
    "RestconfClient",
    "RestconfError",
    "extract_openconfig_interfaces",
]
