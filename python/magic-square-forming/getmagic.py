#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
import sys
import itertools
def getSets(arr_size):
    sets = []
    for i in getSplit([[i,y] for i in range(arr_size) for y in range(arr_size)],arr_size): sets.append(i)
    for i in getSplit([[y,i] for i in range(arr_size) for y in range(arr_size)],arr_size): sets.append(i)
    sets.append([[i,i] for i in range(arr_size)])
    sets.append([[i,arr_size-i-1] for i in range(arr_size)])
    return sets

def getSplit(arr,x):
    blarg = []
    for i in range(0, len(arr), x): blarg.append(arr[i:i+x])
    return blarg

def getVal(s,arr):
    sval = []
    for i in arr:
        x,y = i
        sval.append(s[x][y])
    return sval

def getScore(s,sets):
    sval = [sum(getVal(s,i)) for i in sets]
    mi,mx = min(sval), max(sval)
    return mx - mi

def getMagics(arr_size):
    sq = arr_size * arr_size
    nums = range(1,sq + 1)
    sets = getSets(arr_size)
    magics = []
    for i in itertools.permutations(nums,sq):
        s = getSplit(list(i),arr_size)
        sc = getScore(s,sets)
        if sc == 0:  magics.append(list(i))
    return magics

magics = getMagics(3)
for i in magics: print(i)
