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

ip = "./challenge_sample_input2"
op = "./challenge_sample_output2"
output_arr = map(str,open(op,'r').read().split('\n'))
banner()
# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple
lines = int(raw_input())
Case = namedtuple('Case',map(str,raw_input().split()))
cols = [Case(*raw_input().split()) for _ in range(lines)]
print(sum([float(i.MARKS) for i in cols])/len(cols))
