#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
import sys
import json

def banner():
    ban = '====' * 30
    print("{}\nSAMPLE INP:\n{}\n{}".format(ban,ban,open(ip, 'r').read()))
    #print("{}\nSAMPLE OUT:\n{}\n{}".format(ban,ban,open(op, 'r').read()))
    print("{}\nSTART:\n{}".format(ban,ban))
    sys.stdin = open(ip, 'r')

cnt = -1
def comp(inp,ln):
    outl = output_arr[ln]
    if str(inp) != outl:
        raise Exception("Error input output: line {}, file: {}\ngot: {} expected: {}".format(ln,op,inp,outl))






ip = "./challenge_sample_input"
op = "./challenge_sample_output"

ip = "./input03.txt"
op = "./output03.txt"

ip = "./input00.txt"
op = "./output00.txt"

output_arr = map(str,open(op,'r').read().split('\n'))
banner()
# https://www.hackerrank.com/challenges/circular-array-rotation/problem

#!/bin/python
import sys
n,k,q = map(int,raw_input().strip().split(' '))
a = map(int,raw_input().strip().split(' '))
a = a[n-(k%n):n]+a[0:n-(k%n)]
for a0 in xrange(q):
    #cnt += 1
    m = int(raw_input().strip())
    #comp(a[m],cnt)
    print a[m]
