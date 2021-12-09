#!/usr/bin/env python3


def change_under_format(string):
    if 'False' in string:
        string = string.replace('False', 'false')
    if 'True' in string:
        string = string.replace('True', 'true')
    if 'None' in string:
        string = string.replace('None', 'null')
    return string
