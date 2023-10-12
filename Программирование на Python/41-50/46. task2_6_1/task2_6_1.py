# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 14:40:43 2023

@author: maste
"""
list_in = []
sum, sum_square = -1, 0
while sum != 0:
    sum = 0
    list_in.append(int(input()))
    for i in range(len(list_in)): sum += list_in[i]
for i in range(len(list_in)): sum_square += list_in[i]**2
print(sum_square)    