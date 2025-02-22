import pygame
import os
from constants import *


walk1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/enemies/bumpy/1.png"))
walk2 = pygame.image.load(os.path.join(GAME_PATH, "sprites/enemies/bumpy/2.png"))
dead = pygame.image.load(os.path.join(GAME_PATH, "sprites/enemies/bumpy/dead.png"))
 
class Bumpy:
    def __init__(self, pos):
        self.pos = pos
       
        self.rect_size = (128, 128)

        self.imgs = []
        for i in range(10): 
            self.imgs.append(walk1)
        for i in range(10):
            self.imgs.append(walk2)

        self.img_val = 0

        self.direction = -1
        self.force = 0
        self.dead = False
        self.dead_timer = 0


    def draw(self):
        self.img_val += 1
        if self.img_val >= len(self.imgs):
            self.img_val = 0 
        return self.imgs[self.img_val] 

    def switch_imgs(self, type):
        self.imgs.clear() 
        if type == "die":
            for i in range(10): 
                self.imgs.append(dead)


    def movement(self, tile_rect, update_rect, updated_player_rect, top_rect, player):
        if top_rect.colliderect(pygame.Rect(updated_player_rect.centerx - 25, updated_player_rect.bottom, 75, 10)) and player.die == False:
            self.switch_imgs("die")
            pygame.mixer.Sound.play(ENEMY_DIE_SND)
            self.dead = True

        if self.dead:
            self.dead_timer += 1 
            if self.dead_timer >= 60:
                return True
            return False  
             
        if top_rect.collidelistall(tile_rect):
            self.direction *= -1

        self.pos.x += self.direction 

        

        self.pos.y += self.force
        if update_rect.collidelistall(tile_rect):
            self.pos.y += self.force * -1
            self.force = 0
            
        else:
            self.force += 0.5

              

    def update(self, tile_rect, update_rect, updated_player_rect, player):
        top_rect = pygame.Rect(update_rect.left, update_rect.top, 128, 5)
        result = self.movement(tile_rect, update_rect, updated_player_rect, top_rect, player)

        

        if updated_player_rect.colliderect(update_rect) and self.dead == False:
            #update_rect.centerx < updated_player_rect.centerx THIS IS FALSE WHEN COLLIDNG FROM LEFT TRUE WHEN COLLDING FROM RIGHT
            if update_rect.centerx < updated_player_rect.centerx:
                player.speed_x = 12
            elif update_rect.centerx > updated_player_rect.centerx:
                player.speed_x = -12
            player.force = -10  
            player.controlled_movement = True
 
        return result 
    