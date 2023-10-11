# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 22:11:50 2023

@author: maste
"""

#Сколько всего знаков * будет выведено после исполнения фрагмента программы:
count = 0
i = 0
while i < 5:
    print('*')
    count = count + 1
    if i % 2 == 0:
        print('**')
        count = count + 2
    if i > 2:
        print('***')
        count = count + 3
    i = i + 1
print(count)