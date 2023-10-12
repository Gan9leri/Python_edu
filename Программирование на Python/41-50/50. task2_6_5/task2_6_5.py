# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 14:59:43 2023

@author: maste
"""
n = int(input())
tab = [[0 for j in range(n)] for i in range(n)]
iBeg = 0 #начало строки
iEnd = 0 #конец строки
jBeg = 0 #начало столбца
jEnd = 0 #конец столбца
k = 1 #значение ячейки
i = 0 # индекс строки
j = 0 #индекс столбца

while k <= n*n :
    tab[i][j] = k
    if (i == iBeg) and (j < n - jEnd - 1) : j = j + 1 #вправо
    elif (j == n - jEnd - 1) and (i < n - iEnd - 1) : i = i + 1 #вниз
    elif (j > jBeg) and (i == n - iEnd - 1) : j = j - 1 #влево
    else : i = i - 1 #вверх
    
    if(i == iBeg + 1) and (j == jBeg): #смещаемся на строчку вниз и на стобец влево для нового витка спирали
        iBeg = iBeg + 1
        iEnd = iEnd + 1
        jBeg = jBeg + 1
        jEnd = jEnd + 1
    
    k = k + 1

for i in range(n):
    for j in range(n):
        print(tab[i][j], end = ' ')
    print()