import pygame
import yaml
import os
from constants import *

   
  
  
with open(os.path.join(GAME_PATH, "save/save.yml"), 'r') as save_file:
    print("LOADED")
    data = yaml.full_load(save_file)  
        

level_number_global = data.get('level_number_global')
active_level = data.get('active_level')
chapter_number_global = data.get('chapter_number_global') 

def save(ch_num, aclvl, lvl):
    with open(os.path.join(GAME_PATH, "save/save.yml"), 'w') as file_sv:
        print("saved")
        #print(chapter_number_global, level_number_global)
        file_sv.write(f"level_number_global: {lvl}\nactive_level: {aclvl}\nchapter_number_global: {ch_num}")
  