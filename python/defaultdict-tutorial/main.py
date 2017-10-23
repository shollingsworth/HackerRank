#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
import sys
import json

def banner():
    ban = '====' * 30
    print("{}\nSAMPLE INP:\n{}\n{}".format(ban,ban,open(ip, 'r').read()))
    print("{}\nSAMPLE OUT:\n{}\n{}".format(ban,ban,open(op, 'r').read()))
    print("{}\nSTART:\n{}".format(ban,ban))
    sys.stdin = open(ip, 'r')

cnt = -1
def comp(inp,ln):
    outl = output_arr[ln]
    if str(inp) != outl:
        raise Exception("Error input output: line {}, file: {}\ngot: {} expected: {}".format(ln,op,inp,outl))


ip = "./challenge_sample_input"
op = "./challenge_sample_output"

ip = "./input01.txt"
op = "./output01.txt"
output_arr = map(str,open(op,'r').read().split('\n'))
banner()
# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

import sys
from collections import defaultdict
n,m = map(int,raw_input().split(' '))
A = [raw_input() for _ in range(n)]
B = [raw_input() for _ in range(m)]

track = defaultdict(list)
for idx,v in enumerate(A):
    track[v].append(idx + 1)
for i in B:
    if i not in A:
        print(-1)
    else:
        print(" ".join(map(str,track[i])))
