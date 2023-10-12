# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 13:44:31 2023

@author: maste
"""
s = input()
l = len(s)
result = ''
i = 0
j = 1
s = s + '%'
while i < l:
    if s[i] == s[i+1]: j = j + 1
    else:
        result = result + s[i] + str(j)
        j = 1  
    i = i + 1
print (result)