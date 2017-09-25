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
import collections
def birthdayCakeCandles(n, arr):
    c = collections.Counter(arr)
    return c[max(arr)]

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, arr)
print(result)
