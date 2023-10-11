# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 21:23:34 2023

@author: maste
"""
n = int(input())
if (n % 100) in [0, 10, 11, 12, 13, 14]: print (str(n) + ' программистов')
elif (n % 10) in [2, 3, 4]: print(str(n) + ' программиста')
elif (n % 10) in [1]: print(str(n) + ' программист')
elif ( n%10 ) in [0, 5, 6, 7, 8, 9]: print (str(n) + ' программистов')
else: print (str(n) + ' программистов')  