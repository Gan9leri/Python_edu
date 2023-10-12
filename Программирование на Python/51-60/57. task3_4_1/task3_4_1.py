# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 21:39:49 2023

@author: maste
"""
with open ('file.txt', 'r') as inf:
    s = inf.readline()
print(s)
out = '' #выходна строка
sub = '' #подстрока с числом повторений
sub_num = 0 #число повторений
flag = 0 #флаг о том, что накапливается число
element = ''
for i in range(len(s)):
    if s[i].isdigit() :
        if s[i-1].isalpha() : 
            element = s[i-1]
            print(element)
        flag = 1
        sub = sub + s[i]
    if (s[i].isalpha() and flag == 1) or i == len(s) - 1:
        flag = 0
        sub_num = int(sub)
        #print(sub_num)
        sub = ''
        out = out + element * sub_num
        
        sub_num = 0
print(out)
with open ('out.txt', 'w') as inf:
    inf.write(out)
        

        

        
        
