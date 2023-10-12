# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 17:27:34 2023

@author: maste
"""
stat = {}
s = input().lower().split()
for i in range(len(s)):
    key = s[i]
    stat[key] = s.count(s[i])
for key, value in stat.items():
    print(key, value)