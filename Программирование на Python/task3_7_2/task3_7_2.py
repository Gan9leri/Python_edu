# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 18:09:18 2023

@author: maste
"""

def init_chiper(s1, s2):
    for i in range(len(s1)):
        cip[s1[i]] = []
        cip[s1[i]].append(s2[i])
        
    for i in range(len(s2)):
        decip[s2[i]] = []
        decip[s2[i]].append(s1[i])
 
def incrypt(s3):
    res = ''
    for i in range(len(s3)):
        val = str(cip.get(s3[i]))
        res = res + val
        val = ''
    print_res(res)
 
def decipher(s4):
    res = ''
    for i in range(len(s4)):
        val = str(decip.get(s4[i]))
        res = res + val
        val = ''
    print_res(res)        

def print_res(result):
    s = ''
    sym = ['[', ']', "'"]
    for i in range(len(result)):
        if result[i] not in sym:
            s = s + str(result[i])
    print(s)
            
s1 = str(input())
s2 = str(input())
s3 = str(input())
s4 = str(input())

cip = {}
decip = {}
init_chiper(s1,s2)

incrypt(s3)
decipher(s4)
