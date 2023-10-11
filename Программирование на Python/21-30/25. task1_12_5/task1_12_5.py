# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 21:23:34 2023

@author: maste
"""
a = int(input())
b = int(input())
c = int(input())
if a > b: a, b = b, a
if b > c: b, c = c, b
if a > b: a, b = b, a
print(c)
print(a)
print(b)