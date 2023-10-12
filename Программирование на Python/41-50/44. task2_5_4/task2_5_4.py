# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 14:33:42 2023

@author: maste
"""
list_in = [int(i) for i in input().split()]
for i in range(0, len(list_in)): list_in[i] = int(list_in[i])
n = int(len(list_in))
list_out = [0] * n
for i in range(0, n):
    if n == 1 :
        list_out[i] = list_in[i]
        print(list_out[i])
        break
    elif i == 0 : list_out[i] = list_in[i+1] + list_in[n-1]
    elif i == n-1:
        list_out[i] = list_in[i-1] + list_in[0] 
    else: list_out[i] = list_in[i+1] + list_in[i-1]
    print(list_out[i], end = ' ')