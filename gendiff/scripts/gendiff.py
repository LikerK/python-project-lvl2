#!/usr/bin/env python3
from gendiff.engine.parser import parse
from gendiff.engine.engine import generate_diff
from gendiff.conversion_to_string import conversion_to_string


def main():
    result = parse()
    diff = generate_diff(result.first_file, result.second_file)
    string = conversion_to_string(diff)
    print(string)


if __name__ == '__main__':
    main()
