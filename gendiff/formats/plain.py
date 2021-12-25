#!/usr/bin/env python3
import json


def plain_format(data):
    return get_string(data)


def get_string(diff, path=[]):
    result = []
    keys = diff.keys()
    for key in keys:
        data = diff.get(key)
        status, value = data[0], data[1]
        path.append(key)
        if status == 'removed':
            value = convert_value(value)
            result.append(f"Property '{'.'.join(path)}' was removed")
        elif status == 'added':
            value = convert_value(value)
            result.append(
                f"Property '{'.'.join(path)}' was added with value: {value}")
        elif status == 'changed':
            value_in_changed = [convert_value(i) for i in value]
            result.append(
                f"Property '{'.'.join(path)}' was updated. "
                + f"From {value_in_changed[0]} to {value_in_changed[1]}")
        elif status == 'nested':
            result.append(get_string(value))
        path.pop()
    return '\n'.join(result)


def convert_value(value):
    if type(value) == dict:
        return '[complex value]'
    elif type(value) == str:
        return f"'{value}'"
    return json.dumps(value) if type(value) != str else value
