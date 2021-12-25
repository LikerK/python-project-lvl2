#!/usr/bin/env python3
import json


SPACE = '  '
ADDED = '+ '
REMOVED = '- '


def stylish_format(diff):
    result = '{\n' + get_string_diff(diff) + '}'
    return result


def get_string_diff(diff, depth=0):
    result = ''
    indent = SPACE * depth
    keys = diff.keys()
    for key in keys:
        data = diff.get(key)
        status, value = data[0], data[1]
        if status == 'removed':
            result += get_top(REMOVED + key, value, depth + 1)
        elif status == 'added':
            result += get_top(ADDED + key, value, depth + 1)
        elif status == 'no change':
            result += get_top(SPACE + key, value, depth + 1)
        elif status == 'changed':
            result += get_top(REMOVED + key, value[0], depth + 1)
            result += get_top(ADDED + key, value[1], depth + 1)
        elif status == 'nested':
            result += get_top(SPACE + key, data, depth + 1)
            result += get_string_diff(value, depth + 2)
            indent = SPACE * (depth + 2)
            result += f'{indent}' + '}\n'
    return result


def get_top(key, value, depth):
    indent = SPACE * depth
    if type(value) == dict:
        result = f'{indent}{key}:' + ' {\n' + get_value(value, depth + 3)
        indent = SPACE * (depth + 1)
        result += f'{indent}' + '}\n'
        return result
    elif type(value) == list:
        return f'{indent}{key}: ' + '{\n'
    return (
        f'{indent}{key}: '
        + f'{json.dumps(value) if type(value) != str else value}\n')


def get_value(value, depth):
    indent = SPACE * depth
    result = ''
    keys = value.keys()
    for key in keys:
        v = value.get(key)
        if type(v) == dict:
            result += f'{indent}{key}:' + ' {\n'
            result += get_value(v, depth + 2)
            result += f'{indent}' + '}\n'
        else:
            result += (
                f'{indent}{key}: {json.dumps(v) if type(v) != str else v}\n')
    return result
