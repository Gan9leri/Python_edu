# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 21:56:15 2023

@author: Овсянников Александр
"""
from task2_1 import Human, SmallHouse

Human().default_info()
Jack = Human()
Jack.info()
chalet = SmallHouse(40, 5000)
Jack.buy_house(chalet, 30)
Jack.earn_money()
Jack.buy_house(chalet, 30)
Jack.info()