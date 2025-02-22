import pygame
import os
import yaml 

from constants import *  
#from important import *
from music_manager import *
from pause_menu import *
from important import save

lvl_completed = pygame.image.load(os.path.join(GAME_PATH, "sprites/maps/node_completed.png"))
lvl_unlocked = pygame.image.load(os.path.join(GAME_PATH, "sprites/maps/node_unlocked.png"))
lvl_locked = pygame.image.load(os.path.join(GAME_PATH, "sprites/maps/node_locked.png"))



player = pygame.image.load(os.path.join(GAME_PATH, "sprites/maps/ethan_player.png"))

   


 
class Map:
    def __init__(self, screen, map_number, level, track, levelac):
        self.screen = screen
        self.world_pos = pygame.Vector2()
        self.map_number = map_number

        with open(os.path.join(GAME_PATH, f"sprites/maps/chapter{map_number}/map_pos.yml"), 'r') as file:
            self.data = yaml.full_load(file)  

        self.map_pos = pygame.Vector2(1500, 2000)

        #play audio here and add the map music in constants
        self.music_track = track 
        self.mscmgr = MusicManager(self.music_track, True)
        self.mscmgr.play() 
 
        self.level = level   
        
        self.save_img = pygame.image.load(os.path.join(GAME_PATH, "sprites/menus/pause/map.png"))  

        self.node_positions = self.data.get('map')
        self.nodes = {}

        #node the player is currently standing on
        #hello 
        self.current_node = level
        self.ac_level = levelac

        self.paths = self.data.get('node' + str(self.current_node) + "_paths")

        self.is_moving = False
        self.active_path = []

        self.map = pygame.image.load(os.path.join(GAME_PATH, f"sprites/maps/chapter{map_number}/map.png"))
        
        
 
        #self.cooldown = 0

        #for node in self.node_positions:
        #    self.nodes.append(node)

        

        self.player_pos = pygame.Vector2(self.node_positions[str(level)][0], self.node_positions[str(level)][1])
        self.pause_var = False
        self.pause = PauseMenu(self.screen, self.pause_var, pygame.image.load(os.path.join(GAME_PATH, "sprites/menus/pause/buttons2.png")), "title")
        self.a = self.pause.a 
        self.map_pos = self.player_pos

    def world_to_screen(self, world_coordinate: pygame.Vector2) -> pygame.Vector2:
        return world_coordinate - self.map_pos + SCREEN_CENTER  
    
    def get_rect(self, position, size):
        return pygame.Rect(position.x, position.y, size[0], size[1])

    def move(self, pos, speed, points):
        circle_dir = pygame.math.Vector2(points[0]) - pos
        if circle_dir.length() <= speed:
            pos = points[0]
            #points.append(points[0])
            points.pop(0)
        else:
            circle_dir.scale_to_length(speed)
            new_pos = pygame.math.Vector2(pos) + circle_dir
            pos = (new_pos.x, new_pos.y)
            self.map_pos = new_pos
        #print(self.player_pos.distance_to(pygame.Vector2(points[-1][0], points[-1][1])), points)

        return pygame.Vector2(pos)

    def update_pause(self):
        self.pause.draw()
        update_pause = self.pause.update()
        # self.pause.is_paused = False
        self.a = self.pause.a 

        continue_rect = pygame.rect.Rect(31, 234, 259, 90)
        
        return_to_map_rect = pygame.rect.Rect(34, 455, 259, 204)
        
        
        pos = pygame.mouse.get_pos()
        pressed1 = pygame.mouse.get_pressed()[0]
         
        
        if self.pause.layout_x_pos >= 0 and self.pause.is_paused == True:
            if continue_rect.collidepoint(pos) and pressed1:
                self.pause.is_paused = False #unpause
            
            if return_to_map_rect.collidepoint(pos) and pressed1 and cooldown >= 2:
                self.mscmgr.stop()
                self.pause.a = True
                self.pause.is_paused = False
                
        
            # if cooldown < 2:
            #     return self.goto
             
            
        if i >= 1:
            blah66 = controller.get_button(0)
        else:
            blah66 = self.keys[KEY_X]
            
        
        keys = pygame.key.get_pressed()
        
        if blah66: #0
            self.pause.is_paused = True      
    

        if update_pause == "title":
            return True
        else:
            return False 
        
    def save_pro(self):
        pass
    
        

    def update(self):

        


        self.keys = pygame.key.get_pressed()
        
        #old movement system
        #if self.keys[pygame.K_d]:
        #    map_pos.x += 10
        #elif self.keys[pygame.K_a]: 
        #    map_pos.x -= 10
        #elif self.keys[pygame.K_w]:
        #    map_pos.y -= 10
        #elif self.keys[pygame.K_s]: 
        #    map_pos.y += 10

        self.screen.blit(self.map, self.world_to_screen(self.world_pos))
        
        if i >= 1:
            blah2 = controller.get_button(14)
            blah3 = controller.get_button(13)
            
            blah4 = controller.get_button(11)
            blah5 = controller.get_button(12)
            
            
            blah = controller.get_button(1)
        else:
            blah2 = self.keys[KEY_RIGHT]
            blah3 = self.keys[KEY_LEFT]
            blah4 = self.keys[KEY_UP]
            blah5 = self.keys[KEY_DOWN]
            
            blah = self.keys[KEY_JUMP]
            
        #print(world_to_screen(pygame.Vector2(self.nodes[0], self.nodes[1])))

        for j in self.node_positions:
            index = int(j)
            img = lvl_locked
            if index == self.level:
                img = lvl_unlocked
            elif index < self.level:
                img = lvl_completed
            self.screen.blit(img, self.world_to_screen(pygame.Vector2(self.node_positions[j][0], self.node_positions[j][1])))
            
        self.screen.blit(player, self.world_to_screen(pygame.Vector2(self.player_pos.x, self.player_pos.y)))
        self.update_pause()

        self.is_moving = len(self.active_path) > 0
        if self.is_moving:
            self.player_pos = self.move(self.player_pos,2, self.active_path) 
            return False
        
        self.paths = self.data.get('node' + str(self.current_node) + "_paths")
        #print(self.current_node, self.paths)
        

        if blah2:
            if len(self.paths["RIGHT_PATH"]) > 0 and self.level >= self.paths["COMPLETE"][2]:
                self.is_moving = True
                self.active_path = self.paths["RIGHT_PATH"].copy()
                self.current_node = self.paths["COMPLETE"][2]
            
 
        if blah5:
            if len(self.paths["DOWN_PATH"]) > 0 and self.level >= self.paths["COMPLETE"][1]:
                self.is_moving = True
                self.active_path = self.paths["DOWN_PATH"].copy()
                self.current_node = self.paths["COMPLETE"][1]

        if blah4:
            if len(self.paths["UP_PATH"]) > 0 and self.level >= self.paths["COMPLETE"][0]:
                self.is_moving = True
                self.active_path = self.paths["UP_PATH"].copy()
                self.current_node = self.paths["COMPLETE"][0]
 
        if blah3:
            if len(self.paths["LEFT_PATH"]) > 0 and self.level >= self.paths["COMPLETE"][3]:
                self.is_moving = True
                self.active_path = self.paths["LEFT_PATH"].copy()
                self.current_node = self.paths["COMPLETE"][3]


        
        if blah:
            return "self.current_node"
            
        self.screen.blit(self.save_img, (0, 0)) 
        
        pos_sv = pygame.mouse.get_pos()
        pressed1_sv = pygame.mouse.get_pressed()[0]
        save_rect = self.save_img.get_rect()
    
        if save_rect.collidepoint(pos_sv) and pressed1_sv:
            save(self.map_number, self.ac_level, self.level)
      

 
        if self.pause.is_paused:
            return False   
        
        return False