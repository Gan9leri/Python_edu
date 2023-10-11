# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 22:35:58 2023

@author: maste
"""
a = int(input())
b = int(input())
d = 0
c = 0
for i in range(a, b+1):
    if i % 3 == 0 : 
        c = c + i
        d = d + 1
print(c/d)