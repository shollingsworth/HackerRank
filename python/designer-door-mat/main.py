#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __future__
import sys
sys.stdin = open("./stdin.txt", 'r')
# More than 6 lines of code will result in 0 score. Blank lines are not counted.

N, M = map(int,raw_input().split())
for i in xrange(1,N,2): 
    print("".join([ "-" * ((M-(i * 3))/2), ".|." * i, "-" * ((M-(i * 3))/2), ]))
print("WELCOME".join(["-" * ((M-8)/2 + 1), "-" * ((M-8)/2 + 1)]))
for i in xrange(N-2,-1,-2): 
    print("".join([ "-" * ((M-(i * 3))/2), ".|." * i, "-" * ((M-(i * 3))/2), ]))
