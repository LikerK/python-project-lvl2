#!/usr/bin/env python3
import json
import yaml
import argparse
from gendiff.formats.styles import FORMATS


def parse():
    parser = argparse.ArgumentParser(description='Generate diff')

    # position arguments
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    # options argument
    parser.add_argument('-f', '--format',
                        choices=FORMATS.keys(),
                        default="stylish",
                        help='output format (default: "stylish")')
    args = parser.parse_args()
    return args


def parses(file):
    if file.endswith('json'):
        return json.load(open(file))
    elif file.endswith('yml'):
        return yaml.safe_load(open(file))
