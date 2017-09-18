#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __future__
import sys

sys.stdin = open("./stdin.txt", 'r')

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = tuple(map(int, raw_input().split()))
    print(hash(integer_list))
