#!/usr/bin/env python3
from gendiff.formats import json, plain, stylish


FORMATS = {
    "stylish": stylish.stylish_format,
    'plain': plain.plain_format,
    'json': json.json_format
}
