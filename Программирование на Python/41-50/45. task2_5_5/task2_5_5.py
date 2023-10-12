# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 14:33:42 2023

@author: maste
"""
list_in = [int(i) for i in input().split()]
n = len(list_in)
list_out = []
for i in range(0, n):
    a = list_in[i]
    for j in range(0, n):
      if (a == list_in[j] and i != j): 
          list_out.append(a)
          break
list_out = list(set(list_out))
n = len(list_out)
for i in range(0, n): print(list_out[i], end = ' ')