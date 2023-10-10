# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 22:16:32 2023

@author: maste
"""

A = int(input())
B = int(input())
H = int(input())
if H >= A and H <= B :
    print('Это нормально')
elif H < A :
    print('Недосып')
elif H > B:
    print('Пересып')
