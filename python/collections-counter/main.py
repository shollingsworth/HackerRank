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

from collections import Counter
int(raw_input())
S = Counter(map(int,raw_input().split()))
C = [map(int,raw_input().split()) for _ in range(int(raw_input()))]
sale = 0
for i in C:
    size, amt = i
    if S[size]:
        sale += amt
        S[size] += -1
print(sale)
