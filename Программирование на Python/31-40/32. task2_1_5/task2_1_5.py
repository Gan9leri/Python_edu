# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 22:11:50 2023

@author: maste
"""
a = int(input())
b = int(input())
nok = 0
if a % b == 0: nok = a
else:
    ab = a * b
    while (a != 0) and (b != 0):
        if (a > b):
            a = a % b
        elif (a < b):
            b = b % a
    nod = a + b
    nok = int((ab)/nod)
print(nok)