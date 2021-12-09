#!/usr/bin/env python3
from gendiff.engine.engine import generate_diff
from gendiff.formats.change_under_format import change_under_format


YAML_RESULT = 'tests/result/yalm'
YAML_FILE1 = 'tests/fixtures/filepath1.yml'
YAML_FILE2 = 'tests/fixtures/filepath2.yml'
STYLISH_RESULT = 'tests/result/stylish'
JSON_FILE1 = 'tests/fixtures/filepath1.json'
JSON_FILE2 = 'tests/fixtures/filepath2.json'
PLAIN_RESULT = 'tests/result/plain'
JSON_RESULT = 'tests/result/json'


def get_expected_result(path_to_file):
    with open(path_to_file) as file:
        expected_result = file.read()
    return expected_result


def test_stylish():
    diff = generate_diff(JSON_FILE1, JSON_FILE2)
    result = change_under_format(diff)
    assert result == get_expected_result(STYLISH_RESULT)


def test_yaml():
    diff = generate_diff(YAML_FILE1, YAML_FILE2)
    result = change_under_format(diff)
    assert result == get_expected_result(YAML_RESULT)


def test_palm():
    diff = generate_diff(JSON_FILE1, JSON_FILE2, format_name='plain')
    result = change_under_format(diff)
    assert result == get_expected_result(PLAIN_RESULT)


def test_json():
    diff = generate_diff(JSON_FILE1, JSON_FILE2, format_name='json')
    result = change_under_format(diff)
    assert result == get_expected_result(JSON_RESULT)
