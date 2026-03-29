# RESTCONF + YANG Network Automation

A starter codebase for network automation using **RESTCONF + YANG**.

## What this version includes

- RESTCONF client with `GET` and `PATCH` operations.
- Inventory model (`Device`) for multi-device workflows.
- YANG mapper (OpenConfig interfaces) for data normalization.
- Reusable inventory workflow (`collect_interfaces`).
- Example execution against multiple devices.
- Basic unit tests for client and mapper.

## Repository structure

```text
restconf_yang_network_automation/
├── examples/
│   └── run_inventory.py
├── src/restconf_yang_automation/
│   ├── __init__.py
│   ├── client.py
│   ├── models.py
│   ├── yang_mapper.py
│   └── workflows/
│       ├── __init__.py
│       └── inventory.py
├── tests/
│   ├── test_client.py
│   └── test_yang_mapper.py
└── pyproject.toml
```

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

## Run the example

```bash
python examples/run_inventory.py
```

## Run tests

```bash
pytest -q
```

## Suggested next iterations

- Add vendor-specific drivers (IOS-XE, NX-OS, JunOS).
- Add stronger authentication options (token/OAuth/Vault).
- Validate payloads against specific YANG model versions.
- Add CI pipelines (lint + unit tests + smoke tests).
