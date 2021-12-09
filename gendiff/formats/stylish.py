#!/usr/bin/env python3


SPACE = '  '
ADDED = '+ '
REMOVED = '- '


def edit_diff(diff):
    result = {}
    keys = diff.keys()
    for key in keys:
        value = diff.get(key)
        if key[0] == 'removed':
            result[REMOVED+key[1]] = convert_value(value)
        elif key[0] == 'added':
            result[ADDED+key[1]] = convert_value(value)
        elif key[0] == 'no change':
            result[SPACE+key[1]] = convert_value(value)
        elif key[0] == 'changed':
            result[REMOVED+key[1]] = convert_value(value[0])
            result[ADDED+key[1]] = convert_value(value[1])
        elif key[0] == 'children':
            result[SPACE+key[1]] = edit_diff(value)
    return result


def convert_value(value):
    if type(value) != dict:
        return value
    result = {}
    keys = value.keys()
    for key in keys:
        v1 = value.get(key)
        result[SPACE+key] = convert_value(v1)
    return result


def string_formation(data, indent=1):
    result = ''
    keys = data.keys()
    for key in keys:
        value = data[key]
        if type(value) == dict:
            result += f'{SPACE*indent}{key}: ' + '{\n'
            result += string_formation(value, indent+2)
            result += f'{SPACE*(indent+1)}' + '}\n'
        else:
            result += f'{SPACE*indent}{key}: {value}\n'
    return result


def stylish_format(diff):
    result = '{\n'
    edit_difference = edit_diff(diff)
    result += string_formation(edit_difference)
    result += '}'
    return result
