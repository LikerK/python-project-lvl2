import yaml
import json


def parse_json_file(file_content):
    return json.loads(file_content)


def parse_yaml_file(file_content):
    return yaml.safe_load(file_content)


def get_data(file_content, file_extension):
    if file_extension == '.json':
        return parse_json_file(file_content)
    elif file_extension == '.yml' or file_extension == '.yaml':
        return parse_yaml_file(file_content)
