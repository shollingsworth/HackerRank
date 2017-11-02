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

ip = "./input01.txt"
op = "./output01.txt"
output_arr = map(str,open(op,'r').read().split('\n'))
banner()
# https://www.hackerrank.com/challenges/python-time-delta/problem

"""
dbg = [
    dt1,
    tz1,
    dt2,
    tz2,
    dt1 - dt2,
    dt2 - dt1,
    (dt1 - tz1) - (dt2 - tz2), #winner winner
    (dt2 - tz2) - (dt1 - tz1),
]
print(json.dumps(dbg, indent=5))
"""

#!/bin/python
import sys
import datetime

def getDate(s):
    dtstr = '%a %d %b %Y %H:%M:%S'
    a = s.split(' ')
    tz = a.pop()
    dt = datetime.datetime.strptime(" ".join(a),dtstr)
    sign,hr,mi = [tz[0:1]] + map(int,[tz[1:3],tz[3:5]])
    if sign == '+':
        dt -= datetime.timedelta(hours=hr,minutes=mi)
    elif sign == '-':
        dt += datetime.timedelta(hours=hr,minutes=mi)
    else:
        raise Exception("Error, invalid sign: {}".format(sign))
    return dt

def time_delta(t1, t2):
    a,b = getDate(t1),getDate(t2)
    return abs(int((a - b).total_seconds()))

for _ in xrange(int(raw_input().strip())):
    t1,t2 = raw_input().strip(), raw_input().strip()
    print(time_delta(t1, t2))
