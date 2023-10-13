# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 15:35:46 2023

@author: maste
"""
#Инициализация словарей с ростом и количеством учеников
height, amount = {}, {}
for i in range(1, 12):
    height[i] = 0
    amount[i] = 0
    
#наполнение словарей данными из файла
with open('data.txt', 'r', encoding = 'utf8' ) as file:
    while True:
        s = file.readline().split()
        if not s : break
        else: 
            key = int(s[0])
            val = int(height.get(key))
            val = val + int(s[2])
            height[key] = val     
            if int(s[2]) != 0 :
                val1 = int(amount.get(key))
                val1 = val1 + 1
                amount[key] = val1

#Подсчет среднего роста и запись данных в файл
out = open('out.txt', 'w')

avg = 0.0
for i in range(1, 12):
    h = height.get(i)
    a = amount.get(i)
    if a != 0 :
        avg = h/a
        print(i, avg)
        out.write(str(i) + ' ' + str(avg) + '\n')
    elif a == 0 : 
        print(i, '-')
        out.write(str(i) + ' ' + '-' + '\n')
out.close()

