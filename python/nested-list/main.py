#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
import sys

sys.stdin = open("./stdin.txt", 'r')

save = {}
save_arr = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    save_arr.append(score)
    save.setdefault(score,[])
    save[score].append(name)
    save[score] = sorted(save[score])
k = sorted(list(set(save_arr)))[1]
print("\n".join(save[k]))
