#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __future__
import sys
sys.stdin = open("./stdin.txt", 'r')

def mutate_string(string, position, character):
    a1 = list(string)
    a1[position] = character
    return "".join(a1)


mystr = raw_input()
(pos,char) = raw_input().split(" ")
print(mutate_string(mystr,int(pos),char))
