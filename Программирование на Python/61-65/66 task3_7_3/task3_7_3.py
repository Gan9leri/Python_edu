# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:10:25 2023

@author: maste
"""
#Функция наполнения множества
def fill_set(f_set, k):
    i = 0
    while i < k :
        s = input().split()
        for j in range(len(s)):
            f_set.add(s[j].lower())
        i = i + 1

orf = set() #множество корректных слов
in_s = set() #входная строка со словами
out = set() #множество ошибок

#заполняем множество корректных слов
d = int(input())
fill_set(orf, d)

#Заполняем множество слов входной строки
l = int(input())
fill_set(in_s, l)

#Заполняем множество ошибок
out = list(in_s.difference(orf))
for i in range(len(out)): print(out[i])
