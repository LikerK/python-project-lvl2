#!/usr/bin/env python3
import yaml
import json


def get_data(file):
    if file.endswith('json'):
        with open(file) as f:
            data = json.load(f)
    elif file.endswith('yml'):
        with open(file) as f:
            data = yaml.safe_load(f)
    return data
