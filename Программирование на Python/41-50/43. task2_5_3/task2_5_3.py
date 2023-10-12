# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 14:33:42 2023

@author: maste
"""
list = input().split()
count = 0
for i in range(0, len(list)):
    count = count + int(list[i])
print(count)