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
def getTotalX(a, b):
    cnt = 0
    for x in range(1,101):
        a1 = [n for n in a if (x % n) == 0]
        b1 = [n for n in b if (n % x) == 0]
        if a == a1 and b == b1: cnt += 1
    return cnt

if __name__ == "__main__":
    n, m = map(int,raw_input().strip().split(' '))
    a = map(int, raw_input().strip().split(' '))
    b = map(int, raw_input().strip().split(' '))
    print getTotalX(a, b)
