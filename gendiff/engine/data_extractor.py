#!/usr/bin/env python3
import yaml
import json


def get_content(file_path):
    with open(file_path) as file:
        return file.read()


def parse_json_file(file):
    return json.loads(file)


def parse_yaml_file(file):
    return yaml.safe_load(file)


def get_data(file, file_path):
    if file_path.endswith('json'):
        return parse_json_file(file)
    elif file_path.endswith(('yml', 'yaml')):
        return parse_yaml_file(file)
