#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __future__
import sys
sys.stdin = open("./stdin.txt", 'r')

def split_and_join(line):
   return "-".join(line.split(" "))


split_and_join(raw_input().strip())
