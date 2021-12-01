#!/usr/bin/env python3
from gendiff.engine.engine import get_diff
from gendiff.conversion_to_string import get_string
from gendiff.engine.parser import parses


YAML_RESULT = 'tests/result/yalm'
YAML_FILE1 = 'tests/fixtures/file1.yml'
YAML_FILE2 = 'tests/fixtures/file2.yml'
JSON_RESULT = 'tests/result/json'
JSON_FILE1 = 'tests/fixtures/file_test1.json'
JSON_FILE2 = 'tests/fixtures/file_test2.json'


def get_expected_result(path_to_file):
    with open(path_to_file) as file:
        expected_result = file.read()
    return expected_result


def test_gendiff_json():
    file1 = parses(JSON_FILE1)
    file2 = parses(JSON_FILE2)
    result = get_diff(file1, file2)
    assert get_string(result) == get_expected_result(JSON_RESULT)


def test_gendiff_yaml():
    file1 = parses(YAML_FILE1)
    file2 = parses(YAML_FILE2)
    result = get_diff(file1, file2)
    assert get_string(result) == get_expected_result(YAML_RESULT)
