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
# https://www.hackerrank.com/challenges/validate-a-roman-number/problem

#I, II, III, IV, V, VI, VII, VIII, IX, X
#X, XX, XXX, XL, L, LX, LXX, LXXX, XC, C
#C, CC, CCC, CD, D, DC, DCC, DCCC, CM, M

# helped with: https://stackoverflow.com/questions/267399/how-do-you-match-only-valid-roman-numerals-with-a-regular-expression

import re
thou,hund,tens,sing = 'M{0,3}', '(C[MD]|D?C{0,3})', '(X[CL]|L?X{0,3})', '(I[VX]|V?I{0,3})'
regex = thou+hund+tens+sing+'$'
print(bool(re.match(regex, raw_input())))
