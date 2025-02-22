import pygame
import os
from constants import *
from important import *


star1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/objs/star/1.png"))
star2 = pygame.image.load(os.path.join(GAME_PATH, "sprites/objs/star/2.png"))
star3 = pygame.image.load(os.path.join(GAME_PATH, "sprites/objs/star/3.png"))
star4 = pygame.image.load(os.path.join(GAME_PATH, "sprites/objs/star/4.png"))

class StarEndLevel:
    def __init__(self, pos, level_number_global):
        self.pos = pos
        self.lvl = level_number_global
        self.rect_size = pygame.Vector2(128, 128)

        self.imgs = []
        self.img_val = 0

        for i in range(10):
            self.imgs.append(star1)
        for i in range(10):
            self.imgs.append(star2)
        for i in range(10):
            self.imgs.append(star3)
        for i in range(10):
            self.imgs.append(star4)
 
    
    def draw(self):
        self.img_val += 1
        if self.img_val >= len(self.imgs):
            self.img_val = 0 
        return self.imgs[self.img_val]
    
    def update(self, x, update_rect, updated_player_rect, player):
        if updated_player_rect.colliderect(update_rect):
            pygame.mixer.Sound.play(GOT_STAR_SND)  

            player.completed_level = True
            

            return True
        return False  

