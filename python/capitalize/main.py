#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
import sys
sys.stdin = open("./challenge_sample_input", 'r')
print(open("./challenge_sample_input", 'r').readline().strip())
print(open("./challenge_sample_output", 'r').readline().strip())
print("===========")


# TEMPLATE
def capitalize(string):
    retval = []
    arr = string.split(" ")
    for i in arr:
        starts_with_num = False
        for z in range(0,10):
            if i.startswith(str(z)):
                starts_with_num = True
                break
        if starts_with_num:
            retval.append(i)
        else:
            retval.append(i.title())
    return " ".join(retval)

# TAIL
if __name__ == '__main__':
    string = raw_input()
    capitalized_string = capitalize(string)
    print capitalized_string
