#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
import sys
#sys.stdin = open("./challenge_sample_input", 'r')
sys.stdin = open("./input12.txt", 'r')
print(open("./challenge_sample_output", 'r').read())

def minion_game(string):
    score = {
        #cons
        'stuart': 0,
        #vowel
        'kevin': 0,
    }
    sarr = map(ord,list(string))
    alpha = range(65,91)
    vowels = (65,69,73,79,85)
    for v in vowels: alpha.remove(v)
    s_starts = []
    k_starts = []
    for idx, val in enumerate(sarr):
        if val in alpha: s_starts.append(idx)
        if val in vowels: k_starts.append(idx)
    for k in k_starts: score['kevin'] += len(sarr) - k
    for s in s_starts: score['stuart'] += len(sarr) - s
    ks = score['kevin']
    ss = score['stuart']
    if ks == ss:
        retval = "Draw"
    elif ks > ss:
        retval = "Kevin {}".format(ks)
    else:
        retval = "Stuart {}".format(ss)
    print(retval)

# TAIL
if __name__ == '__main__':
    s = raw_input()
    minion_game(s)
