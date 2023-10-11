# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 23:55:48 2023

@author: maste
"""

a = int(input())
b = int(input())
c = int(input())
p = (a + b + c)/2
S = ( p * (p - a) * (p - b) * ( p - c ) ) ** 0.5
print(S)