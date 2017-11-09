#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
import sys
import json

def banner():
    ban = '====' * 30
    #print("{}\nSAMPLE INP:\n{}\n{}".format(ban,ban,open(ip, 'r').read()))
    #print("{}\nSAMPLE OUT:\n{}\n{}".format(ban,ban,open(op, 'r').read()))
    #print("{}\nSTART:\n{}".format(ban,ban))
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
# https://www.hackerrank.com/challenges/python-sort-sort/problem

#!/bin/python
import sys
n, m = map(int,raw_input().strip().split(' '))
arr = [ map(int,raw_input().strip().split(' ')) for arr_i in xrange(n) ]
assert len(arr) == n
for i in arr: assert len(i) == m
k = int(raw_input().strip())
sdict = [ int(i.split(':')[1]) for i in sorted([ '{:04d}:{:04d}'.format(v,idx) for idx,v in enumerate(zip(*arr)[k]) ]) ]
for i in sdict: print(" ".join(map(str,arr[i])))
