import pygame
import os
import yaml
from constants import *
from important import * 
from music_manager import *


class CutsceneManager:
    def __init__(self, scene_id, pos):
        self.scene_id = scene_id
        self.screen = 0
        self.pos = pos
        
       

        self.file_name = 'cutscenes/cutscene_' + str(self.scene_id) + '.yml'
 
        self.started = True
    
        self.active = False
        with open(os.path.join(GAME_PATH, self.file_name), 'r') as file:
            data = yaml.full_load(file)  
            
        self.individual_scene = data.get('scenes')
        self.indiv_index = 0
        
        self.msgs = data.get('msgs')
        self.type_of_scene = data.get('types')
        
        self.actor_pos = data.get('pos')
        self.actor_img = data.get('img')
        self.character = data.get('character')
        self.indiv_scenes = []
        
        self.portraits = data.get('portraits')
        
        
        self.music = data.get('music')
        self.musicend = data.get('musicend')
        
        
        self.box_width_and_height = pygame.Vector2(900, 200) #X IS WIDTH, Y IS HEIGHT
        
        self.box = pygame.rect.Rect(10, 500, self.box_width_and_height.x, self.box_width_and_height.y) 
        self.box2 = pygame.rect.Rect(20, 510, self.box_width_and_height.x - 20, self.box_width_and_height.y - 20) 
        #OFFSET 10
        
        self.fix = True
        self.timer = 0
        self.x = self.actor_pos[0]
        self.y = self.actor_pos[1]
   
        self.cutscene_started = True
        self.cutscene_finished = False
        
        self.start_pos = CAMERA_POSITION
   
           
    def start(self): #call this function if we enter the invisible hitbox in a level
       # self.active = True
        #if self.type_of_scene == "dialogue":
        
        
            
    
        for indiv in self.individual_scene:
            self.indiv_scenes.append(indiv)
        
        
 
    
    def draw(self, screen):
        #SCENE BARS 
        pygame.draw.rect(screen, (0,0,0), (0,0,1000, 50))
        pygame.draw.rect(screen, (0,0,0), (0,950,1000, 50))
         
    
    def end(self):
        self.active = False
        
   
                    
                    
                    
    def start_dialogue(self):
        pass
    
    
    def draw_dialogue(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.box) 
        
        pygame.draw.rect(screen, (255, 255, 255), self.box2)
        
           
        for msg in self.msgs:
            if self.msgs.index(msg) == self.indiv_index and self.active == True:
                draw_text(msg, (0,0,0), pygame.Vector2(self.box2.x + self.box2.width // 2, self.box2.y + self.box2.height // 2), self.screen)
                
                
        
            
    def end_dialogue(self):
        pass
    
    
    def update_dialogue(self, screen):
        if self.active: 
            self.draw_dialogue(screen)  
            
            
            for imgp in self.portraits:
                if self.portraits.index(imgp) == self.indiv_index:
                    self.screen.blit(pygame.image.load(os.path.join(GAME_PATH, f"sprites/cutscenes/pic/" + imgp + ".png")), (self.box2.x + 200, self.box2.y - 127))
                  
              
               
            keys = pygame.key.get_pressed()
            
            if i >= 1:
                blah = controller.get_button(1)
            else:
                blah = keys[KEY_JUMP]
            
            
            if blah:
                if self.fix == True: 
                    self.indiv_index += 1
                    self.fix = False 
                
                
            if blah:
                if self.fix == False:
                    pass

            elif self.fix == False:
                if self.timer >= 200: #cooldown for dialogue    
                    self.fix = True
                self.timer += 1
            else:
                self.timer = 0
                   
    
    def actor_entity(self):
        if self.active:
            
            
            if self.character == "none":
                pass
            
            if self.character == "starly_for_cutscene_2": #OK SO THE CHARACTERS HAVE DIFFERENT BEHAVIORS DURING A CUTSCENE
                if self.indiv_index >= 2:
                    self.y += 2
                    if self.y >= 400:
                        self.y = 400 
                if self.indiv_index >= 6:
                    self.y -= 10

            if self.character == "ruinsMaster1":
                if self.indiv_index > 0: 
                    
                    
                    if self.y + 256 == 768 - 128: #HARD CODE IS 768
                        self.y = 768 - 256 - 128
                    else:
                        self.y += 3
            if self.character == "starly5":
                if self.indiv_index > 0: 
                    self.y += 2
                    if self.y >= 400: 
                        self.y = 400 
                if self.indiv_index > 6:
                    self.y -= 11
                    
            if self.character == "gear":
                if self.indiv_index > 4:
                    self.y -= 5
                    self.x -= 1
            
            if self.character == "spark":
                if self.indiv_index > 7:
                    self.y -= 100
                
            if self.character == "spark2":
                if self.indiv_index > 6:
                    self.y -= 5
            if self.character == "crystal":
                if self.indiv_index >= 3:
                    self.y -= 7
            if self.character == "penguin":
                if self.indiv_index >= 0:
                    self.y = 128 * 4 + 72
                    
            if self.character == "spark_pumpkin":
                if self.cutscene_finished:
                    self.y = 10000
                    
            if self.character == "starly_lava":
                if self.indiv_index ==  4:
                    self.y += 1
                    
                    if self.y >= 500:
                        self.y = 500
                if self.indiv_index >= 7:
                    self.y -= 10
            if self.character == "boss":
                if self.indiv_index >= 7:
                    self.x -= 3
                    if self.x <= CAMERA_POSITION.x - 1:
                        self.y += 1
                    
                        
            self.screen.blit(pygame.image.load(os.path.join(GAME_PATH, self.actor_img)), (self.x, self.y))
        
    
     
    
    def update(self, player_rect, update_rect, screen): #always call this 
        self.screen = screen
        
        
            
        if self.active:
            #self.cutscene_started = True
            self.draw(screen) 
            
            
            self.start()
            for type in self.type_of_scene:
                if type == "D":
                    self.update_dialogue(screen)
                #IF TYPE IS S THEN SCREEN SHAKE
                #IF TYPE IS A THEN PLAY AN ANIMATION ON AN ENTITY
                #ETC 
           
            for sc in self.indiv_scenes: 
                if self.indiv_index > sc:
                    self.active = False 
        
                  
        if player_rect.colliderect(update_rect) and self.started == True:
            self.active = True
            return True
        return False
           
             