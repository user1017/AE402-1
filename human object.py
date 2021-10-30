# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 11:44:28 2021

@author: Derek
"""

import 人類


a = 人類.Human("derek",58,177)

print(a.name,"bmi:",a.bmi())



b = 人類.Woman("findy",48,165,70,50,55)

print(b.name,"bmi:",b.bmi())
b.printBWH()

    
    