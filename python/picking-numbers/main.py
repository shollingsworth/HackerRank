#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
import sys

ip = "./input06.txt"
op = "./output06.txt"

ip = "./input07.txt"
op = "./output07.txt"

ip = "./challenge_sample_input"
op = "./challenge_sample_output"

ip = "./challenge_sample_input1.txt"
op = "./challenge_sample_output1.txt"

ip = "./input02.txt"
op = "./output02.txt"

ip = "./input04.txt"
op = "./output04.txt"

print("===" * 30)
print("SAMPLE INPUT:")
print("===" * 30)
print(open(ip, 'r').read())
sys.stdin = open(ip, 'r')
print("===" * 30)
print("SAMPLE OUTPUT:")
print("===" * 30)
print(open(op, 'r').read())
print("===" * 30)
print("START")
print("===" * 30)

#!/bin/python
import sys
import itertools
n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
assert len(a) == n
arr_set = list(set(a))
all_sets = [ [v for v in a[:] if v in i] for i in itertools.combinations(arr_set,2) ] 
singles = max([a.count(i) for i in arr_set])
if all_sets:
    set_nums = max([len(v) for v in all_sets if max(v) - min(v) <= 1])
else:
    set_nums = 0
print(max([singles,set_nums]))
