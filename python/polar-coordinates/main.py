#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
import sys
from cmath import *
import cmath
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

z = complex(raw_input())
print("\n".join(map(str,list(cmath.polar(z)))))
