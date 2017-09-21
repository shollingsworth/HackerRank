#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
import sys
print("===" * 30)
print("SAMPLE INPUT:")
print("===" * 30)
#print(open("./input01.txt", 'r').read())
sys.stdin = open("./input01.txt", 'r')
print("===" * 30)
print("SAMPLE OUTPUT:")
print("===" * 30)
print(open("./output01.txt", 'r').read())
print("===" * 30)
print("START")
print("===" * 30)

#Not my solution - https://www.hackerrank.com/challenges/py-the-captains-room/forum/comments/133372
K, A = int(raw_input()), map(int,raw_input().split())
C = set(A)
print(
    ((sum(C)*K) - (sum(A))) // (K-1)
)
