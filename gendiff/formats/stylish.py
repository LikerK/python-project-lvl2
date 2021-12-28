#!/usr/bin/env python3
import json


LVL = '    '
SPACE = '  '
ADDED = '+ '
REMOVED = '- '


def stylish_format(diff):
    result = '{\n' + get_string_diff(diff) + '}'
    return result


def get_string_diff(diff, depth=0):
    indent = get_indent(depth)
    result = ''
    keys = diff.keys()
    for key in keys:
        data = diff.get(key)
        status, value = data[0], data[1]
        if status == 'removed':
            result += get_top(REMOVED + key, value, depth)
        elif status == 'added':
            result += get_top(ADDED + key, value, depth)
        elif status == 'no change':
            result += get_top(SPACE + key, value, depth)
        elif status == 'changed':
            result += get_top(REMOVED + key, value[0], depth)
            result += get_top(ADDED + key, value[1], depth)
        elif status == 'nested':
            result += f'{indent}{SPACE + key}: ' + '{\n'
            result += get_string_diff(value, depth + 1)
            result += f'{indent}' + '  }\n'
    return result


def get_top(key, value, depth, space=''):
    indent = get_indent(depth)
    result = f'{indent}{space}{key}: '
    if type(value) == dict:
        result += '{\n'
        keys = value.keys()
        for key1 in keys:
            v = value.get(key1)
            result += get_top(key1, v, depth + 1, SPACE)
        result += f'{indent}' + '  }\n'
    else:
        result += f'{json.dumps(value) if type(value) != str else value}\n'
    return result


def get_indent(depth):
    return LVL * depth + SPACE
