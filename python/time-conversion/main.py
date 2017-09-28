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
def timeConversion(s):
    hour,minute,second = s.split(':')
    pm = False
    if second.find('PM') >= 0:
        second = second.replace('PM','')
        pm = True
    else:
        second = second.replace('AM','')
    hour,minute,second = map(int,[hour,minute,second])
    if pm and hour != 12: hour += 12
    if not pm and hour == 12: hour = 0
    return "{:02d}:{:02d}:{:02d}".format(hour,minute,second)

s = raw_input().strip()
result = timeConversion(s)
print(result)
