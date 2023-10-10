# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 21:31:22 2023

@author: maste
"""

X = int(input())
H = int(input())
M = int(input())
Y = (H*60 + M) + X
print(Y//60)
print(Y%60)