from pathlib import Path
from gendiff.engine.data_extractor import get_data
from gendiff.engine.file_parser import get_content
from gendiff.formats.styles import FORMATS


def generate_diff(file_path1, file_path2, format_name='stylish'):
    file_extension1 = Path(file_path1).suffix
    file_extension2 = Path(file_path2).suffix
    file1 = get_data(get_content(file_path1), file_extension1)
    file2 = get_data(get_content(file_path2), file_extension2)
    return FORMATS[format_name](get_diff(file1, file2))


def get_diff(data1, data2):
    result = {}
    keys = sorted(data1.keys() | data2.keys())
    for key in keys:
        v1, v2 = data1.get(key), data2.get(key)
        if key in data1 and key not in data2:
            _type = "removed"
            value = v1
        elif key in data2 and key not in data1:
            _type = "added"
            value = v2
        elif v1 == v2:
            _type = "unchanged"
            value = v1
        elif type(v1) is dict and type(v2) is dict:
            _type = 'nested'
            value = get_diff(v1, v2)
        else:
            _type = "changed"
            value = v1, v2
        result[key] = {
            'type': _type,
            'value': value}
    return result
