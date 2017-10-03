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
def getRecord(s):
    hi_s = lo_s = s.pop(0)
    hi_c = lo_c = 0
    for sc in s:
        if sc > hi_s:
            hi_s = sc
            hi_c += 1
        if sc < lo_s:
            lo_s = sc
            lo_c += 1
    return [hi_c,lo_c]

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
print " ".join(map(str, getRecord(s)))
