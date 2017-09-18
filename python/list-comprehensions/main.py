#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __future__
import sys

sys.stdin = open("./stdin.txt", 'r')

if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    print([ [i,j,f] for i in range(x + 1) for j in range(y + 1) for f in range(z + 1) if (i + j + f != n)])
