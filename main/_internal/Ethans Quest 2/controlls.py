import pygame

from enum import Enum

import os
from constants import *


import constants

class ControllerTypes(Enum):
    keyboard = "Keyboard"
    controller = "Controller"



class ControllsMenu: 
    def __init__(self, screen):
        self.screen = screen
        self.img = pygame.image.load(os.path.join(GAME_PATH, "sprites/menus/controlls/bg.png"))

        self.type = ControllerTypes.keyboard #default

        self.key_rect = pygame.Rect(23, 378, 377 - 52, 542 - 377)
        self.controller_rect = pygame.Rect(575, 375, 377 - 52, 542 - 377)
 

    
    def update(self):
        self.screen.blit(self.img, (0, 0))   
        posmouse = pygame.mouse.get_pos()
        pressed1 = pygame.mouse.get_pressed()[0]

        if self.key_rect.collidepoint(posmouse) and pressed1:
            self.type = ControllerTypes.keyboard
           

        if self.controller_rect.collidepoint(posmouse) and pressed1:
            self.type = ControllerTypes.controller
         
            
 
        keys = pygame.key.get_pressed()

        if keys[KEY_X]:
            return True
        
        return False