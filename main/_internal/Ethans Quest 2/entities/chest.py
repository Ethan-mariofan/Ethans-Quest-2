import pygame
import os

from constants import *

class Chest:
    def __init__(self, pos, cutscene):
        self.pos = pos
        
        self.cutscene = cutscene
        
        self.rect_size = (128, 128) 
        
        self.img = []
        self.img.append(pygame.image.load(os.path.join(GAME_PATH, "sprites/objs/chest/1.png")))
        self.img.append(pygame.image.load(os.path.join(GAME_PATH, "sprites/objs/chest/2.png")))
          
        self.is_opened = False
        self.img_val = 0
    
    def draw(self):
        if self.is_opened:
            self.img_val = 1
        else:
            self.img_val = 0
        return self.img[self.img_val]
    
    def update(self, tile_rect, update_rect, updated_player_rect, player):
        pass
             
