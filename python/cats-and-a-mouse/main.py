#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
import sys
print("===" * 30)
print("SAMPLE INPUT:")
print("===" * 30)
"""
print(open("./challenge_sample_input", 'r').read())
sys.stdin = open("./challenge_sample_input", 'r')
"""
#print(open("./input01.txt", 'r').read())
sys.stdin = open("./input01.txt", 'r')

print("===" * 30)
print("SAMPLE OUTPUT:")
print("===" * 30)
#print(open("./output01.txt", 'r').read())
fout = open("./output01.txt", 'r').read().split('\n')
#print(open("./challenge_sample_output", 'r').read())
print("===" * 30)
print("START")
print("===" * 30)

#!/bin/python
import sys
for _ in xrange(int(raw_input().strip())):
    A,B,C = map(int,raw_input().strip().split(' '))
    ac = abs(A-C)
    bc = abs(B-C)
    if ac == bc:
        print "Mouse C"
        continue
    d = {
        ac : 'Cat A',
        bc : 'Cat B',
    }
    print(d[min(d.keys())])
