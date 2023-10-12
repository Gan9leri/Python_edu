# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 14:03:18 2023

@author: maste
"""

a = [1, 2, 3]
b = a
print(b)

a[1] = 10
print(b)

b[0] = 20
print(a)

a = [5, 6]
print(b)