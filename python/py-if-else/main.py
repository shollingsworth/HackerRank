#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __future__

#n = int(raw_input())

for n in range(1,100):
    if n % 2:
        print "Weird"
    elif n in range(2,5):
        print "Not Weird"
    elif n in range(6,21):
        print "Weird"
    elif n > 20:
        print "Not Weird"
