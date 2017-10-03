#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
import sys
ip = "./challenge_sample_input"
op = "./challenge_sample_output"

ip = "./input02.txt"
op = "./output02.txt"


print("===" * 30)
print("SAMPLE INPUT:")
print("===" * 30)
#print(open(ip, 'r').read())
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
def migratoryBirds(n, ar):
    check = [0,0]
    for i in range(1,6):
        num, mcnt = check
        cnt = ar.count(i)
        if cnt > mcnt: check = [i,cnt]
    num, mcnt = check
    return num

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = migratoryBirds(n, ar)
print(result)
