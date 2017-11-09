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



ip = "./input01.txt"
op = "./output01.txt"

ip = "./challenge_sample_input"
op = "./challenge_sample_output"

ip = "./input03.txt"
op = "./output03.txt"

output_arr = map(str,open(op,'r').read().split('\n'))
banner()
# https://www.hackerrank.com/challenges/any-or-all/problem

n,a = int(raw_input()), raw_input().split(' ')
print(all(['-' not in list(i) for i in a]) and any( [ i == i[::-1] for i in a ]))

#print(all([ n == len(a), any([ i[0:(len(i) - len(i) % 2) / 2] == i[(len(i) - len(i) % 2) / 2+len(i)%2:] for i in map(str,b) ] + [ len(a) - len(b) > 0 ]) ]))
# 3rd try, really great solution here that I tried for myself
# https://www.hackerrank.com/challenges/any-or-all/forum/comments/132851
