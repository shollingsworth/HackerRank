#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __future__
import sys
sys.stdin = open("./stdin.txt", 'r')

def swap_case(s):
    retval = []
    upper = range(65,91)
    lower = range(97,123)
    arr = map(ord, list(s))
    for i in arr:
        if i in upper:
            idx = upper.index(i)
            nv = lower[idx]
        elif i in lower:
            idx = lower.index(i)
            nv = upper[idx]
        else:
            nv = i
        retval.append(chr(nv))
    return "".join(retval)

swap_case(raw_input())
