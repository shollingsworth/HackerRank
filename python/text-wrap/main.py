#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __future__
import sys
sys.stdin = open("./stdin.txt", 'r')

def wrap(string, max_width):
    arr = list(string)
    retarr = []
    na = []
    while arr:
        na.append(arr.pop(0))
        if len(na) == max_width:
            retarr.append("".join(na))
            na = []
    if len(na) > 0:
        retarr.append("".join(na))
    return "\n".join(retarr)

print(wrap(raw_input(),int(raw_input())))
