from restconf_yang_automation.client import RestconfClient


def test_build_url_accepts_data_path() -> None:
    client = RestconfClient("https://router", "u", "p")
    assert client._build_url("openconfig-interfaces:interfaces") == (
        "https://router/restconf/data/openconfig-interfaces:interfaces"
    )


def test_build_url_accepts_full_restconf_path() -> None:
    client = RestconfClient("https://router", "u", "p")
    assert client._build_url("restconf/data/ietf-interfaces:interfaces") == (
        "https://router/restconf/data/ietf-interfaces:interfaces"
    )
