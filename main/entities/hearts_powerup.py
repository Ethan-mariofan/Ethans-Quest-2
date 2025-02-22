import pygame
import os
from constants import *

hearts = pygame.image.load(os.path.join(GAME_PATH, "sprites/items/hearts/heart.png"))
#this will be finished soon   


class Heart:
    def __init__(self, pos):
        self.pos = pos
        self.imgs = []
        self.rect_size = (128, 128)

        for i in range(1): 
            self.imgs.append(hearts)


        self.img_val = 0 

    def draw(self):
        self.img_val += 1
        if self.img_val >= len(self.imgs):
            self.img_val = 0 
        return self.imgs[self.img_val]
    
    def update(self, x, update_rect, updated_player_rect, player):
        if updated_player_rect.colliderect(update_rect):
            
            if player.health < 3:
                player.health += 1
           
            
            pygame.mixer.Sound.play(POWER_UP_SND)
            return True
        return False 

