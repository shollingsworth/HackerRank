#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
import sys
sys.stdin = open("./stdin.txt", 'r')

def count_substring(string, sub_string):
    count = 0
    str_arr = list(string)
    while str_arr:
        if len(str_arr) < len(sub_string): break
        if "".join(str_arr[0:len(sub_string)]) == sub_string:
            count += 1
        str_arr.pop(0)
    return count

print(count_substring(raw_input(),raw_input()))
