#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
import sys
sys.stdin = open("./input03.txt", 'r')
print("===" * 30)
print("SAMPLE OUTPUT:")
print("===" * 30)
print(open("./challenge_sample_output", 'r').read())
print("===" * 30)
print("START")
print("===" * 30)

hap = 0
n,m = map(int,raw_input().split())
arr, y, z = [map(int,raw_input().split()) for x in range(0,3)]
A, B = [set(y),set(z)]
for i in arr:
    if i in A: hap += 1
    if i in B: hap -= 1
print(hap)
