# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 14:42:39 2023

@author: maste
"""
n = int(input())
list_out = []
flag = 0
if n == 1: list_out.append(1)
elif n == 2: 
    list_out.append(1)
    list_out.append(2)
else:
    for i in range(n):
        for j in range(i):
            list_out.append(i)
            if len(list_out) == n:
                flag = 1
                break  
        if flag == 1 : break
print(*list_out)