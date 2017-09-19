#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
import sys
sys.stdin = open("./challenge_sample_input", 'r')
out = file("./challenge_sample_output", 'r').read()
print("ANSWER:\n{}\n\n{}\n{}\n\n".format(out,"=*=" * 25,"=*=" * 25))

# TEMPLATE
def print_rangoli(size):
    output = []
    ar = map(chr,range(97,123)[:size])
    width = (len(ar) * 4) - 2
    while ar:
        m = ar.pop(0)
        line = '-'.join(list(reversed(ar[:])) + [m] + list(ar[:]))
        output.append("{:-^{}}".format(line,width - 1))
    print("\n".join(list(reversed(output[1:])) + output))

# TAIL
if __name__ == '__main__':
    n = int(raw_input())
    print_rangoli(n)
