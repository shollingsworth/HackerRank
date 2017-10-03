#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
import sys

ip = "./challenge_sample_input"
op = "./challenge_sample_output"

ip = "./input99.txt"
op = "./output99.txt"

ip = "./input59.txt"
op = "./output59.txt"


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
def solve(year):
    cnt = 0
    cal_map = [
        31, #jan
        28, #feb
        31, #mar
        30, #apr
        31, #may
        30, #jun
        31, #jul
        31, #aug
        30, #sep
    ]
    is_julian = year < 1918
    if year == 1918:
        cal_map[1] += -13
    if is_julian and year % 4 == 0:
        cal_map[1] += 1
    elif year % 400 == 0:
        cal_map[1] += 1
    elif year % 4 == 0 and not year % 100 == 0:
        cal_map[1] += 1
    for m,val in enumerate(cal_map):
        cnt += val
        if cnt > 256: break
    left = val - (cnt - 256)
    mon = m + 1
    return "{:02d}.{:02d}.{:04d}".format(left,mon,year)

year = int(raw_input().strip())
result = solve(year)
print(result)
