#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __future__
import sys
sys.stdin = open("./stdin.txt", 'r')

def print_formatted(number):
    retarr = []
    output = []
    max_pad = 0
    for n in range(1,number + 1):
        narr = []
        narr.append(n) #Decimal
        narr.append(format(n,'o')) # Octal
        narr.append(format(n,'x').upper()) # Hexadecimal (capitalized)
        narr.append(format(n,'b')) #    Binary
        for l in narr:
            if len(str(l)) > max_pad:
                max_pad = len(str(l))
        retarr.append(narr)
    for s in retarr:
        narr = []
        for i in s: narr.append('{:>{}}'.format(i,max_pad))
        print(" ".join(narr))

if __name__ == '__main__':
    print_formatted(int(raw_input()))
