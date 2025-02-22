import pygame
import os
from constants import *
# from main import cooldown

layout = pygame.image.load(os.path.join(GAME_PATH, "sprites/menus/pause/layout.png"))  
buttons = pygame.image.load(os.path.join(GAME_PATH, "sprites/menus/pause/buttons.png"))  



class PauseMenu:
    def __init__(self, screen, is_paused, image, goto):
        self.layout_img = layout
        self.buttons_img = image
                
        self.is_paused = is_paused
        self.screen = screen
         
        self.layout_x_pos = -1000
        self.goto = goto
        self.a = False

        
    def draw(self):
        #animation with movement
        if self.is_paused:
            self.layout_x_pos += 3
            if self.layout_x_pos >= 0:
                self.layout_x_pos = 0
        else:
            self.layout_x_pos -= 3
            if self.layout_x_pos <= -1000:
                self.layout_x_pos = -1000     
        
        self.screen.blit(self.layout_img, (self.layout_x_pos, 0)) #layout
        self.screen.blit(self.buttons_img, (self.layout_x_pos, 0)) #button
    
    def update(self): #if this is true aka return true then switch game_state to map
        pass
        #continue_rect = pygame.rect.Rect(31, 234, 259, 90)
        #
        #return_to_map_rect = pygame.rect.Rect(34, 455, 259, 204)
        #
        #
        #pos = pygame.mouse.get_pos()
        #pressed1 = pygame.mouse.get_pressed()[0]
        # 
        #
        #if self.layout_x_pos >= 0 and self.is_paused == True:
        #    if continue_rect.collidepoint(pos) and pressed1:
        #        self.is_paused = False #unpause
        #    
        #    if return_to_map_rect.collidepoint(pos) and pressed1 and cooldown >= 2:
#
        #        
        #        print(self.goto,' with ',cooldown)
        #        
        #        return self.goto   
        #
        #    # if cooldown < 2:
        #    #     return self.goto
        #    
            
                
            
        
        #keys = pygame.key.get_pressed()
        #
        #if keys[KEY_X]:
        #    self.is_paused = True      
        #    
        #
        #return False
            