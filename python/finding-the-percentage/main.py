#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __future__
import sys

sys.stdin = open("./stdin.txt", 'r')

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    msum = 0
    arr = student_marks[query_name]
    for i in arr: msum += i
    print('{:.2f}'.format(msum/len(arr)))
