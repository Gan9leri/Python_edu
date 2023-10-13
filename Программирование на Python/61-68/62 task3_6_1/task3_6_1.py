# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 13:01:22 2023

@author: maste
"""

import requests
file = requests.get('https://stepik.org/media/attachments/course67/3.6.2/121.txt')
print(file.text)
s = (file.text).splitlines()
print(s)
print(len(s))
out = open('out.txt', 'w')
out.write(str(len(s)))
out.close()

 