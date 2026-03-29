"""Multi-device inventory example for RESTCONF + YANG."""

from __future__ import annotations

from restconf_yang_automation.models import Device
from restconf_yang_automation.workflows.inventory import collect_interfaces


def main() -> None:
    devices = [
        Device(
            name="r1",
            base_url="https://router-1.lab.local",
            username="admin",
            password="admin",
            verify_tls=False,
        ),
        Device(
            name="r2",
            base_url="https://router-2.lab.local",
            username="admin",
            password="admin",
            verify_tls=False,
        ),
    ]

    for device in devices:
        interfaces = collect_interfaces(device)
        print(f"\n[{device.name}] interfaces={len(interfaces)}")
        for item in interfaces:
            print(f"- {item['name']} enabled={item['enabled']} desc={item['description']}")


if __name__ == "__main__":
    main()
