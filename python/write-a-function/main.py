#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __future__
import sys
import os
import logging

def is_leap(year):
    leap = False
    tests = [
        year % 4,
        year % 100,
        year % 400
    ]
    if not tests[0]:
        leap = True
        if not tests[1]:
            leap = False
            if not tests[2]:
                leap = True
    return leap

for i in range(1900,10 ** 5):
    is_leap(i)
