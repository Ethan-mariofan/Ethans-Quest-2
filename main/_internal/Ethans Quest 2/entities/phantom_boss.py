import pygame

import os
from constants import *  

#IMPORTANT TO DEFINE NEW CLASSES FOR A GRAND STAR
star1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/objs/starg/1.png"))
star2 = pygame.image.load(os.path.join(GAME_PATH, "sprites/objs/starg/2.png"))
star3 = pygame.image.load(os.path.join(GAME_PATH, "sprites/objs/starg/3.png"))
star4 = pygame.image.load(os.path.join(GAME_PATH, "sprites/objs/starg/4.png"))
class StarEndLevelGrand:
    def __init__(self, pos):
        self.pos = pos

        self.rect_size = pygame.Vector2(128, 128)

        self.imgs = []
        self.img_val = 0

        for i in range(10):
            self.imgs.append(star1)
        for i in range(10):
            self.imgs.append(star2)
        for i in range(10):
            self.imgs.append(star3)
        for i in range(10):
            self.imgs.append(star4)
 
    
    def draw(self):
        self.img_val += 1
        if self.img_val >= len(self.imgs):
            self.img_val = 0 
        return self.imgs[self.img_val]
    
    def update(self, x, update_rect, updated_player_rect, player, screen, pause): 
        if updated_player_rect.colliderect(update_rect):
            pygame.mixer.Sound.play(GOT_STAR_SND)  

            player.chapter_completed = True
 
            return True
        return False  
    
#SPRITES
idle1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/phantom/idle1.png"))
idle2 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/phantom/idle2.png"))
idle3 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/phantom/idle3.png"))
idle4 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/phantom/idle4.png")) 
    
die1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/phantom/die1.png"))
die2 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/phantom/die2.png"))
die3 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/phantom/die3.png"))
die4 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/phantom/die4.png")) 
    
attack1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/phantom/attack1.png"))
attack2 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/phantom/attack2.png"))
    
damage1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/phantom/damage1.png"))
damage2 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/phantom/damage2.png"))
    
#PHANTOM
class Phantom:
    def __init__(self, pos):
        self.pos = pos
        self.imgs = []
        self.rect_size = (128, 128) 
        
        for i in range(10):
            self.imgs.append(idle1)
        for i in range(10):
            self.imgs.append(idle2)
        for i in range(10):
            self.imgs.append(idle3)
        for i in range(10):
            self.imgs.append(idle4)
        
        self.img_val = 0

        self.state = "idle"
        self.force = 0
        self.dead = False

        self.attack_timer2 = 0
        
        self.health = 5
        self.star = StarEndLevelGrand(self.pos)
        self.dead_timer = 0 
        self.timer = 0
        self.timer2 = 0
        self.attack_timer = 0
        self.damage_timer = 0

    def draw(self):
        self.img_val += 1
        if self.img_val >= len(self.imgs):
            self.img_val = 0 
        return self.imgs[self.img_val] 
    
    def switch_imgs(self, type):
        self.imgs.clear() 
        
        if type == "idle":
            for i in range(10): 
                self.imgs.append(idle1)
            for i in range(10):
                self.imgs.append(idle2)
            for i in range(10): 
                self.imgs.append(idle3)
            for i in range(10):
                self.imgs.append(idle4)
        if type == "attack":
            for i in range(10): 
                self.imgs.append(attack1)
            for i in range(10):
                self.imgs.append(attack2)
           
        if type == "damage":
            for i in range(10): 
                self.imgs.append(damage1)
            for i in range(10):
                self.imgs.append(damage2)
            
            
        if type == "die":
            for i in range(10): 
                self.imgs.append(die1)
            for i in range(10):
                self.imgs.append(die2)
            for i in range(10):  
                self.imgs.append(die3)
            for i in range(10):
                self.imgs.append(die4)

    def update(self, tile_rect, update_rect, updated_player_rect, player, screen, pause):
        self.switch_imgs(self.state) 

        match self.state:
            case "idle": 
                self.pos = self.pos.move_towards(pygame.Vector2(500, 500), 2) 
 

                if self.timer >= 120:
                    self.state = "attack" 
                self.timer += 1
 
            case "attack":
                self.timer = 0
                self.damage_timer = 0
                  
                if update_rect.colliderect(updated_player_rect):
                    self.health -= 1
                    self.state = "damage"

                self.attack_timer += 1
                if self.attack_timer >= 60:
                    self.pos = self.pos.move_towards(pygame.Vector2(player.pos.x, player.pos.y), 3) #faster
                    if self.attack_timer2 >= 60:
                        self.attack_timer = 0
                        self.attack_timer2 = 0
                    self.attack_timer2 += 1
                else:
                    self.pos = self.pos.move_towards(pygame.Vector2(player.pos.x, player.pos.y), 2) #to 

            case "damage":
                self.timer = 0
                self.attack_timer = 0
                self.attack_timer2 = 0
                
                if self.damage_timer >= 60:
                    self.state = "idle"
                self.damage_timer += 1  
            case "die":
                self.pos.y = 500
                
                if self.dead_timer >= 60:
                    
                    update_rects = pygame.Rect(self.pos, (128, 128))

                    
                      
                   
                    de = self.star.update(tile_rect, update_rects, updated_player_rect, player, screen, pause)
                    if de == False:
                        screen.blit(self.star.draw(), update_rects.topleft)

                self.dead_timer += 1
        if self.health <= 0:
            self.state = "die"
             
        return False 