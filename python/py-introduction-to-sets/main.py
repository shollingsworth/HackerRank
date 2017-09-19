#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
import sys
sys.stdin = open("./challenge_sample_input", 'r')
print("===" * 30)
print("SAMPLE OUTPUT:")
print("===" * 30)
print(open("./challenge_sample_output", 'r').read())
print("===" * 30)
print("START")
print("===" * 30)

def average(array):
    s = set(array)
    return float(sum(s)) / len(s)

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print result
