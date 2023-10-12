# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 14:54:10 2023

@author: maste
"""
mat = []
while True :
    s = input()
    if s == 'end' : break
    mat.append([int(i) for i in s.split()])
n = len(mat)
k = len(mat[0])
out = [[0 for j in range(k)] for i in range(n)]
for i in range(n):
    for j in range(k):
        out[i][j] = mat[i-1][j] + mat[(i+1)%n][j] + mat[i][j-1] + mat[i][(j+1)%k]
for i in range(n):
    for j in range(k):
        print(out[i][j], end = ' ')
       
    print()