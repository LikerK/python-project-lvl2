#!/usr/bin/env python3
from gendiff.engine.data_extractor import get_data
from gendiff.formats.styles import FORMATS


def generate_diff(file1, file2, format_name='stylish'):
    file1 = get_data(file1)
    file2 = get_data(file2)
    return FORMATS[format_name](get_diff(file1, file2))


def get_diff(data1, data2):
    result = {}
    keys = sorted(data1.keys() | data2.keys())
    for key in keys:
        v1, v2 = data1.get(key), data2.get(key)
        if key in data1 and key not in data2:
            status = "removed"
            value = v1
        elif key in data2 and key not in data1:
            status = "added"
            value = v2
        elif v1 == v2:
            status = "no change"
            value = v1
        elif type(v1) == dict and type(v2) == dict:
            status = 'nested'
            value = get_diff(v1, v2)
        else:
            status = "changed"
            value = v1, v2
        result[(status, key)] = value
    return result
