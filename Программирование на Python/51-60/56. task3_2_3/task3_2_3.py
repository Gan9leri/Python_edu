# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 17:27:34 2023

@author: maste
"""
n = int(input())
s1 = []
s2 = []
num = {}
i = 0
while i < n:
    s1.append(int(input()))
    i = i + 1
for i in range(len(s1)):
    if s2.count(s1[i]) == 0 :
        s2.append(s1[i])
        key = s1[i]
        num[key] = f(s1[i])
        print(num[key])
    elif s2.count(s1[i]) != 0 :
        print(num[s1[i]])