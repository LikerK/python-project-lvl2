#!/usr/bin/env python3
from gendiff.engine.parser import parses


def generate_diff(file1, file2):
    file1 = parses(file1)
    file2 = parses(file2)
    return get_diff(file1, file2)


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
        else:
            status = "changed"
            value = v1, v2
        result[(status, key)] = value
    return result
