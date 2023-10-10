# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 18:55:19 2023

@author: maste
"""

#Создание команд в словаре
def init_team(name):
    if name not in teams:
        teams[name] = []
        teams[name].append(0)
        teams[name].append(0)
        teams[name].append(0)
        teams[name].append(0)
        teams[name].append(0)

#Подсчет проведенных игр команды
def games(name):
    val = teams.get(str(name))
    val[0] = int(val[0]) + 1
    teams[name] = val
    
#Подсчет побед команды
def victory(s):
    a = int(s[1])
    b = int(s[3])
    if (a > b):
        name = str(s[0])
        val = teams.get(name)
        val[1] = val[1] + 1
        val[4] = val[4] + 3
        teams[name] = val
                
    elif (b > a):
        name = str(s[2])
        val = teams.get(name)
        val[1] = val[1] + 1
        val[4] = val[4] + 3
        teams[name] = val
        
#Подсчет ничьих команды        
def draw(s):
    a = int(s[1])
    b = int(s[3])
    if (a == b):
        name = str(s[0])
        val = teams.get(name)
        val[2] = val[2] + 1
        val[4] = val[4] + 1
        teams[name] = val
                    
        name1 = str(s[2])
        val1 = teams.get(name1)
        val1[2] = val1[2] + 1
        val1[4] = val1[4] + 1
        teams[name1] = val1
 
#Подсчет поражений команды
def lose(s):
    a = int(s[1])
    b = int(s[3])
    
    if (a < b):
        name = str(s[0])
        val = teams.get(name)
        val[3] = val[3] + 1
        teams[name] = val
        
    elif(b < a):
        name = str(s[2])
        val = teams.get(name)
        val[3] = val[3] + 1
        teams[name] = val        

#Вывод словаря
def print_teams(teams):
    res = ''
    for key,value in teams.items():
        s = teams.get(key)
        s = str(s)
        for i in range(1, len(s)-1):
            if(s[i] != ','):
                res = res + s[i]
        print(key + ':' + res)
        res = ''
        
        
    
n = int(input())
teams = {}
i = 0
while i < n :
    s = input().split(';')
    
    init_team(s[0])        
    init_team(s[2])
    games(s[0])
    games(s[2])
    victory(s)
    draw(s)
    lose(s)
        
    i = i + 1

print_teams(teams)

