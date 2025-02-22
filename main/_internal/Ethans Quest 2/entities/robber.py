import pygame
import os
from constants import *
import random
from important import *


#SPRITES 
idle1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/robber/idle1.png"))
idle2 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/robber/idle2.png"))
idle3 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/robber/idle3.png"))

attack1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/robber/walk1.png"))
attack2 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/robber/walk2.png"))
attack3 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/robber/walk3.png"))
attack4 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/robber/walk4.png"))

damage1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/robber/damage1.png"))
damage2 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/robber/damage2.png"))
damage3 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/robber/damage3.png"))

die1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/robber/die1.png"))
die2 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/robber/die2.png"))
die3 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/robber/die3.png"))

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


class BossRobber:
    def __init__(self, pos):
        self.pos = pos
      
        self.imgs = []
        self.rect_size = (128, 128)
        self.posstart = pos
        for i in range(10): 
            self.imgs.append(idle1)
        for i in range(10):
            self.imgs.append(idle2)
        for i in range(10): 
            self.imgs.append(idle3)
       
        
        
        self.img_val = 0  

        self.state = "idle"
        self.dir = -1
        self.force = 0
        self.dead = False
        
        
        self.t = 0
        self.t2 = 0
        
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
        if self.dir == 1:
            image = pygame.transform.flip(self.imgs[self.img_val], True, False)
        elif self.dir == -1:
            image = pygame.transform.flip(self.imgs[self.img_val], False, False)
        return image
    
    def switch_imgs(self, type):
        self.imgs.clear() 
        
        if type == "idle":
            for i in range(10): 
                self.imgs.append(idle1)
            for i in range(10):
                self.imgs.append(idle2)
            for i in range(10): 
                self.imgs.append(idle3)
            
        if type == "attack":
            for i in range(10): 
                self.imgs.append(attack1)
            for i in range(10):
                self.imgs.append(attack2)
            for i in range(10): 
                self.imgs.append(attack3)
            for i in range(10):
                self.imgs.append(attack4)
        if type == "damage":
            for i in range(10): 
                self.imgs.append(damage1)
            for i in range(10):
                self.imgs.append(damage2)
            for i in range(10): 
                self.imgs.append(damage3)
            
        if type == "die":
            for i in range(10): 
                self.imgs.append(die1)
            for i in range(10):
                self.imgs.append(die2)
            for i in range(10): 
                self.imgs.append(die3)
        
                
                 
    def update(self, tile_rect, update_rect, updated_player_rect, player, screen, pause):
        self.switch_imgs(self.state)
        
        if player.can_move == True and pause.is_paused == False:
            match self.state:
                case "idle":
                    self.attack_timer = 0
                   

                    self.damage_timer = 0
                    if self.timer >= 120:
                        self.state = "attack"
                    self.timer += 1


                case "attack":
                    self.timer = 0
                    self.damage_timer = 0
                    update_rect.height = 240
                    
                    top_rect = pygame.Rect(update_rect.left, update_rect.top, 128, 5)
                    #pygame.draw.rect(screen, (0,0,0), update_rect)

                    self.attack_timer += 1
                    if top_rect.colliderect(pygame.Rect(updated_player_rect.centerx - 25, updated_player_rect.bottom, 75, 10)) and player.die == False and self.state != "damage":
                        self.health -= 1
                        self.state = "damage"
                    
                    if updated_player_rect.colliderect(update_rect) and player.invincible == False:
                        player.health -= 1
                        player.invincible = True

                    if self.t >= 60:
                        self.pos.x += 2
                        self.dir = 1
                        if self.t2 >= 60:
                            self.t = 0
                            self.t2 = 0
                        self.t2 += 1
                    else:
                        self.pos.x -= 2
                        self.dir = -1
                    self.t += 1

                    if self.attack_timer >= 300:
                        self.state = "idle"


                case "damage":
                    self.timer = 0
                    self.attack_timer = 0

                    if self.damage_timer >= 60:
                        self.state = "idle"
                    self.damage_timer += 1   
                case "die":

                    if self.dead_timer >= 60:

                        update_rects = pygame.Rect(self.pos, (128, 128))

                        de = self.star.update(tile_rect, update_rects, updated_player_rect, player, screen, pause)
                        if de == False:
                            screen.blit(self.star.draw(), update_rects.topleft)

                    self.dead_timer += 1
                    #lol




        if self.health <= 0:
            self.state = "die"
             
        return False 
    
    
    


