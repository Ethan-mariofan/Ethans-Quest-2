import pygame 
import os
from constants import *
from music_manager import *
#sprites/menus/credits/

credits_text = {
                "100" : "code:",
                "150" : "Ethan Mallie",
                "200" : "Marcus",
                "250" : "Pygame Team",
                "300" : "James", 
                "350" : "",
                "400" : "Sprites:",
                "450" : "Ethan Mallie",
                "500" : "",
                "550" : "Story:",
                "600" : "Ethan Mallie",    
                "650" : "",   
                "700" : "Music/Sounds:",
                "750" : "Ethan Mallie",
                "800" : "Nintendo", 
                "850" : "SMBX2 Team",
                "900" : "Donkey Kong Team",    
                "950" : "",   
                "1000" : "Beta Testing:",
                "1050" : "Ethan Mallie",
                "1100" : "Marcus",
                "1150" : "",
                "1200" : "Characters:",
                "1250" : "Nintendo",
                "1300" : "Ethan Mallie",
                "1350" : "",
                "1400" : "",
                "1450" : "",
                "1500" : "Thanks For Playing!!!"
                }
  

bg = pygame.image.load(os.path.join(GAME_PATH, "sprites/menus/credits/bg_credits.png"))
class Credits:
    def __init__(self, screen):
        self.screen = screen 

        self.bg = bg
        self.credits_text = credits_text

        self.text_x = 500
        self.text_y = []
        
        
        
        self.music = MusicManager(ENDING, False)
        self.music.play()
        
        self.position = pygame.Vector2(500, 500)
        
        self.end = False

        self.ico_ethan = pygame.image.load(os.path.join(GAME_PATH, "sprites/menus/credits/ethan.png"))
        self.ico_marcus = pygame.image.load(os.path.join(GAME_PATH, "sprites/menus/credits/anti_copy_and_paste_marcus.png"))
        self.ico_james = pygame.image.load(os.path.join(GAME_PATH, "sprites/menus/credits/james.png"))

        self.timer = 0
    def world_to_screen(self, world_coordinate: pygame.Vector2) -> pygame.Vector2:
        return world_coordinate - self.position + SCREEN_CENTER  
     
    def draw(self):
        self.screen.blit(self.bg, (0, 0))  
 
        for i in self.credits_text: 
            blah = int(i)
            self.position.y += 0.05
            
             
            draw_text(self.credits_text[i], (0, 0, 0), self.world_to_screen(pygame.Vector2(self.text_x, blah)), self.screen) 

            #int(self.text_y.index(i)) -= 2    
            
               
            if self.position.y >= 2100: #change this if incorrect
                self.end = True 
         
    def update(self):
         
        self.timer += 1 

        if self.timer >= 60 and self.timer < 150: 
            self.screen.blit(self.ico_ethan, self.world_to_screen(pygame.Vector2(100, 500)))
        if self.timer >= 150 and self.timer < 280:
            self.screen.blit(self.ico_marcus, self.world_to_screen(pygame.Vector2(100, 600)))
        if self.timer >= 280 and self.timer < 390:
            self.screen.blit(self.ico_james, self.world_to_screen(pygame.Vector2(100, 700)))

        if self.end:
            return True
        return False