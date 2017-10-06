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
def bonAppetit(n, no_eat, charged, items):
    assert len(ar) == n
    no_eat = items.pop(no_eat)
    tot = sum(items)
    diff = charged - tot/2
    if diff:
        return diff
    else:
        return "Bon Appetit"
n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
ar = map(int, raw_input().strip().split(' '))
b = int(raw_input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
