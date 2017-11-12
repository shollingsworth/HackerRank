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







ip = "./input03.txt"
op = "./output03.txt"

ip = "./challenge_sample_input"
op = "./challenge_sample_output"

ip = "./input01.txt"
op = "./output01.txt"

ip = "./input02.txt"
op = "./output02.txt"

output_arr = map(str,open(op,'r').read().split('\n'))
banner()
# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem

import re
c,v = 'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm', 'AEIOUaeiou'
r = [i.group(1) for i in re.finditer(r'([{}]{{2,}})[{}]'.format(v,c),re.escape(raw_input()))]
print("\n".join(r) if len(r) else -1)
