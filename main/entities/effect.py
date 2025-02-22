import pygame

import os
import random

from constants import *


class Effect:
    def __init__(self, screen, img):
        self.img = img
        self.screen = screen
        
     
        self.pos = pygame.Vector2(0, -400)
         
        
    def draw(self):
       #pos = pygame.Vector2(random.randint(0, 0), random.randint(0, 0))
        
        self.pos.y += 1 
        if self.pos.y >= 40:
            self.pos.y = -400
        
        self.screen.blit(self.img, (self.pos.x, self.pos.y))    
        