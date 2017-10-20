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
        raise Exception("Error input output: line {}, file: {}\ngot: {} expected: {}".format(ln+1,op,inp,outl))


ip = "./challenge_sample_input"
op = "./challenge_sample_output"

ip = "./input0x.txt"
op = "./output0x.txt"

ip = "./input07.txt"
op = "./output07.txt"

ip = "./input00.txt"
op = "./output00.txt"

output_arr = map(str,open(op,'r').read().split('\n'))
banner()
# https://www.hackerrank.com/challenges/save-the-prisoner/problem

#!/bin/python
import sys
def saveThePrisoner(n, m, s):
    pris, sweets, pid = n,m,s
    sweets = sweets % pris
    b = ((sweets + pid) - 1) - pris
    v = abs(pris + b)
    if v == 0:
        return abs(b)
    elif b <= 0:
        return v
    else:
        return b

for a0 in xrange(int(raw_input().strip())):
    #cnt += 1
    n, m, s = map(int,raw_input().strip().split(' '))
    result = saveThePrisoner(n, m, s)
    #comp(result,cnt)
    print(result)
