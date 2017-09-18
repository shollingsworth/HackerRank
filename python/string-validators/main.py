#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __future__
import sys
sys.stdin = open("./stdin.txt", 'r')

if __name__ == '__main__':
    funcs = [
        str.isalnum,
        str.isalpha,
        str.isdigit,
        str.islower,
        str.isupper,
    ]
    s = raw_input().strip()
    for f in funcs:
        res = False
        for c in list(s):
            if f(c):
                res = True
        print(res)
