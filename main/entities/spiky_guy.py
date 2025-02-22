import pygame
import os
from constants import *

from important import *


image1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/enemies/spiky_guy/1.png"))
image2 = pygame.image.load(os.path.join(GAME_PATH, "sprites/enemies/spiky_guy/2.png"))
image3 = pygame.image.load(os.path.join(GAME_PATH, "sprites/enemies/spiky_guy/3.png"))
image4 = pygame.image.load(os.path.join(GAME_PATH, "sprites/enemies/spiky_guy/4.png"))

class SpikyGuy:
    def __init__(self, pos):
        self.pos = pos
        self.imgs = []
        self.rect_size = (128, 128)
        
        for i in range(10): 
            self.imgs.append(image1)
        for i in range(10):
            self.imgs.append(image2)
        for i in range(10): 
            self.imgs.append(image3)
        for i in range(10):
            self.imgs.append(image4)
            
        self.dead = False
        self.img_val = 0
        
        self.timer = 0
        self.timer2 = 0
        
    def draw(self):
        self.img_val += 1
        if self.img_val >= len(self.imgs):
            self.img_val = 0 
        return self.imgs[self.img_val] 

    def update(self, tile_rect, update_rect, updated_player_rect, player):

        if update_rect.colliderect(updated_player_rect) and player.invincible == False and self.dead == False:
            player.health -= 1
            player.invincible = True
            
            
        #starts at -1 
        if self.timer >= 60:
            self.pos.y += 1
            if self.timer2 >= 60:
                self.timer = 0
                self.timer2 = 0  
            self.timer2 += 1
        else:
            self.pos.y -= 1
        self.timer += 1