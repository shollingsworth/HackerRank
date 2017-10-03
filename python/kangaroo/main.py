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
def kangaroo(x1, v1, x2, v2):
    for i in xrange(1,10000):
        if (x1 + (v1 * i)) == (x2 + (v2 * i)): return 'YES'
    return 'NO'
x1, v1, x2, v2 = map(int,raw_input().strip().split(' '))
result = kangaroo(x1, v1, x2, v2)
print(result)
