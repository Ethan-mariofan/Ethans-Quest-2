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



idle1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/FinalBoss/1.png"))
idle2 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/FinalBoss/2.png"))
idle3 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/FinalBoss/3.png"))
idle4 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/FinalBoss/4.png"))

attack1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/FinalBoss/attack1.png"))
attack2 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/FinalBoss/attack2.png"))
attack3 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/FinalBoss/attack3.png"))
attack4 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/FinalBoss/attack4.png"))

damage1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/FinalBoss/damage1.png"))
damage2 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/FinalBoss/damage2.png"))
damage3 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/FinalBoss/damage3.png"))
damage4 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/FinalBoss/damage4.png"))

die1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/FinalBoss/die1.png"))
die2 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/FinalBoss/die2.png"))
die3 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/FinalBoss/die3.png"))
die4 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/FinalBoss/die4.png"))

lazer = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/FinalBoss/lazer.png"))




class Lazer:
    def __init__(self, pos):
        self.pos = pos
     
        self.rect_size = (128, 128)
        
        self.img = lazer
        
    
        
    def draw(self):
        return self.img

    
         

    def update(self, tile_rect, update_rect, updated_player_rect, player):
        self.pos.y += 3
 
        if self.pos.y >= 1000:
            return True

        if updated_player_rect.colliderect(update_rect) and player.invincible == False:
            player.health -= 1
            player.invincible = True

        return False










class FinalBoss:
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
        self.dir = -1
        self.force = 0
        self.dead = False
        
        
        self.health = 8 #final boss 8 health 
        
        
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
            for i in range(10): 
                self.imgs.append(damage4)
            
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
                
                self.attack_timer = 0
                self.damage_timer = 0
                if self.timer >= 60 and self.timer < 120:
                    self.pos = self.pos.move_towards(pygame.Vector2(500, 400), 3)
                    
                elif self.timer >= 120 and self.timer < 400:
                    self.pos = self.pos.move_towards(pygame.Vector2(450, 680), 3)
                    
                elif self.timer >= 400:
                    self.state = "attack"
                self.timer += 1
            
            case "attack":
                if update_rect.colliderect(updated_player_rect):
                    self.health -= 1
                    self.state = "damage"
                    
                self.pos = pygame.Vector2(500, 650)
                self.timer = 0
                self.damage_timer = 0
                
                self.attack_timer += 1
                
                if self.attack_timer == 220:
                    self.enemy = Lazer(pygame.Vector2(500, 50))   
                    #self.enemy2 = Lazer(pygame.Vector2(750, 50))
                if self.attack_timer >= 221:
                    update_rectg = pygame.Rect(self.enemy.pos, self.enemy.rect_size)

                    if update_rectg.x < 1500:                  
                        screen.blit(self.enemy.draw(), update_rectg.topleft)
 
                        if player.can_move == True and pause.is_paused == False:
                            
                            nextstate = self.enemy.update(tile_rect, update_rectg, updated_player_rect, player)
                            if nextstate:  
                                self.state = "idle"
            case "damage":
                self.timer = 0
                self.attack_timer = 0

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