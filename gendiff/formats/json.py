#!/usr/bin/env python3
import json


def edit_diff(diff):
    result = {}
    keys = diff.keys()
    for key in keys:
        value = diff.get(key)
        if key[0] == 'nested':
            result[key[1]] = [key[0], edit_diff(value)]
        else:
            result[key[1]] = [key[0], value]
    return result


def json_format(diff):
    result = edit_diff(diff)
    return json.dumps(result, indent=2)
