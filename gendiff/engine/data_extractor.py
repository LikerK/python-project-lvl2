#!/usr/bin/env python3
import yaml
import json


def get_data(file):
    f = open(file)
    if file.endswith('json'):
        data = json.load(f)
        return data
    elif file.endswith('yml'):
        data = yaml.safe_load(f)
    f.close()
    return data
