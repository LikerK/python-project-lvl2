#!/usr/bin/env python3
from gendiff.formats.change_under_format import change_under_format


SPACE = '  '
ADDED = '+ '
REMOVED = '- '


def stylish_format(diff):
    result = '{\n' + get_string_diff(diff) + '}'
    return result


def get_string_diff(diff, indent=0):
    result = ''
    keys = diff.keys()
    for key in keys:
        data = diff.get(key)
        status, value = data[0], data[1]
        if status == 'removed':
            result += get_top(REMOVED + key, value, indent + 1)
        elif status == 'added':
            result += get_top(ADDED + key, value, indent + 1)
        elif status == 'no change':
            result += get_top(SPACE + key, value, indent + 1)
        elif status == 'changed':
            result += get_top(REMOVED + key, value[0], indent + 1)
            result += get_top(ADDED + key, value[1], indent + 1)
        elif status == 'nested':
            result += get_top(SPACE + key, data, indent + 1)
            result += get_string_diff(value, indent + 2)
            result += f'{SPACE * (indent + 2)}' + '}\n'
    return result


def get_top(key, value, indent):
    if type(value) == dict:
        return (
            f'{SPACE * indent}{key}:' + ' {\n' + get_value(value, indent + 3) 
            + f'{SPACE * (indent+1)}' + '}\n')
    elif type(value) == list:
        return f'{SPACE * indent}{key}: ' + '{\n'
    return change_under_format(f'{SPACE * indent}{key}: {value}\n')


def get_value(value, indent):
    result = ''
    keys = value.keys()
    for key in keys:
        v = value.get(key)
        if type(v) == dict:
            result += f'{SPACE * indent}{key}:' + ' {\n'
            result += get_value(v, indent + 2)
            result += f'{SPACE * indent}' + '}\n'
        else:
            result += f'{SPACE * indent}{key}: {v}\n'
    return change_under_format(result)
