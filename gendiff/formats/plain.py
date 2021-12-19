#!/usr/bin/env python3
from gendiff.formats.change_under_format import change_under_format


def plain_format(data):
    return get_string(data)


def get_string(diff, path=[]):
    result = []
    keys = diff.keys()
    for key in keys:
        value = diff.get(key)
        path.append(key)
        if value[0] == 'removed':
            value = convert_value(value[1])
            result.append(f"Property '{'.'.join(path)}' was removed")
        elif value[0] == 'added':
            value = convert_value(value[1])
            result.append(
                f"Property '{'.'.join(path)}' was added with value: {value}")
        elif value[0] == 'changed':
            value = [convert_value(i) for i in value[1]]
            result.append(
                f"Property '{'.'.join(path)}' was updated. "
                + f"From {value[0]} to {value[1]}")
        elif value[0] == 'nested':
            result.append(get_string(value[1]))
        path.pop()
    return '\n'.join(result)


def convert_value(value):
    if type(value) == dict:
        return '[complex value]'
    elif type(value) == str:
        return f"'{value}'"
    return change_under_format(str(value))
