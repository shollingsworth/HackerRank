#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
import sys

ip = "./challenge_sample_input"
op = "./challenge_sample_output"

ip = "./challenge_sample_input1"
op = "./challenge_sample_output1"

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
def solve(size,page):
    if size % 2 == 0 : size += 1
    return min([
        [page in [i,i -1] for i in xrange(size,0,-2)].index(True),
        [page in [i,i +1] for i in xrange(0,size,2)].index(True),
    ])
n,p = int(raw_input().strip()), int(raw_input().strip())
print(solve(n,p))
