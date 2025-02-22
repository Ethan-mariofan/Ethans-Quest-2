import pygame
import os
from constants import *
import random
from important import *

idle1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/Starly/idle1.png"))
idle2 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/Starly/idle2.png"))
idle3 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/Starly/idle3.png"))
idle4 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/Starly/idle4.png"))


attack1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/Starly/attack1.png"))
attack2 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/Starly/attack2.png"))
attack3 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/Starly/attack3.png"))
attack4 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/Starly/attack4.png"))

damage1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/Starly/damage1.png"))
damage2 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/Starly/damage2.png"))
damage3 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/Starly/damage3.png"))

die1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/Starly/die1.png"))
die2 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/Starly/die2.png"))
die3 = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/Starly/die3.png"))

onfloordead = pygame.image.load(os.path.join(GAME_PATH, "sprites/bosses/Starly/on_ground_dead.png"))
 


#BROWN
br_goomba_walk1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/enemies/goomba/1_normal.png"))
br_goomba_walk2 = pygame.image.load(os.path.join(GAME_PATH, "sprites/enemies/goomba/2_normal.png"))
br_goomba_die = pygame.image.load(os.path.join(GAME_PATH, "sprites/enemies/goomba/dead_normal.png"))

#BLUE 
bl_goomba_walk1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/enemies/goomba/1_blue.png"))
bl_goomba_walk2 = pygame.image.load(os.path.join(GAME_PATH, "sprites/enemies/goomba/2_blue.png"))
bl_goomba_die = pygame.image.load(os.path.join(GAME_PATH, "sprites/enemies/goomba/dead_blue.png"))


class GoombaStarly:
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

class BossStarly:
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
        for i in range(10):
            self.imgs.append(idle4)
        
        
        self.img_val = 0  

        self.state = "idle"
        self.force = 0
        self.dead = False
        
        self.health = 5
        
        self.enemy = GoombaStarly(self.pos, "blue")
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
            
        if type == "die":
            for i in range(10): 
                self.imgs.append(die1)
            for i in range(10):
                self.imgs.append(die2)
            for i in range(10): 
                self.imgs.append(die3)
        if type == "on_floor_dead":
            for i in range(10): 
                self.imgs.append(onfloordead)
                
                 
    def update(self, tile_rect, update_rect, updated_player_rect, player, screen, pause):
        self.switch_imgs(self.state)
        
        match self.state:
            case "idle":
                self.attack_timer = 0
                self.pos = self.pos.move_towards(pygame.Vector2(random.randint(300, 500), 500), 3)
                self.damage_timer = 0
                if self.timer >= 120:
                    self.state = "attack"
                self.timer += 1
                
                
            case "attack":
                self.timer = 0
                self.damage_timer = 0
                
            
                self.attack_timer += 1
                if self.attack_timer == 60:
                    self.enemy = GoombaStarly(self.pos, "blue")    
                if self.attack_timer >= 61:
                    
                    update_rectg = pygame.Rect(self.enemy.pos, self.enemy.rect_size)

                    if update_rectg.x < 1500:                  
                        screen.blit(self.enemy.draw(), update_rectg.topleft)
 
                        if player.can_move == True and pause.is_paused == False:
                            
                            delete2 = self.enemy.update(tile_rect, update_rectg, updated_player_rect, player)
                            if delete2 and self.state != "damage":
                                self.health -= 1
                                self.state = "damage" 
                                 
                                
                if self.attack_timer >= 340:
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
                #lol
               
                        
            case "on_floor_dead":
                pass


        if self.health <= 0:
            self.state = "die"
             
        return False 
    
    
    


