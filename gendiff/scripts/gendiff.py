#!/usr/bin/env python3
from gendiff.scripts.parser import parse
from gendiff.engine.engine import generate_diff


def main():
    result = parse()
    diff = generate_diff(result.first_file, result.second_file, result.format)
    print(diff)


if __name__ == '__main__':
    main()
