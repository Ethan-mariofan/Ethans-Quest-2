import os
import pygame
from constants import *
from level import *
from entities.player import *
from important import *
from map import * 
from title_screen import * 
from intro_story import *  
from intro_chapter2 import * 
from intro_chapter3 import *        
from intro_chapter4 import *     
from intro_chapter5 import *  
from controlls import *
from intro_chapter6 import *
from ending_cutscene import *
from credits import *
               
pygame.init()   
pygame.mixer.init()      
     
pygame.display.set_caption("Ethan's Quest 2")    
pygame.display.set_icon(pygame.image.load(os.path.join("logo.png")))
  
cursor = pygame.cursors.Cursor((20, 20), pygame.image.load(os.path.join(GAME_PATH, "cursor.png")))
pygame.mouse.set_cursor(cursor)  
 
 
#REMINDER:
    #compile the game into an exe file   
    #play test the game all the way through 
         
      
      
                      
clock = pygame.time.Clock()      
 
    
levels = [ 
    ["cove", "cove", COAST_LINE, "sprites/effect/wisps.png", False], 
          ["cove", "cove", COAST_LINE, "sprites/effect/wisps.png", False], 
          ["cove_storm", "cove_storm", COVE_RUINS, "sprites/effect/rain.png", False], 
          ["cove_ruins", "cove_ruins", COVE_RUINS, "sprites/effect/none.png", True],  
          ["cove_ruins", "cove_ruins", COVE_RUINS, "sprites/effect/none.png", False], 
          ["castle", "castle", STARLY_ENCOUNTER, "sprites/effect/boss_die_star.png", False],
          ["western", "western", WESTERN_DESERT, "sprites/effect/none.png", False],
          ["western", "western", WESTERN_DESERT, "sprites/effect/none.png", False],
          ["oil", "oil", FACTORY, "sprites/effect/oil.png", False],
          ["western", "western", WESTERN_DESERT, "sprites/effect/none.png", False],  
          ["western", "western", WESTERN_DESERT, "sprites/effect/wind.png", False],
          ["oil", "oil", ROBBER, "sprites/effect/none.png", False],
          ["snow", "snow", SNOW, "sprites/effect/snow.png", False],
          ["snow", "snow", SNOW, "sprites/effect/snow.png", False],
          ["town_snow", "town_snow", SNOW, "sprites/effect/snow.png", False],
          ["snow", "snow", SNOW, "sprites/effect/snow.png", False],
          ["snow", "snow", SNOW, "sprites/effect/snow.png", False],
          ["igloo", "igloo", STARLY_ENCOUNTER, "sprites/effect/snow.png", False],
          ["pumpkin", "pumpkin", PUMPKIN, "sprites/effect/leaf.png", False],
          ["pumpkin", "pumpkin", PUMPKIN, "sprites/effect/leaf.png", False],
          ["pumpkin", "pumpkin_alt", SPOOKY, "sprites/effect/none.png", False],
          ["autumn", "autumn", PUMPKIN, "sprites/effect/leaf.png", False],
          ["autumn", "autumn", PUMPKIN, "sprites/effect/leaf.png", False],
          ["castle", "castle", SCARY, "sprites/effect/none.png", False],
          ["lava", "lava", LAVA, "sprites/effect/lava.png", False],  
          ["lava", "lava", LAVA, "sprites/effect/lava.png", False],
          ["lava", "lava", LAVA, "sprites/effect/lava.png", False],
          ["lava", "lava", LAVA, "sprites/effect/lava.png", False],
          ["lava", "lava", LAVA, "sprites/effect/lava.png", False],
          ["lava", "lava", CHASE, "sprites/effect/lava2.png", True],
          ["final", "final", DARK, "sprites/effect/none.png", False],
          ["final", "final", DARK, "sprites/effect/none.png", False], 
          ["final", "final", WE_ARE_EVIL, "sprites/effect/none.png", False]  
          ]      
                  
               
CAMERA_POSITION.x = 500       
CAMERA_POSITION.y = 475                      

                
        
screen = pygame.display.set_mode(SCREEN_SIZE, pygame.DOUBLEBUF | pygame.HWSURFACE)
        
title = None
level = None
map = None
intro = None 
intro2 = None    
intro3 = None
intro4 = None
intro5 = None
controll = None
intro6 = None
end = None 
credit = None
 
levels_completed = 0
    
game_state = "title"

    
   
        
running = True    
while running:     
    #key_or_controller()
    
    
        
        
    for event in pygame.event.get():  
        #if event.type == pygame.JOYDEVICEADDED:
        #    joy = pygame.joystick.Joystick(event.device_index)
        #    joystick.append(joy)
        if event.type == pygame.QUIT:                
            running = False       
    
    screen.fill((255, 255, 255))    

    
    if cooldown > 0:   
        cooldown -= 1    
        

    match game_state:    
        case "level": 
 
            if level == None: 
                level = Level(screen, active_level, levels[active_level-1][0], levels[active_level-1][1], levels[active_level-1][2], levels[active_level-1][3], levels[active_level-1][4], chapter_number_global) 
                continue

            controll = None
            intro2 = None
            intro4 = None
            title = None
            intro = None
            intro3 = None
            intro5 = None
            intro6 = None
            map = None
            end = None
            credit = None

            updated_level = level.update()
           
            if updated_level == 2:
                #map = None
                
                #level_number_global += 1
                chapter_number_global += updated_level - 1
                if levels_completed < active_level and level_number_global < 33:
                    
                    level_number_global += updated_level - 1  #updated_level
                    
                    active_level = level_number_global 
                    levels_completed += 1 
                 
                
                    
                
                
                if chapter_number_global == 2:
                    
                    
                    game_state = "intro2"  
                if chapter_number_global == 3:
                    
                    game_state = "intro3" 
                if chapter_number_global == 4:
                    
                    game_state = "intro4"#if its 2 it goes to intro2 if its 3 it goes to intro 3 etc...

                if chapter_number_global == 5:
                    
                    game_state = "intro5" 
                if chapter_number_global == 6:
                    
                    game_state = "intro6" 
                    
                if chapter_number_global == 7:
                    game_state = "ending" 
                    
               #######level = None
                     
            elif updated_level:
                #map = none
                if levels_completed < active_level and level_number_global < 33:
                    level_number_global += updated_level#updated_level
                    active_level = level_number_global
                    levels_completed += 1 
                 
                game_state = "map"    
                level = None 

            elif level.update_pause() or level.a == True:   
                #map = none
                game_state = "map"
                level = None
                         
                      
           
         
 
        case "map":  
            keys = pygame.key.get_pressed()
            if map == None:
                active_level = level_number_global
                map = Map(screen, chapter_number_global, level_number_global, CHAPTER1_MAP, active_level) 
                continue

            

    
            updated_map = map.update()
            controll = None
            end = None
            intro4 = None
            intro = None
            credit = None
            intro6 = None
            intro2 = None
            intro3 = None
            intro5 = None
            if updated_map == "self.current_node":  
                active_level = map.current_node 
                level = None
                
                game_state = "level"
                  
        
            elif updated_map or map.update_pause() or map.a == True:
                
                title = None       
                game_state = "title" 
    
        case "title":  

            if title == None:
                title = TitleScreen(screen, TITLE)
                continue
   
            if title.update() or title.button(): 
                level = None
                
                if level_number_global == 1: 
                    intro = None 
                    game_state = "intro"
                elif level_number_global > 1:
                    map = None
                    game_state = "map"  
                    
                    
        case "intro":  
 
            if intro == None:
                intro = IntroStory(screen) 
                continue

            if intro.update() or intro.update():
                map = None 
                title = None 
                intro4 = None
                intro6 = None
                end = None
                credit = None
                intro5 = None
                intro = None
                level = None
                game_state = "level"
                
        case "intro2":   

            if intro2 == None:
                intro2 = IntroChapter2(screen) 
                continue
 
            if intro2.update() or intro2.update():
                map = None 
                title = None 
                intro4 = None
                intro6 = None
                end = None
                intro = None
                intro2 = None
                intro5 = None
                level = None
                credit = None
                
                active_level = 7
                level_number_global = 7
                save(chapter_number_global, active_level, level_number_global)
                
                game_state = "level"
        case "intro3":  

            if intro3 == None:
                intro3 = IntroChapter3(screen) 
                continue
   
            if intro3.update() or intro3.update():
                map = None 
                title = None 
                
                intro = None
                intro5 = None
                intro6 = None
                intro2 = None
                end = None
                credit = None
                intro3 = None
                intro4 = None
                level = None

                
                active_level = 13
                level_number_global = 13
                save(chapter_number_global, active_level, level_number_global)
                
                game_state = "level"

        case "intro4":  

            if intro4 == None:
                intro4 = IntroChapter4(screen) 
                continue
   
            if intro4.update() or intro4.update():
                map = None 
                title = None 
                
                intro = None
                intro2 = None
                credit = None
                intro3 = None
                end = None
                intro5 = None
                intro4 = None
                intro6 = None
                level = None

                
                active_level = 19
                level_number_global = 19
                save(chapter_number_global, active_level, level_number_global)
                
                game_state = "level"   
        
        case "intro5":  

            if intro5 == None:
                intro5 = IntroChapter5(screen) 
                continue
   
            if intro5.update() or intro5.update():
                map = None 
                title = None 
                
                intro = None
                intro2 = None
                intro3 = None
                end = None
                credit = None
                intro5 = None
                intro6 = None  
                intro4 = None
                level = None  

                
                active_level = 25
                level_number_global = 25
                save(chapter_number_global, active_level, level_number_global)
                
                game_state = "level"   
        
        case "controll":
            if controll == None:
                controll = ControllsMenu(screen)
                continue 

            #controll = None
            map = None

            if controll.update() or controll.update():
                map = None
                controll = None
                game_state = "map"
                
                
                
        case "intro6":  

            if intro6 == None:
                intro6 = IntroChapter6(screen) 
                continue
   
            if intro6.update() or intro6.update():
                map = None 
                title = None 
                
                intro = None
                credit = None
                intro2 = None
                intro3 = None
                intro5 = None
                intro6 = None
                end = None 
                intro4 = None
                level = None
 
                
                active_level = 31
                level_number_global = 31
                save(chapter_number_global, active_level, level_number_global)
                
                game_state = "level"   
    
        case "ending":  

            if end == None:
                end = Ending(screen) 
                continue
   
            if end.update() or end.update():
                map = None 
                title = None 
                
                intro = None
                intro2 = None
                credit = None
                intro3 = None
                intro5 = None
                intro6 = None
                end = None 
                intro4 = None
                level = None
 
              
                
                game_state = "credits"   
        case "credits":  

            if credit == None:
                credit = Credits(screen) 
                continue

            credit.draw()
   
            if credit.update() or credit.update():
                map = None 
                title = None 
                
                intro = None
                intro2 = None
                credit = None
                intro3 = None
                intro5 = None
                intro6 = None
                end = None 
                intro4 = None
                level = None
                credit = None
 
                active_level = 33
                level_number_global = 33
                save(chapter_number_global, active_level, level_number_global) 

                screen.fill((255, 255, 255))
                
                game_state = "" 
                
        
                #END OF GAME!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    #print(int(clock.get_fps())) 
    clock.tick(60)     #dont copy and paste  
    pygame.display.flip()
     

pygame.display.quit()        