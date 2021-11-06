# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 10:58:56 2021

@author: Derek
"""

import pygame,random

black = (0,0,0)

white = (255,255,255)

red = (255,0,0)



class Block(pygame.sprite.Sprite): #BLOCK類別:繼承自Sprite類別
    
    def __init__(self,color,width,height): #建構式 當物件產生時 呼叫建構式 傳入參數(顏色,block的長,寬)
        
        super().__init__()  #呼叫父類別的建構式-Sprite類別
        
        self.image = pygame.Surface([width,height])
        self.image.fill(color)  
        
        
        self.rect = self.image.get_rect()  #抓出image的rect物件,設定給block的屬性rect
                                           #rect.width and high就是傳入建構式的長度和高度
                                           #rect.x rect.y = 0 ,會依照情況改變
                                           
        

pygame.init()


screen_width = 700
screen_height = 400


screen=pygame.display.set_mode([screen_width,screen_height])
pygame.display.set_caption("我的遊戲")


block_list = pygame.sprite.Group()
#建立一個角色群組(group)
#將城市中的每一個block 加到group裡 except太空船

all_sprite_list = pygame.sprite.Group()
#建立一個角色群組(group)
#將城市中的每一個block 加到group裡 include太空船

for i in range(50):
    block = Block(black,20,15)
    
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
    
    all_sprite_list.add(block)
    
    
player = Block(red,20,15)
all_sprite_list.add(player)




done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    screen.fill(white)
            
    all_sprite_list.draw(screen)
            
            
            
            
            
            
            
            
    
    pygame.display.flip()
    clock.tick(60)       
pygame.quit()

