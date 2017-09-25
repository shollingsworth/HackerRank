#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
import sys
print("===" * 30)
print("SAMPLE INPUT:")
print("===" * 30)
print(open("./input14.txt", 'r').read())
sys.stdin = open("./input14.txt", 'r')

#print(open("./challenge_sample_input", 'r').read())
#sys.stdin = open("./challenge_sample_input", 'r')

print("===" * 30)
print("SAMPLE OUTPUT:")
print("===" * 30)

print(open("./output14.txt", 'r').read())

#print(open("./challenge_sample_output", 'r').read())

print("===" * 30)
print("START")
print("===" * 30)

import itertools
K,M = map(int,raw_input().split())
a = [i for i in [map(int,raw_input().split())[1:] for _ in range(K)]]
def T(a): return sum([i ** 2 for i in a]) % M
print(max([T(n) for n in itertools.product(*a)]))
