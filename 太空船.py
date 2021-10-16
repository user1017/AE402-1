# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 11:20:23 2021

@author: Derek
"""
import pygame

black = (0,0,0)

white = (255,255,255)

pygame.init()


size = (800,600)

screen=pygame.display.set_mode(size)
pygame.display.set_caption("我的遊戲")

done = False
clock = pygame.time.Clock()


click_sound = pygame.mixer.Sound("laser5.ogg")


background_image = pygame.image.load("saturn_family1.jpg").convert()
player_image = pygame.image.load("playerShip1_orange.png").convert()
player_image.set_colorkey(black)#去背


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()
            
            
            
    screen.blit(background_image,(0,0))
    player_pos = pygame.mouse.get_pos()
    x = player_pos[0]#第一個數字
    y = player_pos[1]
    
    screen.blit(player_image,(x,y))
    
    
    pygame.display.flip()
    clock.tick(60)       
pygame.quit()
