### Hexlet tests and linter status:
[![Actions Status](https://github.com/LikerK/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/LikerK/python-project-lvl2/actions)
[![example workflow](https://github.com/LikerK/python-project-lvl2/workflows/my_linter/badge.svg)](https://github.com/LikerK/python-project-lvl2/actions/workflows/my_linter.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/c4dbc593129a63a866a6/maintainability)](https://codeclimate.com/github/LikerK/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/c4dbc593129a63a866a6/test_coverage)](https://codeclimate.com/github/LikerK/python-project-lvl2/test_coverage)

---
### Description

This program finds differences between files (formats: JSON, YAML)

---
### Program installation

<code>pip install git+https://github.com/LikerK/python-project-lvl2.git</code>

---
### How to use

<code>gendiff --format path/to/file1 path/to/file2</code>

If you need help

<code>gendiff -h</code>

The program can produce output in three formats.

---
#### STYLISH (default format) 
Minus ("-") - the key is only in the first file. Plus ("+") - the key is only in the second file The absence of a plus or minus signifies that the key is present in both files, and its values are the same.

<code>gendiff path/to/file1 path/to/file2</code>

Examples:

[![asciicast](https://asciinema.org/a/hmGSipGs9tviRXqFFbHbJRlSY.svg)](https://asciinema.org/a/hmGSipGs9tviRXqFFbHbJRlSY)
[![asciicast](https://asciinema.org/a/XyvFXV5t4e7FQXU8HOrNtuLhN.svg)](https://asciinema.org/a/XyvFXV5t4e7FQXU8HOrNtuLhN)
[![asciicast](https://asciinema.org/a/SweSq18hMAwzWDAfeQeZrho79.svg)](https://asciinema.org/a/SweSq18hMAwzWDAfeQeZrho79)

---
#### PLAIN
Describes what changes have occurred from the first file to the second file

<code>gendiff -f plain path/to/file1 path/to/file2</code>

Example:

[![asciicast](https://asciinema.org/a/PcgK9HWW2YT5NrIWLy20BqV4Y.svg)](https://asciinema.org/a/PcgK9HWW2YT5NrIWLy20BqV4Y)

---
#### JSON
Output in json format

<code>gendiff -f json path/to/file1 path/to/file2</code>

Example:

[![asciicast](https://asciinema.org/a/RlAgiBQpnjzVG0VaxO67km6AX.svg)](https://asciinema.org/a/RlAgiBQpnjzVG0VaxO67km6AX)
