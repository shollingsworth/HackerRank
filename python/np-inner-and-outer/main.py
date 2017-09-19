#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
import sys
import numpy
sys.stdin = open("./challenge_sample_input", 'r')
print("===" * 30)
print("SAMPLE OUTPUT:")
print("===" * 30)
print(open("./challenge_sample_output", 'r').read())
print("===" * 30)
print("START")
print("===" * 30)

A = numpy.array(map(int,raw_input().split()))
B = numpy.array(map(int,raw_input().split()))
print(numpy.inner(A,B))
print(numpy.outer(A,B))
