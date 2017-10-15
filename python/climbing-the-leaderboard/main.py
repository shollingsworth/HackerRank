#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
import sys
import json

def banner():
    ban = '====' * 30
    #print("{}\nSAMPLE INP:\n{}\n{}".format(ban,ban,open(ip, 'r').read()))
    #print("{}\nSAMPLE OUT:\n{}\n{}".format(ban,ban,open(op, 'r').read()))
    print("{}\nSTART:\n{}".format(ban,ban))
    sys.stdin = open(ip, 'r')

cnt = -1
def comp(inp,ln):
    outl = output_arr[ln]
    if str(inp) != outl:
        raise Exception("Error input output: line {}, file: {} lv: {}\ngot: {} expected: {}".format(ln,op,lv,inp,outl))

ip = "./challenge_sample_input"
op = "./challenge_sample_output"


ip = "./input07.txt"
op = "./output07.txt"

ip = "./input01.txt"
op = "./output01.txt"

ip = "./input06.txt"
op = "./output06.txt"
banner()
output_arr = map(str,open(op,'r').read().split('\n'))
#https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

#!/bin/python
import sys
n = int(raw_input().strip())
scores = sorted(set(map(int,raw_input().strip().split(' '))),reverse=True)
m = int(raw_input().strip())
alice = map(int,raw_input().strip().split(' '))

l = len(scores)
for i in alice:
    while (l > 0) and (i >= scores[l-1]): l -= 1
    print l+1
