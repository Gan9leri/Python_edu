# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 12:32:00 2023

@author: Овсянников Александр
"""
class Human():
    
    defoult_name = 'Jack'
    defoult_age = 30
    
    def __init__(self, name = defoult_name, age = defoult_age):
               
        self.name = name
        self.age = age   
        
        self.__money = 0
        self.__house = 0
        
    def info(self):
        print('name - ', self.name)
        print('age - ', self.age)
        print('house - ', self.__house)
        print('money - ', self.__money)
    
    @staticmethod
    def default_info():
        print('defoult_name -', Human().defoult_name)
        print('defoult_age -', Human().defoult_age)
        
    def ___make_deal(self, House, money):
        self.__house = House
        self.__money -= money
        
    def earn_money(self):
        self.__money += 5000
        
    def buy_house(self, House, discount):
        if self.__money < House.final_price(discount) : print('Недостаточно средств')
        else: self.___make_deal(House, House.final_price(discount))
        
class House():
    
    def __init__(self, area, price):
        self._area = area
        self._price = price
    
    def final_price(self, discount):
        return self._price - discount
    
class SmallHouse(House):
    
    def __init__(self, area, price):
        super().__init__(area, price)
        self._area = 40
        self._price = price


        

        
        

    
    
        
        
        
        
        
    