#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __future__
import sys

sys.stdin = open("./stdin.txt", 'r')

arr = []
N = int(raw_input())
while N:
    line = raw_input()
    tarr = line.split()
    action = tarr.pop(0)
    if action == 'insert':
        idx = int(tarr.pop(0))
        val = tarr.pop(0)
        arr.insert(idx,int(val))
    elif action == 'remove':
        val = int(tarr.pop(0))
        arr.remove(val)
    elif action == 'append':
        val = int(tarr.pop(0))
        arr.append(val)
    elif action == 'print':
        print(arr)
    elif action == 'sort':
        arr = sorted(arr)
    elif action == 'pop':
        arr.pop()
    elif action == 'reverse':
        arr.reverse()
    N += -1
