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
output_arr = map(str,open(op,'r').read().split('\n'))
banner()
# https://www.hackerrank.com/challenges/2d-array/problem



#!/bin/python
import sys
arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)

all_sums = []
for a in [[x,y] for x in range(6) for y in range(6)]:
    msum = 0
    x,y = a
    a,b = x+3,y+3
    if max([a,b]) > 6: continue
    for idx,n in enumerate([n[y:b] for idx,n in enumerate(arr[x:x+3])]):
        if idx == 1:
            msum += n[1]
        else:
            msum += sum(n)
    all_sums.append(msum)
print(max(all_sums))
