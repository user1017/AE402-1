# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 10:45:30 2021

@author: Derek
"""

import pygame

black = (0,0,0)

white = (255,255,255)

pygame.init()


size = (700,500)

screen=pygame.display.set_mode(size)
pygame.display.set_caption("我的遊戲")

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
            screen.fill(white)
    
    pygame.display.flip()
    clock.tick(60)       
pygame.quit()
