# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 14:50:42 2023

@author: maste
"""
lst = [int(i) for i in input().split()]
x = int(input())
n = int(len(lst))
list_out = []
for i in range(n): 
    if x == lst[i]: list_out.append(i)
if len(list_out) == 0 : print('Отсутствует')
else: print(*list_out)