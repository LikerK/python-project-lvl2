#!/usr/bin/env python3


def plain_format(diff, path=[]):
    result = []
    keys = diff.keys()
    for key in keys:
        value = diff.get(key)
        path.append(key[1])
        if key[0] == 'removed':
            value = convert_value(value)
            result.append(f"Property '{'.'.join(path)}' was removed")
        elif key[0] == 'added':
            value = convert_value(value)
            result.append(
                f"Property '{'.'.join(path)}' was added with value: {value}")
        elif key[0] == 'changed':
            value = [convert_value(i) for i in value]
            result.append(
                f"Property '{'.'.join(path)}' was updated. "
                + f"From {value[0]} to {value[1]}")
        elif key[0] == 'children':
            result.append(plain_format(value))
        path.pop()
    return '\n'.join(result)


def convert_value(value):
    if type(value) == dict:
        return '[complex value]'
    elif type(value) == str:
        return f"'{value}'"
    return value
