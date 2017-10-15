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
def getMoneySpent(keyboards, drives, s):
    final_sum = -1
    arr = [sum([i,n]) for i in keyboards for n in drives if sum([i,n]) <= s]
    if not arr:
        return -1
    else:
        return max(arr)
s,n,m = map(int,raw_input().strip().split(' '))
keyboards = map(int, raw_input().strip().split(' '))
assert len(keyboards) == n
drives = map(int, raw_input().strip().split(' '))
assert len(drives) == m
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
