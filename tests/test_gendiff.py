#!/usr/bin/env python3
import pytest
from gendiff.engine.engine import generate_diff


NOT_NESTED_RESULT = 'tests/fixtures/result/not_nested'
NESTED_RESULT = 'tests/fixtures/result/nested'
YAML_FILE1 = 'tests/fixtures/filepath1.yaml'
YAML_FILE2 = 'tests/fixtures/filepath2.yaml'
YAML_FILE_PATH1 = 'tests/fixtures/file1.yaml'
YAML_FILE_PATH2 = 'tests/fixtures/file2.yaml'
YML_FILE1 = 'tests/fixtures/filepath1.yml'
YML_FILE2 = 'tests/fixtures/filepath2.yml'
YML_FILE_PATH1 = 'tests/fixtures/file1.yml'
YML_FILE_PATH2 = 'tests/fixtures/file2.yml'
JSON_FILE1 = 'tests/fixtures/filepath1.json'
JSON_FILE2 = 'tests/fixtures/filepath2.json'
JSON_FILE_PATH1 = 'tests/fixtures/file1.json'
JSON_FILE_PATH2 = 'tests/fixtures/file2.json'
JSON_RESULT = 'tests/fixtures/result/json'
PLAIN_RESULT = 'tests/fixtures/result/plain'
PLAIN_NESTED_RESULT = 'tests/fixtures/result/plain_nested'


def get_expected_result(path_to_file):
    with open(path_to_file) as file:
        expected_result = file.read()
    return expected_result


@pytest.mark.parametrize('path1, path2, format, result', [
    (YAML_FILE1, YAML_FILE2, 'stylish', NOT_NESTED_RESULT),
    (YAML_FILE_PATH1, YAML_FILE_PATH2, 'stylish', NESTED_RESULT),
    (YML_FILE1, YML_FILE2, 'stylish', NOT_NESTED_RESULT),
    (YML_FILE_PATH1, YML_FILE_PATH2, 'stylish', NESTED_RESULT),
    (JSON_FILE1, JSON_FILE2, 'stylish', NESTED_RESULT),
    (JSON_FILE_PATH1, JSON_FILE_PATH2, 'stylish', NOT_NESTED_RESULT),
    (JSON_FILE1, JSON_FILE2, 'plain', PLAIN_NESTED_RESULT),
    (JSON_FILE_PATH1, JSON_FILE_PATH2, 'plain', PLAIN_RESULT),
    (JSON_FILE1, JSON_FILE2, 'json', JSON_RESULT),
])
def test_gendiff(path1, path2, format, result):
    assert generate_diff(
        path1, path2, format) == get_expected_result(result)
