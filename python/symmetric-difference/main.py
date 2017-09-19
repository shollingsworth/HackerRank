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

mset = {}
for _ in range(0,2):
    mset[_] = set()
    n = int(raw_input())
    for i in map(int, raw_input().split()): mset[_].add(i)

out = set()
for i in mset[0].difference(mset[1]): out.add(i)
for i in mset[1].difference(mset[0]): out.add(i)
for i in sorted(out):
    print(i)
