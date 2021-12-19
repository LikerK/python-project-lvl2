#!/usr/bin/env python3
import pytest
from gendiff.engine.engine import generate_diff


YAML_RESULT = 'tests/fixtures/result/yalm'
YAML_FILE1 = 'tests/fixtures/filepath1.yml'
YAML_FILE2 = 'tests/fixtures/filepath2.yml'
STYLISH_RESULT = 'tests/fixtures/result/stylish'
JSON_FILE1 = 'tests/fixtures/filepath1.json'
JSON_FILE2 = 'tests/fixtures/filepath2.json'
PLAIN_RESULT = 'tests/fixtures/result/plain'
JSON_RESULT = 'tests/fixtures/result/json'
YAML_FILE_PATH1 = 'tests/fixtures/filepath1.yml'
YAML_FILE_PATH2 = 'tests/fixtures/filepath2.yml'
YAML_FILE_PATH_RESULT = 'tests/fixtures/result/yaml2'


def get_expected_result(path_to_file):
    with open(path_to_file) as file:
        expected_result = file.read()
    return expected_result


@pytest.mark.parametrize('path1, path2, format, result', [
    (JSON_FILE1, JSON_FILE2, 'stylish', STYLISH_RESULT),
    (YAML_FILE1, YAML_FILE2, 'stylish', YAML_RESULT),
    (JSON_FILE1, JSON_FILE2, 'plain', PLAIN_RESULT),
    (JSON_FILE1, JSON_FILE2, 'json', JSON_RESULT),
    (YAML_FILE_PATH1, YAML_FILE_PATH2, 'stylish', YAML_FILE_PATH_RESULT)
])
def test_gendiff(path1, path2, format, result):
    assert generate_diff(
        path1, path2, format) == get_expected_result(result)
