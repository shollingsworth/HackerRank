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
n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
mlen = len(a[0])
d1 = []
d2 = []
for x in range(mlen):
    for y in range(mlen):
        if x != y: continue
        d1.append(a[x][y])
        d2.append(a[mlen-x-1][y])
print(abs(sum(d1) - sum(d2)))
