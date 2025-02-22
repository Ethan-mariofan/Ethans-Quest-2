import pygame
import os
from constants import *

coin1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/items/coins/1.png"))
coin2 = pygame.image.load(os.path.join(GAME_PATH, "sprites/items/coins/2.png"))
coin3 = pygame.image.load(os.path.join(GAME_PATH, "sprites/items/coins/3.png"))
coin4 = pygame.image.load(os.path.join(GAME_PATH, "sprites/items/coins/4.png"))
coin5 = pygame.image.load(os.path.join(GAME_PATH, "sprites/items/coins/5.png"))

 
class Coin:
    def __init__(self, pos):
        self.pos = pos
        self.rect_size = pygame.Vector2(128, 128)

        self.imgs = []
        self.img_val = 0

        for i in range(10):
            self.imgs.append(coin1)
        for i in range(10):
            self.imgs.append(coin2)
        for i in range(10):
            self.imgs.append(coin3)
        for i in range(10):
            self.imgs.append(coin4)
        for i in range(10):
            self.imgs.append(coin5)


    def draw(self):
        self.img_val += 1
        if self.img_val >= len(self.imgs):
            self.img_val = 0 
        return self.imgs[self.img_val]
    
    def update(self, x, update_rect, updated_player_rect, player):
        if updated_player_rect.colliderect(update_rect):
            player.coins += 1
            pygame.mixer.Sound.play(COIN_SND)
            return True
        return False 