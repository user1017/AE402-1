# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 11:43:58 2021

@author: Derek
"""

import pygame,random

black = (0,0,0)

white = (255,255,255)

pygame.init()

def randcolour():
    r = random.randrange(0,255)
    g = random.randrange(0,255)
    b = random.randrange(0,255)
    return(r,g,b)

size = (700,500)

screen=pygame.display.set_mode(size)
pygame.display.set_caption("我的遊戲")

done = False
clock = pygame.time.Clock()
count = 0
click = False
pos = (0,0)
limit = 50
colour = randcolour()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            click = True
            count = 0
            colour = randcolour()
            
            
    screen.fill(black)
    if click and count < limit:
        pygame.draw.circle(screen,colour,pos,count)
        count+=1
        if click and count > limit:
            click = False
    
    
    pygame.display.flip()
    clock.tick(60)       
pygame.quit()