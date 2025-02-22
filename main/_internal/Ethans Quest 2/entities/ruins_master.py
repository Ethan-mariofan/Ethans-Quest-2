import pygame

import os
from constants import *
from entities.cutscene_manager import *

rm1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/enemies/RuinsMaster/1.png"))
rm2 = pygame.image.load(os.path.join(GAME_PATH, "sprites/enemies/RuinsMaster/2.png"))
rm3 = pygame.image.load(os.path.join(GAME_PATH, "sprites/enemies/RuinsMaster/3.png"))
rm4 = pygame.image.load(os.path.join(GAME_PATH, "sprites/enemies/RuinsMaster/4.png"))
rm5 = pygame.image.load(os.path.join(GAME_PATH, "sprites/enemies/RuinsMaster/5.png"))
rm6 = pygame.image.load(os.path.join(GAME_PATH, "sprites/enemies/RuinsMaster/6.png"))
rm7 = pygame.image.load(os.path.join(GAME_PATH, "sprites/enemies/RuinsMaster/7.png"))
rm8 = pygame.image.load(os.path.join(GAME_PATH, "sprites/enemies/RuinsMaster/8.png"))
rm9 = pygame.image.load(os.path.join(GAME_PATH, "sprites/enemies/RuinsMaster/9.png"))
rm10 = pygame.image.load(os.path.join(GAME_PATH, "sprites/enemies/RuinsMaster/10.png"))
rm11 = pygame.image.load(os.path.join(GAME_PATH, "sprites/enemies/RuinsMaster/11.png"))


class RuinsMaster:
    def __init__(self, pos):
        self.pos = pos
        
        self.imgs = []
        self.rect_size = (339, 398)
        
        
        self.cutscene = None
    
        for i in range(10): 
            self.imgs.append(rm1)
        for i in range(10):
            self.imgs.append(rm2)
        for i in range(10): 
            self.imgs.append(rm3)
        for i in range(10):
            self.imgs.append(rm4)
        for i in range(10): 
            self.imgs.append(rm5)
        for i in range(10):
            self.imgs.append(rm6)
        for i in range(10): 
            self.imgs.append(rm7)
        for i in range(10):
            self.imgs.append(rm8)
        for i in range(10): 
            self.imgs.append(rm9)
        for i in range(10):
            self.imgs.append(rm10)
        for i in range(10):
            self.imgs.append(rm11)
        

        self.img_val = 0  
         
        self.dead = False
    def draw(self):
        self.img_val += 1
        if self.img_val >= len(self.imgs):
            self.img_val = 0 
        return self.imgs[self.img_val] 
        
    def update(self, tile_rect, update_rect, updated_player_rect, player):

        
        if updated_player_rect.colliderect(update_rect) and player.invincible == False and self.dead == False:
            player.health -= 1
            player.invincible = True
 
        self.pos.x += 3
        