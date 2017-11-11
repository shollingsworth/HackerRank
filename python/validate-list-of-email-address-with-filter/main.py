#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __future__
import sys
import json

def banner():
    ban = '====' * 30
    print("{}\nSAMPLE INP:\n{}\n{}".format(ban,ban,open(ip, 'r').read()))
    print("{}\nSAMPLE OUT:\n{}\n{}".format(ban,ban,open(op, 'r').read()))
    print("{}\nSTART:\n{}".format(ban,ban))
    sys.stdin = open(ip, 'r')

cnt = -1
def comp(inp,ln):
    outl = output_arr[ln]
    if str(inp) != outl:
        raise Exception("Error input output: line {}, file: {}\ngot: {} expected: {}".format(ln,op,inp,outl))


ip = "./challenge_sample_input"
op = "./challenge_sample_output"

ip = "./input05.txt"
op = "./output05.txt"
output_arr = map(str,open(op,'r').read().split('\n'))
banner()
# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem

def fun(s):
    let = range(ord('A'),ord('Z')+1) + range(ord('a'),ord('z')+1)
    sym = map(ord,list('-_'))
    dig = range(ord('0'),ord('9')+1)
    a = s.split('@')
    if len(a) != 2: return False
    user,dom = a[0],a[1].split('.')
    if len(dom) != 2: return False
    web, ext = dom
    if len(ext) > 3: return False
    utf = [True if i in let+sym+dig else False for i in map(ord,list(user))]
    dtf = [True if i in let+dig else False for i in map(ord,list(web))]
    lng = [True if len(i) > 0 else False for i in [user,web,ext]]
    tests = utf + dtf + lng
    if not all(tests): return False
    return True

def filter_mail(emails):
    return filter(fun, emails)

print(sorted(filter_mail([ raw_input() for _ in range(int(raw_input())) ] + ['blarg@hello@foo','foo@hello.comm','f*@blarg.com','fudge@blar_.com'])))
