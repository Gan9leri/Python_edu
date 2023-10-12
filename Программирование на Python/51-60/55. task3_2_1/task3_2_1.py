# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 17:18:00 2023

@author: maste
"""
def update_dictionary(d, key, value):
    if key in d: 
        d[key].append(value)
    if key not in d:
        if 2*key in d:
            d[2*key].append(value)
        if 2*key not in d:
            d[2*key] = []
            d[2*key].append(value)