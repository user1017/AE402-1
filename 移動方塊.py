# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 10:43:59 2021

@author: Derek
"""

import pygame

black = (0,0,0)

white = (255,255,255)

yellow = (255,255,0)

red = (255,0,0)

pygame.init()


size = (700,500)

screen=pygame.display.set_mode(size)
pygame.display.set_caption("移動方塊")

done = False
clock = pygame.time.Clock()

x = 0
y = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    keys = pygame.key.get_pressed()    
    
    if keys[pygame.K_LEFT]:
        x-=1
    elif keys[pygame.K_RIGHT]:
        x+=1
    elif keys[pygame.K_UP]:
        y-=1
    elif keys[pygame.K_DOWN]:
        y+=1
        
    else:
        pass
    
            
    screen.fill(black)
    pygame.draw.rect(screen,white,(x+10,y+10,10,10))



    pygame.display.flip()
    clock.tick(240)       
pygame.quit()