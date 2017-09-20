#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
import sys
sys.stdin = open("./challenge_sample_input", 'r')
print("===" * 30)
print("SAMPLE OUTPUT:")
print("===" * 30)
print(open("./challenge_sample_output", 'r').read())
print("===" * 30)
print("START")
print("===" * 30)

n = input()
mset = set(map(int, raw_input().split())) 
for arr in [raw_input().split() for _ in range(0,int(raw_input()))]:
    if len(arr) > 1:
        cmd, arg = arr
    else:
        arg = None
        cmd = arr.pop()
    if arg is not None:
        mset.__getattribute__(cmd)(int(arg))
    else:
        mset.__getattribute__(cmd)()
print(sum(mset))
