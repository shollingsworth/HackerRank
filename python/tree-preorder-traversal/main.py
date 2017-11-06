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
output_arr = map(str,open(op,'r').read().split('\n'))
banner()
# https://www.hackerrank.com/challenges/tree-preorder-traversal/problem

class Node(object):
    def __init__( self, data=None) :
        self.data  = data
        self.left  = None
        self.right = None

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def addLeft(self,data):
        node = Node(data=data)
        self.left = node
        return self

    def addRight(self,data):
        node = Node(data=data)
        self.right = node
        return self

a = Node(1)
b = a.addRight(2).getRight()
c = b.addRight(5).getRight()
d = c.addLeft(3).addRight(6).getLeft()
d.addRight(4)

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
import sys
def preOrder(root):
    if root.data is not None:
        sys.stdout.write(str(root.data) + ' ')
    if root.left is not None:
        preOrder(root.left)
    if root.right is not None:
        preOrder(root.right)

preOrder(a)
