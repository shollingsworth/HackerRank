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
# https://www.hackerrank.com/challenges/py-collections-deque/problem

from collections import deque
d = deque()
cmds = [raw_input() for _ in range(int(raw_input()))]
cmap = {
    'append': d.append,
    'pop': d.pop,
    'popleft': d.popleft,
    'appendleft': d.appendleft,
}


for cmd in  [i.split() for i in cmds]:
    ecmd = cmap[cmd.pop(0)]
    if cmd:
        v = cmd.pop(0)
        ecmd(v)
    else:
        ecmd()
print(" ".join(map(str,d)))
