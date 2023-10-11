# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 22:35:30 2023

@author: maste
"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
for i in range(c, d + 1):
    print('\t', i, end = '')
print()
for j in range(a, b + 1):
    print(j, end = '')
    for k in range(c, d + 1):
        print ('\t', j*k, end = '')
    print()