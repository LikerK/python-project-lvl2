#!/usr/bin/env python3
import json
import argparse


def parse():
    parser = argparse.ArgumentParser(description='Generate diff')

    # position arguments
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    # options argument
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    return args


def parses(file):
    return json.load(open(file))
