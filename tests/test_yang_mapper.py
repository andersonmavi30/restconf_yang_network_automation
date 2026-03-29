from restconf_yang_automation.yang_mapper import extract_openconfig_interfaces


def test_extract_openconfig_interfaces_returns_normalized_items() -> None:
    payload = {
        "openconfig-interfaces:interfaces": {
            "interface": [
                {
                    "name": "Gig1",
                    "config": {
                        "description": "uplink",
                        "enabled": True,
                        "type": "ethernetCsmacd",
                    },
                }
            ]
        }
    }

    result = extract_openconfig_interfaces(payload)

    assert result == [
        {
            "name": "Gig1",
            "description": "uplink",
            "enabled": True,
            "type": "ethernetCsmacd",
        }
    ]
