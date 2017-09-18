#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __future__
import sys
sys.stdin = open("./stdin.txt", 'r')

def print_full_name(a, b):
    print("Hello {} {}! You just delved into python.".format(a,b))

print_full_name(raw_input(),raw_input())
