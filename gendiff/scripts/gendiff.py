#!/usr/bin/env python3
from gendiff.engine.parser import parse
from gendiff.engine.engine import generate_diff
from gendiff.formats.change_under_format import change_under_format


def main():
    result = parse()
    diff = generate_diff(result.first_file, result.second_file, result.format)
    result = change_under_format(diff)
    print(result)


if __name__ == '__main__':
    main()
