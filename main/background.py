import pygame

import os
from constants import * 

class Background:
    def __init__(self, img, speed, x):  
        self.img = img
        self.speed = speed

        self.pos = pygame.Vector2(x, 0)


    def draw(self, screen):
        screen.blit(self.img, self.pos)

    def move(self, player):
        self.pos.x -= player.speed_x * self.speed
        if self.pos.x >= 1700:
            self.pos.x = -1000
        elif self.pos.x <= -1700:
            self.pos.x = 1000
  
    def update(self, screen, player):
        self.draw(screen)
        self.move(player) 