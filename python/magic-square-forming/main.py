#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
import sys


ip = "./challenge_sample_input"
op = "./challenge_sample_output"

ip = "./input1.txt"
op = "./output1.txt"

ip = "./input02.txt"
op = "./output02.txt"

ip = "./input09.txt"
op = "./output09.txt"


print("===" * 30)
print("SAMPLE INPUT:")
print("===" * 30)
print(open(ip, 'r').read())
sys.stdin = open(ip, 'r')
print("===" * 30)
print("SAMPLE OUTPUT:")
print("===" * 30)
print(open(op, 'r').read())
print("===" * 30)
print("START")
print("===" * 30)

#!/bin/python
import sys
magics = [
    [2, 7, 6, 9, 5, 1, 4, 3, 8],
    [2, 9, 4, 7, 5, 3, 6, 1, 8],
    [4, 3, 8, 9, 5, 1, 2, 7, 6],
    [4, 9, 2, 3, 5, 7, 8, 1, 6],
    [6, 1, 8, 7, 5, 3, 2, 9, 4],
    [6, 7, 2, 1, 5, 9, 8, 3, 4],
    [8, 1, 6, 3, 5, 7, 4, 9, 2],
    [8, 3, 4, 1, 5, 9, 6, 7, 2]
]
s = []
for s_i in xrange(3):
    s_temp = map(int,raw_input().strip().split(' '))
    for i in s_temp: s.append(i)

fscores = []
for m in magics:
    cost = 0
    for i,v in enumerate(m):
        s1 = s[i]
        c1 = m[i]
        if s1 == c1: continue
        cost += abs(c1 - s1)
    fscores.append(cost)
print(min(fscores))
