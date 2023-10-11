# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 21:23:34 2023

@author: maste
"""
type = input()
if type == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c)/2
    S = ( p * (p - a) * (p - b) * ( p - c ) ) ** 0.5
    print(S)
elif type == 'прямоугольник':
    a = int(input())
    b = int(input())
    S = a * b
    print(S)
elif type == 'круг':
    r = int(input())
    S = 3.14 * (r ** 2) 
    print(S)