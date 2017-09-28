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

#!/bin/python
import sys
s,t = map(int,raw_input().strip().split(' '))
a,b = map(int,raw_input().strip().split(' ')) 
raw_input().strip().split(' ') # ignoring counts, C++ stuff
apple, orange = [map(int,raw_input().strip().split(' ')) for _ in range(2)]
print(sum([1 for f in apple if s <= (a + f) <= t]))
print(sum([1 for f in orange if s <= (b + f) <= t]))
