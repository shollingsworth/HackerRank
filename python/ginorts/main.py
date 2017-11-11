#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
import sys
import json

def banner():
    ban = '====' * 30
    print("{}\nSAMPLE INP:\n{}\n{}".format(ban, ban, open(ip, 'r').read()))
    print("{}\nSAMPLE OUT:\n{}\n{}".format(ban, ban, open(op, 'r').read()))
    print("{}\nSTART:\n{}".format(ban, ban))
    sys.stdin = open(ip, 'r')

cnt = -1
def comp(inp, ln):
    outl = output_arr[ln]
    if str(inp) != outl:
        raise Exception("Error input output: line {}, file: {}\ngot: {} expected: {}".format(ln, op, inp, outl))


ip = "./challenge_sample_input"
op = "./challenge_sample_output"
output_arr = map(str, open(op, 'r').read().split('\n'))
banner()
# https://www.hackerrank.com/challenges/ginorts/problem
s = raw_input()
a = reduce(lambda x,y: x+y,map(lambda v: range(*v),[[97,123,1], [65,91,1], [49,58,2], [48,58,2]]))
m = dict(zip(map(chr,a),range(len(a) + 1)))
i = dict(zip(m.values(),m.keys()))
print(reduce(lambda x,y: x+y,map(lambda x: i[x],sorted(map(lambda x: m[x],list(s))))))
