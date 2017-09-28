#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
import sys
print("===" * 30)
print("SAMPLE INPUT:")
print("===" * 30)
print(open("./challenge_sample_input", 'r').read())
sys.stdin = open("./challenge_sample_input", 'r')
print("===" * 30)
print("SAMPLE OUTPUT:")
print("===" * 30)
print(open("./challenge_sample_output", 'r').read())
print("===" * 30)
print("START")
print("===" * 30)


#!/bin/python
import sys
def div(arr):
    return (len(arr) / float(n))
n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
zero, pos, neg = map(div,[[x for x in arr if x == 0], [x for x in arr if x > 0],[x for x in arr if x < 0]])
print("{}\n{}\n{}\n".format(pos,neg,zero))
