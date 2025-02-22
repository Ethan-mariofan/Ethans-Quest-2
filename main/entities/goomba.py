import pygame
import os
from constants import *

#BROWN
br_goomba_walk1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/enemies/goomba/1_normal.png"))
br_goomba_walk2 = pygame.image.load(os.path.join(GAME_PATH, "sprites/enemies/goomba/2_normal.png"))
br_goomba_die = pygame.image.load(os.path.join(GAME_PATH, "sprites/enemies/goomba/dead_normal.png"))

#BLUE 
bl_goomba_walk1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/enemies/goomba/1_blue.png"))
bl_goomba_walk2 = pygame.image.load(os.path.join(GAME_PATH, "sprites/enemies/goomba/2_blue.png"))
bl_goomba_die = pygame.image.load(os.path.join(GAME_PATH, "sprites/enemies/goomba/dead_blue.png"))


#pumpkin
pk_goomba_walk1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/enemies/goomba/1_p.png"))
pk_goomba_walk2 = pygame.image.load(os.path.join(GAME_PATH, "sprites/enemies/goomba/2_p.png"))
pk_goomba_die = pygame.image.load(os.path.join(GAME_PATH, "sprites/enemies/goomba/dead_p.png"))





class Goomba:
    def __init__(self, pos, color):
        self.pos = pos
        self.imgs = []
        self.rect_size = (128, 128)
        self.color = color 

        if self.color == "brown":
            for i in range(10): 
                self.imgs.append(br_goomba_walk1)
            for i in range(10):
                self.imgs.append(br_goomba_walk2)
        if self.color == "blue":
            for i in range(10): 
                self.imgs.append(bl_goomba_walk1)
            for i in range(10):
                self.imgs.append(bl_goomba_walk2)
        if self.color == "pumpkin":
            for i in range(10): 
                self.imgs.append(pk_goomba_walk1)
            for i in range(10):
                self.imgs.append(pk_goomba_walk2)
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
            if self.color == "brown":
                for i in range(10): 
                    self.imgs.append(br_goomba_die)
            if self.color == "blue":
                for i in range(10): 
                    self.imgs.append(bl_goomba_die)
            if self.color == "pumpkin":
                for i in range(10): 
                    self.imgs.append(pk_goomba_die)
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

        if updated_player_rect.colliderect(update_rect) and player.invincible == False and self.dead == False:
            player.health -= 1
            player.invincible = True

        return result

        

    
