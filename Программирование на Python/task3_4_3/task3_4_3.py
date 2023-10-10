# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 12:10:43 2023

@author: maste
"""
#Считывание из файла
with open('file.txt', 'r', encoding = 'utf8') as file:
   inf = file.read().split()
#print(inf)

#Формирование словаря с оценками по студентам
mag = {}
for i in range(len(inf)):
    s = inf[i].split(';')
    for j in range(len(s)):
        if s[j].isalpha() : 
            key = s[j]
            mag[key] = []
        elif s[j].isdigit() :
            mag[key].append(s[j])
#print(mag)

#Формирование словаря с оценками по предметам
flag = 0
sub_mag = {}
key = 'rus'
sub_mag[key] = []
key = 'math'
sub_mag[key] = []
key = 'fis'
sub_mag[key] = []
for i in range(len(inf)):
    s = inf[i].split(';')
    for j in range(len(s)):
        if s[j].isalpha():
            flag = 1
        elif s[j].isdigit() and flag == 1:
            flag = flag + 1
            sub_mag['rus'].append(s[j])
        elif s[j].isdigit() and flag == 2:
            flag = flag + 1
            sub_mag['math'].append(s[j])
        elif s[j].isdigit() and flag == 3:
            flag = 0
            sub_mag['fis'].append(s[j])
#print(sub_mag)

#Расчет среднего арифметического и запись в файл
out = open('out.txt', 'w')
avg = [] 
for key in mag:
    a,b,c = mag.get(key)
    avg.append((int(a) + int(b) + int(c))/3)
for i in range(len(avg)):
    avg[i] = str(avg[i])
    out.write(avg[i] + '\n')

#Расчет средней оценки по предметам по всем абитуриентам и запись в файл
summ = 0
count = 0
s = []
for key in sub_mag:
    s = sub_mag.get(key)
    for j in range(len(s)):
        summ = summ + int(s[j])
        count = count + 1
    sub_avg = summ/count
    sub_avg = str(sub_avg)
    out.write(sub_avg + ' ')
    summ = 0
    count = 0
    
out.close()
