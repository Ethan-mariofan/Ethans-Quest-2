import pygame
import os
from constants import *


flow1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/lava/lava_1.png"))
flow2 = pygame.image.load(os.path.join(GAME_PATH, "sprites/lava/lava_2.png"))
flow3 = pygame.image.load(os.path.join(GAME_PATH, "sprites/lava/lava_3.png"))


fall1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/lava/fall_1.png"))
fall2 = pygame.image.load(os.path.join(GAME_PATH, "sprites/lava/fall_2.png"))
fall3 = pygame.image.load(os.path.join(GAME_PATH, "sprites/lava/fall_3.png"))

class LavaFall:
    def __init__(self, pos):
        self.pos = pos
        self.imgs = []
        self.rect_size = (256, 1000)
        
        for i in range(10):
            self.imgs.append(fall1)
        for i in range(10):
            self.imgs.append(fall2)
        for i in range(10):
            self.imgs.append(fall3)
        self.img_val = 0
        
    def draw(self):
        self.img_val += 1
        if self.img_val >= len(self.imgs):
            self.img_val = 0 
        return self.imgs[self.img_val] 

    def update(self, tile_rect, update_rect, updated_player_rect, player):
        pass
        
class LavaFlow:
    def __init__(self, pos):
        self.pos = pos
        self.imgs = []
        self.rect_size = (1000, 60)
        
        for i in range(10):
            self.imgs.append(flow1)
        for i in range(10):
            self.imgs.append(flow2)
        for i in range(10):
            self.imgs.append(flow3)
        self.img_val = 0 
        
    def draw(self):
        self.img_val += 1
        if self.img_val >= len(self.imgs):
            self.img_val = 0 
        return self.imgs[self.img_val] 
   
        
    def update(self, tile_rect, update_rect, updated_player_rect, player):
        self.pos = pygame.Vector2(CAMERA_POSITION.x - 500, 1000 - 100)
        
        if updated_player_rect.colliderect(update_rect) and player.invincible == False:
            player.health -= 3 #die in lava
          