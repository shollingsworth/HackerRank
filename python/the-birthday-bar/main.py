#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
import sys
print("===" * 30)
print("SAMPLE INPUT:")
print("===" * 30)
print(open("./input07.txt", 'r').read())
sys.stdin = open("./input07.txt", 'r')
print("===" * 30)
print("SAMPLE OUTPUT:")
print("===" * 30)
print(open("./output07.txt", 'r').read())
print("===" * 30)
print("START")
print("===" * 30)

#!/bin/python
import sys
import itertools
def solve(n, s, d, m):
    sum_cnt = 0
    for x in range(0,len(s)):
        start = x
        end = x + m
        arr = s[start:end]
        if len(arr) < m: break
        if d == sum(arr): sum_cnt += 1
    return sum_cnt

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
d, m = map(int,raw_input().strip().split(' '))
result = solve(n, s, d, m)
print(result)
