#!/bin/bash
python3 -m coverage run --source=python_crc16 -m pytest test_pytest.py
python3 -m coverage report -m 