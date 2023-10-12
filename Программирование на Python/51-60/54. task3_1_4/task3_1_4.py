# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 17:07:18 2023

@author: maste
"""

def modify_list(l):
    i = len(l) - 1
    while i >= 0:
        if l[i] % 2 != 0 : l.pop(i)
        else: l[i] = int(l[i] / 2)
        i = i - 1