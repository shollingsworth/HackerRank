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

arr = [ raw_input().split() for _ in range(1,5)]
n,A,n,B = [set(i) for i in arr]
print(len(A.symmetric_difference(B)))
