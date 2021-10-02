# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 22:35:25 2021

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

    pygame.draw.arc(screen,pink,(100,100),20,270,2)

    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()