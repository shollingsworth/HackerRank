#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
import sys
print("===" * 30)
print("SAMPLE INPUT:")
print("===" * 30)
print(open("./challenge_sample_input", 'r').read())
sys.stdin = open("./challenge_sample_input", 'r')
print("===" * 30)
print("SAMPLE OUTPUT:")
print("===" * 30)
print(open("./challenge_sample_output", 'r').read())
print("===" * 30)
print("START")
print("===" * 30)

#!/bin/python
import sys
def solve(grades):
    retval = []
    for i in grades:
        lo = 5 - (i % 5)
        if lo < 3 and i > 37: g = i + lo
        else: g = i
        retval.append(g)
    return retval
grades = [int(raw_input().strip()) for _ in xrange(int(raw_input().strip()))]
print "\n".join(map(str, solve(grades)))
