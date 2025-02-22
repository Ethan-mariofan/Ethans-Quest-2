import pygame
import os
from constants import *



class Platform:
    def __init__(self, pos, type, img):
        self.pos = pos
        self.type = type
        
        
        self.img = img
        img_plat = pygame.image.load(os.path.join(GAME_PATH, self.img))
        
    
        self.imgs = []

        for i in range(1): 
            self.imgs.append(img_plat)


        self.rect_size = (256, 128)
        self.img_val = 0
        
        
        
        self.timer = 0
        self.timer2 = 0
        self.cool_down = 0
        
        
    def draw(self):
        self.img_val += 1
        if self.img_val >= len(self.imgs):
            self.img_val = 0 
        return self.imgs[self.img_val]  
    
    def update(self, tile_rect, update_rect, updated_player_rect, player):
        #update_rect.x = 256
        if self.type == "bounce":
            if updated_player_rect.colliderect(update_rect):
                #self.pos.y += 2 

                player.pos.y += player.force * -1
                player.force = 0
                player.cool_down += 1
            
                player.force = -16
                player.pos.y -= 10    
        
        if self.type == "horizontal":
            if self.timer >= 60:
                self.pos.x += 1 
                if self.timer2 >= 60:
                    self.timer = 0
                    self.timer2 = 0  
                self.timer2 += 1
            else:
                self.pos.x -= 1
            self.timer += 1
            keys = pygame.key.get_pressed()
            
            
            new = pygame.Rect(updated_player_rect.x, updated_player_rect.y, updated_player_rect.width, updated_player_rect.height + 30)
            
            
            if new.colliderect(update_rect):
                player.force = 0
                player.pos.y += player.force * -1 
                
                self.cool_down += 1
                
                if i >= 1:
                    blah = controller.get_button(1)
                else:
                    blah = keys[KEY_JUMP]
                if blah:
                    if self.cool_down >= 10 and not player.completed_level: 
                        player.force = -16
                        player.pos.y -= 20  
    
                        pygame.mixer.Sound.play(PLAYER_JUMP_SND)
            else: 
                self.cool_down = 0