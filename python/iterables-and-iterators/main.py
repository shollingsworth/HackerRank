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

import itertools
N, arr, K = [raw_input() for _ in range(3)]
arr, K = arr.split(), int(K)
match = [i + 1 for i,v in enumerate(arr) if v == 'a']
ita = itertools.combinations(range(1,len(arr) + 1),K)
it = itertools.combinations(range(1,len(arr) + 1),K)
def r(a): 
    if a in match: return True
a = len(list(ita))
b = sum([1 for i in it if bool(list(itertools.ifilter(r,i)))])
print(float(b) / float(a))
