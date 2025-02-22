import pygame
import os
from constants import *
from important import *
from entities.cutscene_manager import *

img1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/cutscenes/intro2/1.png"))
img2 = pygame.image.load(os.path.join(GAME_PATH, "sprites/cutscenes/intro2/2.png"))
img3 = pygame.image.load(os.path.join(GAME_PATH, "sprites/cutscenes/intro2/3.png"))
img4 = pygame.image.load(os.path.join(GAME_PATH, "sprites/cutscenes/intro2/4.png"))
img5 = pygame.image.load(os.path.join(GAME_PATH, "sprites/cutscenes/intro2/5.png"))
img6 = pygame.image.load(os.path.join(GAME_PATH, "sprites/cutscenes/intro2/6.png"))
 
chapter = pygame.image.load(os.path.join(GAME_PATH, "sprites/chapter_art/ch2/img.png"))
class IntroChapter2:
    def __init__(self, screen):
        self.screen = screen
        
        self.chapter = chapter
        self.timer = 0
        self.imgs = []
        self.img_val = 0
        self.imgs.append(img1)
        self.imgs.append(img2)
        self.imgs.append(img3)
        self.imgs.append(img4)
        self.imgs.append(img5)
        self.imgs.append(img6)
        
        self.cutscene = []
        self.cutscene.append(CutsceneManager(100, pygame.Vector2(0, 0)))
        
        self.mscmgr = MusicManager(INTRO, True)
        self.mscmgr.play() 
        self.ch = True
        
    def draw(self):
        keys = pygame.key.get_pressed()
        
        if self.ch:
            self.screen.blit(self.imgs[self.img_val], (0, 0))
        
        
    def update(self):
        self.draw()
        keys = pygame.key.get_pressed()
        
        if not self.ch:
            self.screen.blit(self.chapter, (0, 0))
            
            if keys[KEY_JUMP] and self.timer >= 120:
                return True
            self.timer += 1
        for cutscene in self.cutscene:
            update_rect = pygame.Rect(cutscene.pos.x, cutscene.pos.y, 128, 1000)
            if update_rect.x >= 1500:
                continue
            
            self.img_val = cutscene.indiv_index 
            
            
            if cutscene.cutscene_started == True and cutscene.active:
                self.mscmgr.stop()
                #self.mscmgr.play()
                self.mscmgr = MusicManager(os.path.join(GAME_PATH, cutscene.music), True)
                self.mscmgr.play()
                cutscene.cutscene_started = False   
            
            if cutscene.cutscene_started == False and cutscene.active == False and cutscene.cutscene_finished == False:
                self.mscmgr.stop()
                #self.mscmgr.play()
                self.mscmgr = MusicManager(os.path.join(GAME_PATH, cutscene.musicend), True)
                self.mscmgr.play()
                cutscene.cutscene_finished = True  
            
            cutscene.actor_entity() #position is the one on the map
            delete = cutscene.update(pygame.rect.Rect(0, 0, 128, 1000), update_rect, self.screen)
            
            if delete:
                update_rect.y = 10000
                cutscene.started = False 
            #if cutscene.active:
            #    self.player.can_move = False
            #else:
            #    self.player.can_move = True
            if cutscene.cutscene_started == False and cutscene.active == False and cutscene.cutscene_finished == False:
                self.ch = False
                
                
                
        return False