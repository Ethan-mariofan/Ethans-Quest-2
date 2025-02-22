import pygame
import os
from constants import *



image1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/player/spark.png"))
image2 = pygame.image.load(os.path.join(GAME_PATH, "sprites/player/spark2.png"))

class Spark:
    def __init__(self, pos):
        self.pos = pos
        
        self.imgs = []
        self.rect_size = (128, 128)
        
        
        for i in range(10): 
            self.imgs.append(image1)
        for i in range(10):
            self.imgs.append(image2)
        
        self.img_val = 0
        
        self.dir = 1
        
    def draw(self):
        self.img_val += 1
        if self.img_val >= len(self.imgs):
            self.img_val = 0  
        if self.dir == 1:
            image = pygame.transform.flip(self.imgs[self.img_val], False, False)
 
        if self.dir == -1: 
            image = pygame.transform.flip(self.imgs[self.img_val].copy(), True, False)
            
            
        return image
    
    def update(self, tile_rect, update_rect, updated_player_rect, player):  
        
        if player.dir == 1:
            self.pos = pygame.Vector2(player.pos.x - 120, player.pos.y - 30)
            self.dir = 1
            
        elif player.dir == -1:
            self.pos = pygame.Vector2(player.pos.x + 128 + 120, player.pos.y - 30) 
            self.dir = -1