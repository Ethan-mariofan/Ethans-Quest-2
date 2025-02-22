import pygame

import os
from constants import *

pygame.mixer.init()

#THIS IS FOR THE MUSIC MANAGER 
class MusicManager:
    def __init__(self, track, is_lvl_msc):
        self.track = track 
        self.is_lvl_msc = is_lvl_msc #if true its level music if false it is cutscene music 
    
    def play(self):
        pygame.mixer.music.load(self.track)
        pygame.mixer.music.play(-1)
    
    def stop(self):
        pygame.mixer.music.stop()
        
          