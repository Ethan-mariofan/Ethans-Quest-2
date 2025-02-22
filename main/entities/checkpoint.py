import pygame
import os
from constants import *

check1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/objs/checkpoint/1.png"))
check2 = pygame.image.load(os.path.join(GAME_PATH, "sprites/objs/checkpoint/2.png"))
check3 = pygame.image.load(os.path.join(GAME_PATH, "sprites/objs/checkpoint/3.png"))

class CheckPoint:
    def __init__(self, pos):
        self.pos = pos
        self.start_pos = pos
        self.rect_size = pygame.Vector2(128, 128)

        self.imgs = []
        self.img_val = 0

        for i in range(10):
            self.imgs.append(check1)
        for i in range(10):
            self.imgs.append(check2)
        for i in range(10):
            self.imgs.append(check3)



    def draw(self):
        self.img_val += 1
        if self.img_val >= len(self.imgs):
            self.img_val = 0 
        return self.imgs[self.img_val]
    
    def update(self, x, update_rect, updated_player_rect, player):
        if updated_player_rect.colliderect(update_rect) and player.checkpoint_gotton == False:
            
            pygame.mixer.Sound.play(POWER_UP_SND)
            player.checkpoint_pos = pygame.Vector2(update_rect.x, update_rect.y)
            player.checkpoint_gotton = True 
            player.checkpoint_start_pos = self.start_pos
            
        return False 