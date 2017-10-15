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
# https://www.hackerrank.com/challenges/utopian-tree/problem

#!/bin/python
import sys
for i in [int(raw_input().strip()) for x in xrange(int(raw_input().strip()))]:
    h = 1
    c = 0
    while i > 0:
        c += 1
        if c % 2 == 0:
            h += 1
        else:
            h += h
        i -= 1
    print(h)
