import pygame
import os
from constants import *
from important import *
from music_manager import *

logo = pygame.image.load(os.path.join(GAME_PATH, "title_logo.png"))
button_img = pygame.image.load(os.path.join(GAME_PATH, "sprites/menus/title/button.png"))

bg = pygame.image.load(os.path.join(GAME_PATH, "sprites/menus/title/bg.png"))

class TitleScreen:
    def __init__(self, screen, track):
        self.track = track
 
        self.mscmgr = MusicManager(self.track, True)  
        self.mscmgr.play()   

        self.logo = logo
        self.button_img = button_img
        self.bg = bg
        self.screen = screen
 
        self.logo_pos = pygame.Vector2(250, 0)

        self.button_pos = pygame.Vector2(250, 800)
        self.button_rect = pygame.Rect(self.button_pos.x, self.button_pos.y, 500, 200)
         
  
    def draw(self):
        self.screen.blit(self.bg, (0, 0))   

        self.screen.blit(self.logo, (self.logo_pos.x, self.logo_pos.y))   
        self.screen.blit(self.button_img, (self.button_pos.x, self.button_pos.y))

    def movement_logo(self):
        self.logo_pos.y += 1
            
        if self.logo_pos.y >= 50:
            self.logo_pos.y = 50


    def button(self): #if its true then switch the scene   
        pos = pygame.mouse.get_pos()
        pressed1 = pygame.mouse.get_pressed()[0]

        if self.button_rect.collidepoint(pos) and pressed1:
            self.mscmgr.stop()
            return True
        return False
    

    def update(self):
        self.movement_logo()
        self.draw()

        self.button()
        return False

        
        
            
        
        
        

