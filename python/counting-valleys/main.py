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

smap = {
    'U' : 1,
    'D' : -1,
}
num_steps = int(raw_input())
steps = list(raw_input())
assert len(steps) == num_steps
valleys = 0
level = 0
for i in steps:
    prev = level
    level += smap[i]
    if prev < 0 and level == 0: valleys += 1
print(valleys)
