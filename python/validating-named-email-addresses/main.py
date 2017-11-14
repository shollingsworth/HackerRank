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

ip = "./input01.txt"
op = "./output01.txt"

ip = "./input06.txt"
op = "./output06.txt"

output_arr = map(str,open(op,'r').read().split('\n'))
banner()
# https://www.hackerrank.com/challenges/validating-named-email-addresses/problem

import email.utils as eutil
import re
regex = '^[a-zA-Z][a-zA-Z-_\.0-9]*@[A-Za-z]+\.[A-Za-z]{1,3}$'
for addy in [raw_input() for _ in range(int(raw_input()))]:
    name, email = eutil.parseaddr(addy)
    if re.match(regex,email):
        print(eutil.formataddr((name, email)))
