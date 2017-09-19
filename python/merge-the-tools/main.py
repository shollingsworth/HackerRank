#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
import sys
sys.stdin = open("./challenge_sample_input", 'r')
#print(open("./challenge_sample_output", 'r').read())


def merge_the_tools(string, k):
    #sarr = map(ord,list(string))
    sarr = list(string)
    sections = []
    while sarr:
        sect = []
        for i in range(0,k): sect.append(sarr.pop(0))
        sections.append(sect)

    for sect in sections:
        nsect = []
        while sect:
            nv = sect.pop(0)
            while nv in sect:
                sect.remove(nv)
            nsect.append(nv)
        print("".join(nsect))


# TAIL
if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)
    
