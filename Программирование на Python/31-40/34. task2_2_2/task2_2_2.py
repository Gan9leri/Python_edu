# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 22:27:25 2023

@author: maste
"""

#Определите, какое значение будет иметь переменная 
#i после выполнения следующего фрагмента программы:

i = 0
s = 0
while i < 10:
    i = i + 1
    s = s + i
    if s > 15:
        continue
    i = i + 1
print(i)