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

from itertools import groupby
S = raw_input()
arr = []
for i in groupby(S):
    a,it = list(i)
    a,it = int(a), len(list(it))
    arr.append((it,a))
print(" ".join([str(i) for i in arr]))
