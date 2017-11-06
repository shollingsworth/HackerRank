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

ip = "./input06.txt"
op = "./output06.txt"

output_arr = map(str,open(op,'r').read().split('\n'))
banner()
# https://www.hackerrank.com/challenges/dynamic-array/problem

import sys
def gtype(x,y,qtype,si):
    if qtype == 1:
        seq[str(si)].append(y)
    else:
        la = y % len(seq[str(si)])
        return seq[str(si)][la]

n,q = map(int,raw_input().split(' '))
arr = [map(int,raw_input().split(' ')) for _ in range(q)]
seq = {}
for i in range(n): seq[str(i)] = []
last_answer = 0
for q in arr:
    qtype,x,y = q
    si = (x ^ last_answer) % n
    la = gtype(x,y,qtype,si)
    if la:
        last_answer = la
        print(last_answer)
