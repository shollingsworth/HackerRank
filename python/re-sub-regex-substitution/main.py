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


ip = "./input06.txt"
op = "./output06.txt"

ip = "./challenge_sample_input"
op = "./challenge_sample_output"

output_arr = map(str,open(op,'r').read().split('\n'))
banner()
# https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem

import re
s = "\n".join([raw_input() for _ in range(int(raw_input()))])
regexes = map(re.escape,[' && ',' || '])
replace = [' and ',' or ']
while True in [ bool(re.search(regex,s)) for regex in regexes ]:
    a1,b1 = regexes
    a2,b2 = replace
    s = re.sub(a1,a2,s)
    s = re.sub(b1,b2,s)
print(s)


"""
solution #1
mmap = {
}
for repl, arr in mmap.items():
    regex, orig = arr
    for m in re.finditer(regex,s):
        if re.match(' ',m.group(1)):
            s = re.sub(orig,repl,s)
print(s)

"""
