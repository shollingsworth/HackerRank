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

from itertools import combinations
S,k = raw_input().split()
S,k = list(S), int(k)
for _ in range(1,k + 1):
    print("\n".join(sorted(["".join(sorted(i)) for i in list(combinations(S,_))])))
