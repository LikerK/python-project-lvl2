#!/usr/bin/env python3
import json


def stylish_format(diff):
    result = '{\n' + get_string_diff(diff) + '}'
    return result


LVL = '    '

STATUSES = {
    'no change': '    ',
    'added': '  + ',
    'removed': '  - ',
    'changed': '    ',
    'indent': '    ',
    'nested': '    '
    }


def get_string_diff(diff, depth=0):
    result = ''
    keys = diff.keys()
    for key in keys:
        data = diff.get(key)
        status, value = data[0], data[1]
        if status == 'changed':
            result += get_top('removed', key, value[0], depth)
            result += get_top('added', key, value[1], depth)
        else:
            result += get_top(status, key, value, depth)
    return result


def get_top(status, key, value, depth):
    indent = get_indent(depth)
    result = f'{indent}{STATUSES[status]}{key}: '
    if type(value) == dict:
        result += '{\n'
    return result + get_value(value, depth + 1, status)


def get_value(value, depth, status):
    indent = get_indent(depth)
    if status == 'nested':
        return get_string_diff(value, depth) + indent + '}\n'
    if type(value) == dict:
        result = ''
        keys = value.keys()
        for key in keys:
            v = value.get(key)
            result += get_top('indent', key, v, depth)
        result += indent + '}\n'
        return result
    return f'{json.dumps(value) if type(value) != str else value}\n'


def get_indent(depth):
    return LVL * depth
