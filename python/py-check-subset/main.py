#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
import sys
print("===" * 30)
print("SAMPLE INPUT:")
print("===" * 30)
print(open("./challenge_sample_input", 'r').read())
sys.stdin = open("./challenge_sample_input", 'r')
print("===" * 30)
print("SAMPLE OUTPUT:")
print("===" * 30)
print(open("./challenge_sample_output", 'r').read())
print("===" * 30)
print("START")
print("===" * 30)

for i in range(int(raw_input())): #More than 4 lines will result in 0 score. Blank lines won't be counted.  
    a, A = int(raw_input()), set(raw_input().split())
    b, B = int(raw_input()), set(raw_input().split())
    print(A.issubset(B))
