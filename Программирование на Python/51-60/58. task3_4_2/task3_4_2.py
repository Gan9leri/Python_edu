# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 17:03:41 2023

@author: maste
"""

with open('file.txt', 'r') as inf:
    s = inf.read().split()
#print(s)
my_dict = {}
out = []
sort = []
for i in range(len(s)): s[i] = s[i].lower()
#print(s)
for i in range(len(s)):
    if s[i] not in my_dict:
        my_dict[s[i]] = 1
        #print(my_dict)
    elif s[i] in my_dict:
        k = my_dict.get(s[i])
        k = int(k)
        k = k + 1
        my_dict[s[i]] = k
        #print(k)
#print(my_dict)
for key in my_dict:
    k = int(my_dict[key])
    if k == max(my_dict.values()):
        key = str(key)
        print(key)
        print(my_dict[key])
        out.append(key)
#print(out)
#if len(out) > 1 :
#    print(min(out))
#else: print(out)

        
                



    