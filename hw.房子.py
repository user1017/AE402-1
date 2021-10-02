# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 21:09:40 2021

@author: Derek
"""

import pygame


black = (0,0,0)

white = (255,255,255)

pink = (255,192,203)

pygame.init()


size = (700,500)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("我的遊戲")

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    screen.fill(white)

    pygame.draw.rect(screen,black,(300,200,200,300),10)
    pygame.draw.rect(screen,black,(320,300,50,50),3)
    pygame.draw.rect(screen,black,(430,300,50,50),3)
    pygame.draw.rect(screen,black,(390,440,30,60),3)

    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()