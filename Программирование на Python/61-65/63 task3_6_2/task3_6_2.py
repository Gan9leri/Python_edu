# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 15:44:36 2023

@author: maste
"""

import requests
s = requests.get('https://stepik.org/media/attachments/course67/3.6.3/699991.txt')


while True:
    if s.text.startswith('We'): break
    else:
        s = requests.get('https://stepik.org/media/attachments/course67/3.6.3/' + s.text)
        print(s.text)

print(s.text)
        
