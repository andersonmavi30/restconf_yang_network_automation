"""Interface inventory workflow for multiple devices."""

from __future__ import annotations

from restconf_yang_automation.client import RestconfClient
from restconf_yang_automation.models import Device
from restconf_yang_automation.yang_mapper import extract_openconfig_interfaces


def collect_interfaces(device: Device) -> list[dict[str, object]]:
    """Collect and normalize interface data for one device."""
    client = RestconfClient(
        base_url=device.base_url,
        username=device.username,
        password=device.password,
        verify_tls=device.verify_tls,
        timeout=device.timeout,
    )
    payload = client.get_data("openconfig-interfaces:interfaces")
    return extract_openconfig_interfaces(payload)
