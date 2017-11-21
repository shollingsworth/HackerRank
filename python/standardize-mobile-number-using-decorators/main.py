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
# https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem

def wrapper(f):
    def fun(l):
        r = []
        for n in l:
            c = n[::-1][:10][::-1]
            tarr = ['+91',c[:5],c[5:10]]
            r.append(" ".join(tarr))
        return f(r)
    return fun

@wrapper
def sort_phone(l):
    print('\n'.join(sorted(l)))

if __name__ == '__main__':
    l = [raw_input() for _ in range(int(input()))]
    sort_phone(l)
