import pygame
import os
from constants import *

idle1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/objs/fireball/1.png"))
idle2 = pygame.image.load(os.path.join(GAME_PATH, "sprites/objs/fireball/2.png"))
idle3 = pygame.image.load(os.path.join(GAME_PATH, "sprites/objs/fireball/3.png"))
idle4 = pygame.image.load(os.path.join(GAME_PATH, "sprites/objs/fireball/4.png"))

class FireBall:
    def __init__(self, pos):
        self.pos = pos
        self.rect_size = (128, 128)

        self.imgs = []
        for i in range(10): 
            self.imgs.append(idle1)
        for i in range(10):
            self.imgs.append(idle2)
        for i in range(10): 
            self.imgs.append(idle3)
        for i in range(10):
            self.imgs.append(idle4)

        self.timer = 0
        self.timer2 = 0
        
        self.img_val = 0

    def draw(self):
        self.img_val += 1
        if self.img_val >= len(self.imgs):
            self.img_val = 0 
        return self.imgs[self.img_val] 
    
    def update(self, tile_rect, update_rect, updated_player_rect, player):
        if updated_player_rect.colliderect(update_rect) and player.invincible == False:
            player.health -= 1
            player.invincible = True  

        if self.timer >= 60:
            self.pos.x += 1
            if self.timer2 >= 60:
                self.timer = 0
                self.timer2 = 0
            self.timer2 += 1
        else:
            self.pos.x -= 1
        self.timer += 1
            