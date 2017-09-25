#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
#import cmath
import math
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

A,B = [int(raw_input()) for _ in range(2)]
C = math.sqrt( (A ** 2) + (B ** 2)) 
print(A,B,C)
