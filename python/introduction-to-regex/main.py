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

ip = "./input04.txt"
op = "./output04.txt"

ip = "./input01.txt"
op = "./output01.txt"

ip = "./input02.txt"
op = "./output02.txt"
output_arr = map(str,open(op,'r').read().split('\n'))
banner()
# https://www.hackerrank.com/challenges/introduction-to-regex/problem

import re
pattern = '^[+-]{0,1}[0-9]*\.[0-9]+$'
print("\n".join(map(str,[ bool(re.match(pattern, raw_input())) for _ in range(int(raw_input())) ])))
