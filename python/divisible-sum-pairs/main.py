#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
import sys
import json
ip = "./input07.txt"
op = "./output07.txt"

ip = "./challenge_sample_input"
op = "./challenge_sample_output"

ip = "./input14.txt"
op = "./output14.txt"
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
def divisibleSumPairs(n, k, ar):
    cnt = 0
    for idx1,v in enumerate(ar):
        for idx2 in range(0,len(ar)):
            if idx1 == idx2 or not idx1 > idx2: continue
            a,b = ar[idx1],ar[idx2]
            if (a + b) % k == 0: cnt += 1
    return cnt

n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
ar = map(int, raw_input().strip().split(' '))
result = divisibleSumPairs(n, k, ar)
print(result)
