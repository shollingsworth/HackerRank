#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
import sys
print("===" * 30)
print("SAMPLE INPUT:")
print("===" * 30)
#print(open("./challenge_sample_input", 'r').read())
sys.stdin = open("./input05.txt", 'r')
print("===" * 30)
print("SAMPLE OUTPUT:")
print("===" * 30)
#print(open("./challenge_sample_output", 'r').read())
print("===" * 30)
print("START")
print("===" * 30)

#!/bin/python
import sys
l_dict = {}
for i in [str(raw_input().strip()) for _ in xrange(int(raw_input().strip()))]:
    ilen = len(i)
    l_dict.setdefault(ilen,[])
    l_dict[ilen].append(i)
is_sorted = [s for i in sorted(l_dict.keys()) for s in sorted(l_dict[i])]
for s in is_sorted: print(s)
