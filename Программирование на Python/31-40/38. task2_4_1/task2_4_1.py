# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 13:34:19 2023

@author: maste
"""
s = input()
G = s.upper().count('G')
C = s.upper().count('C')
l = len(s)
p = ((G + C)/l)*100
print(p)