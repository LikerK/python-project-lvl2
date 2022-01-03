#!/usr/bin/env python3
import json


LVL = '    '
TYPES = {
    'no change': '    ',
    'added': '  + ',
    'removed': '  - ',
    'changed': '    ',
    'empty indent': '    ',
    'nested': '    '}


def stylish_format(diff, depth=0):
    result = '{\n'
    keys = diff.keys()
    for key in keys:
        node = diff[key]
        result += stringify_node(key, node, depth)
    result += '}'
    return result


def stringify_node(key, node, depth):
    indent = get_indent(depth)
    type, value = node['type'], node['value']
    result = ''
    if type == 'changed':
        first_value = value[0]
        second_value = value[1]
        result += (
            f'{indent}{TYPES["removed"]}{key}: '
            + get_value(first_value, depth))
        result += (
            f'{indent}{TYPES["added"]}{key}: '
            + get_value(second_value, depth))
    elif type == 'nested':
        result += f'{indent}{TYPES[type]}{key}: ' + '{\n'
        for key, node in value.items():
            result += stringify_node(key, node, depth + 1)
        result += indent + TYPES['empty indent'] + '}\n'
    else:
        result = f'{indent}{TYPES[type]}{key}: ' + get_value(value, depth)
    return result


def get_value(value, depth):
    if type(value) is dict:
        return convert_dict_to_str(value, depth + 1)
    return f'{json.dumps(value) if type(value) != str else value}\n'


def convert_dict_to_str(dict, depth):
    indent = get_indent(depth)
    result = '{\n'
    keys = dict.keys()
    for key in keys:
        value = dict.get(key)
        result += (
            f'{indent}{TYPES["empty indent"]}{key}: '
            + get_value(value, depth))
    result += indent + '}\n'
    return result


def get_indent(depth):
    return LVL * depth
