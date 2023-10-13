# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 14:22:30 2023

@author: maste
"""

n = int(input())
i, x, y = 0, 0, 0
while i < n:
    s = input().split()
    if s[0] == 'север' : y = y + int(s[1])
    elif s[0] == 'юг' : y = y - int(s[1])
    elif s[0] == 'запад': x = x - int(s[1])
    elif s[0] == 'восток' : x = x + int(s[1])
    i = i + 1
print(x,y)


