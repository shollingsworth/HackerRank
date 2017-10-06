#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
import sys

ip = "./challenge_sample_input"
op = "./challenge_sample_output"

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
def sockMerchant(n, ar):
    sock_cnt = 0
    assert len(ar) == n
    for i in set(ar):
        cnt = ar.count(i)
        evens = cnt - (cnt % 2)
        if not evens: continue
        sock_cnt += evens / 2
    return sock_cnt
n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = sockMerchant(n, ar)
print(result)
