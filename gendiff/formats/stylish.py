import json


LVL = '    '
EMPTY_INDENT = '    '
MAPPING_VERTEX_TYPES_TO_INDENTS = {
    'no change': '    ',
    'added': '  + ',
    'removed': '  - ',
    'unchanged': '    ',
    'nested': '    '}


def stylish_format(diff):
    depth = 0
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
            f'{indent}{MAPPING_VERTEX_TYPES_TO_INDENTS["removed"]}{key}: '
            + get_value(first_value, depth))
        result += (
            f'{indent}{MAPPING_VERTEX_TYPES_TO_INDENTS["added"]}{key}: '
            + get_value(second_value, depth))
    elif type == 'nested':
        result += (
            f'{indent}{MAPPING_VERTEX_TYPES_TO_INDENTS[type]}{key}: ' + '{\n')
        for key, node in value.items():
            result += stringify_node(key, node, depth + 1)
        result += indent + EMPTY_INDENT + '}\n'
    else:
        result = (
            f'{indent}{MAPPING_VERTEX_TYPES_TO_INDENTS[type]}{key}: '
            + get_value(value, depth))
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
            f'{indent}{EMPTY_INDENT}{key}: '
            + get_value(value, depth))
    result += indent + '}\n'
    return result


def get_indent(depth):
    return LVL * depth
