import pygame
import os
from constants import *


#walk
pl_walk1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/player/walk1.png"))
pl_walk2 = pygame.image.load(os.path.join(GAME_PATH, "sprites/player/walk2.png"))
pl_walk3 = pygame.image.load(os.path.join(GAME_PATH, "sprites/player/walk3.png"))
pl_walk4 = pygame.image.load(os.path.join(GAME_PATH, "sprites/player/walk4.png"))
pl_walk5 = pygame.image.load(os.path.join(GAME_PATH, "sprites/player/walk5.png"))
pl_walk6 = pygame.image.load(os.path.join(GAME_PATH, "sprites/player/walk6.png"))

#jump
pl_jump1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/player/jump1.png"))
pl_jump2 = pygame.image.load(os.path.join(GAME_PATH, "sprites/player/jump2.png"))
pl_jump3 = pygame.image.load(os.path.join(GAME_PATH, "sprites/player/jump3.png"))

#idle
pl_idle1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/player/idle1.png"))
pl_idle2 = pygame.image.load(os.path.join(GAME_PATH, "sprites/player/idle2.png"))
pl_idle3 = pygame.image.load(os.path.join(GAME_PATH, "sprites/player/idle3.png"))


pl_die1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/player/die1.png")) 
   
class Player:
    def __init__(self, pos):
        self.pos = pos
        self.coins = 0
        self.keys = pygame.key.get_pressed()
        self.rect_size = (128, 256)
 
        self.force = 0
        self.on_ground = False

        self.img = []
        #for i in range(10): 
        #    self.img.append(pl_idle1)
        #for i in range(10):
        #    self.img.append(pl_idle2)
        #for i in range(10): 
        #    self.img.append(pl_idle3) 
        
        self.can_move = True
        
        self.can_jump = False
    
        self.img_val = 0 
        self.speed_x = 0

        self.cool_down = 0

        self.dir = 1
        self.health = 3
        self.invincible = False
        self.inv_timer = 0

        self.checkpoint_pos = pygame.Vector2()
        self.checkpoint_gotton = False
        self.checkpoint_start_pos = pygame.Vector2()

        self.die = False
        self.controlled_movement = False


        #star stuff
        
        self.completed_level = False
        self.chapter_completed = False

    def draw(self):
        self.img_val += 1
        if self.img_val >= len(self.img):
            self.img_val = 0

        if self.dir == 1:
            pygame.transform.flip(self.img[self.img_val], False, False)

        if self.dir == -1:
            self.img[self.img_val] = pygame.transform.flip(self.img[self.img_val].copy(), True, False)

        return self.img[self.img_val]
    def switch_img(self, type):
        self.img.clear()
         
        if type == "idle":
            for i in range(10): 
                self.img.append(pl_idle1)
            for i in range(10):
                self.img.append(pl_idle2)
            for i in range(10):
                self.img.append(pl_idle3) 
        if type == "walk":
            
            for i in range(10): 
                self.img.append(pl_walk1)
            for i in range(10):
                self.img.append(pl_walk2)
            for i in range(10):
                self.img.append(pl_walk3) 
            for i in range(10): 
                self.img.append(pl_walk4)
            for i in range(10):
                self.img.append(pl_walk5)
            for i in range(10):
                self.img.append(pl_walk6) 
        if type == "jump":

            for i in range(10): 
                self.img.append(pl_jump1)
            for i in range(10):
                self.img.append(pl_jump2)
            for i in range(10):
                self.img.append(pl_jump3) 
        if type == "die":
            for i in range(10): 
                self.img.append(pl_die1) 
    

   
    def gravity(self, tile_rect, update_rect):
        self.pos.y += self.force 
        player_rect = pygame.Rect(update_rect.x,  update_rect.y, 128, 256)

        
        
        #pygame.draw.rect(screen, (0,0,0), tile_rect, 6)
        self.keys = pygame.key.get_pressed()
        if i >= 1:
            blah66 = controller.get_button(1)
        else:
            blah66 = self.keys[KEY_JUMP]
               
        if player_rect.collidelistall(tile_rect):
            self.pos.y += self.force * -1
            self.force = 0
            self.cool_down += 1
            if blah66:
                if self.cool_down >= 10 and not self.completed_level and self.can_move: 
                    self.force = -16
                    self.pos.y -= 10  
                    
                    pygame.mixer.Sound.play(PLAYER_JUMP_SND)
        else:
            if self.die == False:
                self.switch_img("jump")  
            self.cool_down = 0 
            self.force += 0.5

    def update(self, tile_rect, update_rect):
        self.gravity(tile_rect, update_rect)
        
        if self.invincible:
            self.inv_timer += 1
            if self.inv_timer >= 120:
                self.invincible = False
                self.inv_timer = 0

    