# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 10:55:11 2021

@author: Derek
"""
class Human():     #class 創造類別

    def __init__ (self,name,weight,height):     #init物件初始化
        
        self.name = name
        self.weight = weight
        self.height = height
        
        
        
    def bmi(self):
        return self.weight/ ((self.height/100)**2)
    
    
class Woman(Human):
    
    def __init__ (self,name,weight,height,bust,waist,hip):
        super().__init__(name,weight,height)
        
        
        self.bust = bust
        self.waist = waist
        self.hip = hip
        
    def printBWH(self):
        print(" bust = {}, waist = {}, hip = {} ".format(self.bust, self.waist, self.hip))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        