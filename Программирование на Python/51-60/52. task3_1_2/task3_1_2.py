# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 16:57:59 2023

@author: maste
"""
def f(x):
    if x <= -2: return 1 - ( x + 2 )**2
    elif x > -2 and x <= 2 : return - (x / 2)
    elif x > 2 : return ( x - 2 )**2 + 1