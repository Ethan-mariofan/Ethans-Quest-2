import pygame
import os
from constants import *



class Faller:
    def __init__(self, pos):
        self.pos = pos
        self.type = type
        
        
        self.img = pygame.image.load(os.path.join(GAME_PATH, "sprites/objs/faller/1.png"))
        


        self.rect_size = (128, 256)
          
    def draw(self):
        return self.img
        
    def update(self, tile_rect, update_rect, updated_player_rect, player):

        keys = pygame.key.get_pressed()
        new = pygame.Rect(updated_player_rect.x, updated_player_rect.y, updated_player_rect.width, updated_player_rect.height + 30)
            
            
        if new.colliderect(update_rect):

            self.pos.y += 1 #move down (fall)

            player.force = 0  
            player.pos.y += player.force * -1 
            
            self.cool_down += 1
            if i >= 1:
                blah = controller.get_button(1)
            else:
                blah = keys[KEY_JUMP]
            if blah:
                if self.cool_down >= 5 and not player.completed_level: 
                    player.force = -16
                    player.pos.y -= 20  
    
                    pygame.mixer.Sound.play(PLAYER_JUMP_SND)
        else: 
            self.cool_down = 0
        