#!/usr/bin/env python3


def conversion_to_string(dictonary):
    keys = dictonary.keys()
    result = '{\n'
    for key in keys:
        if key[0] == 'removed':
            result += '   - {}: {}\n'.format(key[1], dictonary[key])
        elif key[0] == 'added':
            result += '   + {}: {}\n'.format(key[1], dictonary[key])
        elif key[0] == 'no change':
            result += '     {}: {}\n'.format(key[1], dictonary[key])
        elif key[0] == 'changed':
            value = dictonary.get(key)
            result += '   - {}: {}\n'.format(key[1], value[0])
            result += '   + {}: {}\n'.format(key[1], value[1])
    result += '}'
    return change_under_json(result)


def change_under_json(string):
    if 'False' in string:
        string = string.replace('False', 'false')
    if 'True' in string:
        string = string.replace('True', 'true')
    return string
