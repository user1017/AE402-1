# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 11:40:19 2021

@author: Derek
"""

import pygame
import random

snow_list=[]
for i in range(50):

    x = random.randrange(0,400)
    y = random.randrange(0,400)
    snow_list.append([x,y])
    


black = (0,0,0)

white = (255,255,255)

pink = (255,192,203)

pygame.init()


size = (400,400)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("我的遊戲")

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    screen.fill(black)
    
    for i in range(len(snow_list)):
        
        pygame.draw.circle(screen,white,(snow_list[i]),2)
        snow_list[i][1]+=1
        
        if  snow_list[i][1]>400:
            y = random.randrange(-50,-10)
            snow_list[i][1]=y
            x = random.randrange(0,400)
            snow_list[i][0]=x

    pygame.display.flip()
    
    clock.tick(120)
    
pygame.quit()
