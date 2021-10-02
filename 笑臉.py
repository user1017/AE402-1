# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 22:08:18 2021

@author: Derek
"""

import pygame


black = (0,0,0)

white = (255,255,255)

pink = (255,192,203)

yellow = (255,255,0)

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

    pygame.draw.circle(screen,yellow,(350,250),150)
    pygame.draw.circle(screen,black,(300,220),20)
    pygame.draw.circle(screen,black,(400,220),20)
    pygame.draw.arc(screen,black,(290,320,100,20)130,230,10)

    pygame.display.flip()
    clock.tick(100)
    
pygame.quit()