#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
import sys
print(open("./challenge_sample_input", 'r').read())
sys.stdin = open("./challenge_sample_input", 'r')
print("===" * 30)
print("SAMPLE OUTPUT:")
print("===" * 30)
print(open("./challenge_sample_output", 'r').read())
print("===" * 30)
print("START")
print("===" * 30)

n  = int(raw_input())
arr = map(int,raw_input().split())
A = set(arr)
scount = int(raw_input())
for _ in range(0,scount):
    cmd = raw_input().split().pop(0)
    B = set(map(int,raw_input().split()))
    A.__getattribute__(cmd)(B)
print(sum(list(A)))
