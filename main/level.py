import os   
import pygame
from constants import *
from entities.player import * 
from entities.coin import *
from entities.goomba import * 
from background import *
from entities.platform import * 
from entities.hearts_powerup import *
from music_manager import *
from entities.checkpoint import *
from entities.star import *
from pause_menu import *
from entities.cutscene_manager import *
from entities.spiky_guy import *
from entities.effect import *
from entities.ruins_master import * 
from entities.starly_boss import *
from entities.robber import *
from entities.bumpy import *
from entities.starly_igloo import *
from entities.spark_join import *
from entities.phantom_boss import *
from entities.fireball import *
from entities.faller import *
import random
from entities.chest import *
from entities.lava import *
import entities.stargrandlava as wearelava
from entities.final_boss import *


coin_and_lives = pygame.image.load(os.path.join(GAME_PATH, "sprites/hud/lives_and_coins.png"))
heart_full = pygame.image.load(os.path.join(GAME_PATH, "sprites/hud/heart.png"))
heart_empty = pygame.image.load(os.path.join(GAME_PATH, "sprites/hud/heart_empty.png"))
 
 

class Tile:  
    def __init__(self, type, pos): 
        self.type = type 
        self.pos = pos
        self.x = pos.x
        self.y = pos.y
          
 

empty_char = ["`", "p", "/", "c", "G", "P", "h", "+", "-", "z", "s", "Z", "o", "L", "l", "q", "Q", "S", "a", "b"] #capital P is platform  z is cutscene
decoration_char = ["g", "f"]

  
tile_imgs = {}

def world_to_screen(world_coordinate: pygame.Vector2) -> pygame.Vector2:
    return world_coordinate - CAMERA_POSITION + SCREEN_CENTER  

def load_entities(lvl_num):
    file_name = 'levels/level' + str(lvl_num) + '.txt'

    entities = [] 
    platforms = []
    cutscenes = []
    cutscene_to_enemy_ruins_master = []
    bosses = []
    spark = []
 
    with open(os.path.join(GAME_PATH, file_name)) as f:
        lines = f.readlines()
        lava = []
        lava_star = []
        for y, row in enumerate(lines): 
            for x, item in enumerate(row):
                item = item.strip()
 
                coordinate = pygame.Vector2(x * 128, y * 128)

                if item == "p":
                    entities.append(Player(coordinate))
                if item == "/":
                    boundery = coordinate
                if item == "c":
                    entities.append(Coin(coordinate))
                if item == "G":
                    if lvl_num >= 19 and lvl_num <= 24:
                        entities.append(Goomba(coordinate, "pumpkin"))
                    else:
                        entities.append(Goomba(coordinate, "blue"))
                if item == "P":
                    if lvl_num == 21:
                        platforms.append(Platform(coordinate, "bounce", "sprites/objs/platforms/platform_pumpkinalt.png"))
                    else:
                        platforms.append(Platform(coordinate, "bounce", "sprites/objs/platforms/platform_cove.png"))
                if item == "h":
                    entities.append(Heart(coordinate)) 
                if item == "+":
                    entities.append(CheckPoint(coordinate))
                if item == "-": 
                    if lvl_num == 30:
                        lava_star = coordinate
                        lava = wearelava.StarEndLevelGrand(lava_star)
                        
                    else:
                        entities.append(StarEndLevel(coordinate, lvl_num))
                if item == "z":
                    cutscenes.append(CutsceneManager(lvl_num, coordinate)) #LEVEL NUM IS CUTSCENE ID 
                if item == "s":
                    entities.append(SpikyGuy(coordinate))
                if item == "Z":
                    cutscene_to_enemy_ruins_master.append(RuinsMaster(coordinate))
                if item == "o":
                    if lvl_num >= 7 and lvl_num <= 11:
                        platforms.append(Platform(coordinate, "horizontal", "sprites/objs/platforms/platform_sun.png"))
                    elif lvl_num == 17:
                        platforms.append(Platform(coordinate, "horizontal", "sprites/objs/platforms/platform_snow.png"))
                    elif lvl_num == 20:
                        platforms.append(Platform(coordinate, "horizontal", "sprites/objs/platforms/platform_pumpkin.png"))
                    elif lvl_num == 28:
                        entities.append(Faller(coordinate))
                    else:
                        platforms.append(Platform(coordinate, "horizontal", "sprites/objs/platforms/platform_cove.png"))
                    
                if item == "L":
                    bosses.append(BossStarly(coordinate))
                if item == "l":
                    entities.append(Goomba(coordinate, "brown"))
                if item == "q": 
                    bosses.append(BossRobber(coordinate)) 
                if item == "Q":
                    if lvl_num == 33:
                        bosses.append(FinalBoss(coordinate))
                        
                    
                    elif lvl_num == 18:
                        bosses.append(StarlyBossIgloo(coordinate))
                    elif lvl_num == 24:
                        bosses.append(Phantom(coordinate))
                    else:
                        entities.append(Bumpy(coordinate))
                        
                if item == "S":
                    spark.append(Spark(coordinate))

                if item == "a":
                    if lvl_num == 30:
                        entities.append(LavaFlow(pygame.Vector2(CAMERA_POSITION.x - 500, 1000 - 100))) #LAVA STUFF
                    else:
                        entities.append(FireBall(coordinate))
                if item == "b":
                    if lvl_num == 30:
                        entities.append(LavaFall(pygame.Vector2(coordinate.x, -100))) #LAVA STUFF
                    else:
                        entities.append(Chest(coordinate, cutscenes[0]))
                    
                    
                
    return (entities, boundery, platforms, cutscenes, cutscene_to_enemy_ruins_master, bosses, spark, lava, lava_star)

def load_backgrounds(tile_set):
    folder_dir = os.path.join(GAME_PATH, f"sprites/bg/{tile_set}")

    backgrounds = []

    for image in os.listdir(folder_dir):
 
        backgrounds.append(Background(pygame.image.load(os.path.join(GAME_PATH, f"sprites/bg/{tile_set}/{image}")).convert_alpha(), float(image.replace(".png", "").replace("_", ".")), 0))
        backgrounds.append(Background(pygame.image.load(os.path.join(GAME_PATH, f"sprites/bg/{tile_set}/{image}")).convert_alpha(), float(image.replace(".png", "").replace("_", ".")), -1000))
        backgrounds.append(Background(pygame.image.load(os.path.join(GAME_PATH, f"sprites/bg/{tile_set}/{image}")).convert_alpha(), float(image.replace(".png", "").replace("_", ".")), 1000))
    
    return backgrounds
        

 

def load_level(lvl_num, tile_set, previous_tileset):  
    file_name = 'levels/level' + str(lvl_num) + '.txt'
  

    tiles = [] 
    decor = []

    if tile_set != previous_tileset:
        tile_imgs.clear()

    previous_tileset = tile_set
    
    with open(os.path.join(GAME_PATH, file_name)) as f:
        lines = f.readlines()
         
        for y, row in enumerate(lines): 
            for x, item in enumerate(row):
                item = item.strip()

                coordinate = pygame.Vector2(x * 128, y * 128)

                if not item or item in empty_char:
                    continue

                if item in tile_imgs.keys():
                    if item in decoration_char:
                        decor.append(Tile(tile_imgs[item], coordinate))
                        continue
                    tiles.append(Tile(tile_imgs[item], coordinate)) 
                    continue

                tile_imgs.update({item : pygame.image.load(os.path.join(GAME_PATH, f"sprites/tiles/{tile_set}/{item}.png"))})

                #decoration chars 
                if item in decoration_char:
                    decor.append(Tile(tile_imgs[item], coordinate))
                    continue
                tiles.append(Tile(tile_imgs[item], coordinate))

    return (tiles,decor)
  

class Level:
    def __init__(self, screen, level_num, tile_set, background_set, music_track, effect, autoscroll, ch): 
        self.screen = screen
        self.level_num = level_num
        self.tile_set = tile_set
        self.music_track = music_track
        self.ch_num = ch
        CAMERA_POSITION.x = 500
        CAMERA_POSITION.y = 475
        
        
        

        self.is_auto_scroll = autoscroll
        #self.cooldown = 2
        self.effects = Effect(self.screen, pygame.image.load(os.path.join(GAME_PATH, effect)).convert_alpha())
        
        self.mscmgr = MusicManager(self.music_track, True)
        self.mscmgr.play() 
        self.pauses = False
        
        self.pause = PauseMenu(self.screen, self.pauses, pygame.image.load(os.path.join(GAME_PATH, "sprites/menus/pause/buttons.png")), "map")
        
        self.a = self.pause.a 
        
        self.previous_tileset = ""

        self.gameover_text = random.randint(0, 50)

        level_loaded = load_level(level_num, tile_set, self.previous_tileset)
        entities_loaded = load_entities(self.level_num)
 

        self.backgrounds = load_backgrounds(background_set)

        self.tile_rects = []
        self.tiles = level_loaded[0]
        self.decor = level_loaded[1]
        self.entities = entities_loaded[0]
        self.lava = entities_loaded[7]

        self.player = self.entities[0] 
        self.entities.pop(0)

        self.boundry = entities_loaded[1]

        self.platforms = entities_loaded[2]
        
        self.cutscenes = entities_loaded[3]
        self.ruins_cutscene = entities_loaded[4]
        self.bosses = entities_loaded[5]
        self.spark = entities_loaded[6]
        
        self.lavastar = entities_loaded[8]
        
        self.lives = 5
        self.death_timer = 0
        self.star_timer = 0
        self.star_timer2 = 0



    def death(self): 
        self.player.switch_img("die")
        self.player.force = 0
        self.death_timer += 1 
        if self.death_timer < 100:
            self.player.pos.y -= 5

        else:
            self.player.pos.y += 10
        self.player.die = True

    def reset(self):
        has_checkpoint = self.player.checkpoint_gotton
        checkpoint_pos = self.player.checkpoint_pos
        start_checkpoint = self.player.checkpoint_start_pos

        #load level again reset
        level_loaded = load_level(self.level_num, self.tile_set, self.previous_tileset)
        entities_loaded = load_entities(self.level_num)
        
        self.player.switch_img("idle")
        self.tile_rects = []
        self.tiles = level_loaded[0] 
        self.decor = level_loaded[1]
        self.entities = entities_loaded[0]
        self.boundry = entities_loaded[1]

        self.platforms = entities_loaded[2]
        
        self.lava = entities_loaded[7]
        self.cutscenes = entities_loaded[3]
        
        self.ruins_cutscene = entities_loaded[4]
        self.bosses = entities_loaded[5]   
        self.spark = entities_loaded[6]  
        self.lavastar = entities_loaded[8]   

        self.player = self.entities[0]
        self.entities.pop(0)

        self.boundry = entities_loaded[1]
        self.player.can_move = True
        self.player.health = 3  
        CAMERA_POSITION.x = 500
        CAMERA_POSITION.y = 475 
        self.player.die = False
 
        if has_checkpoint: 
            self.player.pos.x = start_checkpoint.x
            self.player.pos.y = checkpoint_pos.y - 300
            CAMERA_POSITION.x = start_checkpoint.x
            CAMERA_POSITION.y = 475
            if self.level_num == 4:
                self.cutscenes[0].cutscene_finished = True 
            if self.level_num == 20:
                self.cutscenes[0].cutscene_finished = True 

    def draw_level(self): 
        
        
        self.tile_rects = []
        for tile in self.tiles:
            update_rect = pygame.Rect(world_to_screen(tile.pos), (128, 128))
               
            self.tile_rects.append(update_rect) 

            self.screen.blit(tile.type, update_rect.topleft)       

        for dec in self.decor: 
            update_rect = pygame.Rect(world_to_screen(dec.pos), (128, 128))
            self.screen.blit(dec.type, update_rect.topleft)

        updated_player_rect = pygame.Rect(world_to_screen(self.player.pos), self.player.rect_size)
        if not self.pause.is_paused:
            self.player.update(self.tile_rects, updated_player_rect)
        self.screen.blit(self.player.draw(), updated_player_rect.topleft)

        if updated_player_rect.y >= 1000: #death bounds  
            self.player.health = 0 

        for entity in self.entities:
            update_rect = pygame.Rect(world_to_screen(entity.pos), entity.rect_size)

            if self.level_num == 29 and self.cutscenes[0].indiv_index >= 5:
                entity.is_opened = True
            if update_rect.x >= 1500:
                continue 
            
            
            self.screen.blit(entity.draw(), update_rect.topleft)
            if self.pause.is_paused:
                continue
            if self.player.can_move == False:
                continue
                    
                    
            if self.level_num == 30:
                coordinate = pygame.Rect(world_to_screen(self.lavastar), (128, 128)) 
                fff = self.lava.update(self.tile_rects, coordinate, updated_player_rect, self.player, self.screen, self.pause)
                if fff == False:
                    self.screen.blit(self.lava.draw(), coordinate)
              
        
            delete = entity.update(self.tile_rects, update_rect, updated_player_rect, self.player)
            if delete:
                self.entities.remove(entity)
        
        for platform in self.platforms:
            update_rect = pygame.Rect(world_to_screen(platform.pos), (platform.rect_size))
            if update_rect.x >= 1500:
                continue

            delete = platform.update(self.tile_rects, update_rect, updated_player_rect, self.player)
            self.screen.blit(platform.draw(), update_rect.topleft)  
            if delete:
                self.platforms.remove(platform)
                
            #pygame.draw.rect(self.screen, (0,0,0), update_rect)
            #pygame.draw.rect(self.screen, (0,255, 0), pygame.Rect(updated_player_rect.x, updated_player_rect.y, updated_player_rect.width, updated_player_rect.height + 30))
                
        
 
        for ruins in self.ruins_cutscene:
            update_rect = pygame.Rect(world_to_screen(ruins.pos), ruins.rect_size)
            if update_rect.x >= 1500:
                continue
            
            if self.cutscenes[0].cutscene_finished == True: 
                self.screen.blit(ruins.draw(), update_rect.topleft)
                
            if self.pause.is_paused:
                continue
            if self.player.can_move == False:
                continue
            
            if not self.cutscenes[0].cutscene_finished: 
                continue
            
            ruins.update(self.tile_rects, update_rect, updated_player_rect, self.player)
        
        
        for boss in self.bosses:
            update_rect = pygame.Rect(world_to_screen(boss.pos), boss.rect_size)

            if update_rect.x >= 1500:
                continue
            
            self.screen.blit(boss.draw(), update_rect.topleft)
            if self.pause.is_paused:
                continue
            if self.player.can_move == False: 
                continue 
            if not self.cutscenes[0].cutscene_finished: 
                continue
            delete = boss.update(self.tile_rects, update_rect, updated_player_rect, self.player, self.screen, self.pause)
            
                
        for spk in self.spark:
            update_rect = pygame.Rect(world_to_screen(spk.pos), spk.rect_size)
      
            if self.level_num == 20 and self.cutscenes[0].cutscene_finished: 
                
                self.screen.blit(spk.draw(), update_rect.topleft)
                
                if update_rect.x >= 1500:
                    continue
                if self.pause.is_paused:
                    continue
                spk.update(self.tile_rects, update_rect, updated_player_rect, self.player)

            if self.level_num >= 21:
                self.screen.blit(spk.draw(), update_rect.topleft)
                
                if update_rect.x >= 1500:
                    continue
                if self.pause.is_paused:
                    continue
                spk.update(self.tile_rects, update_rect, updated_player_rect, self.player)
 
        for cutscene in self.cutscenes:
            update_rect = pygame.Rect(world_to_screen(cutscene.pos), (128, 1000))
            if update_rect.x >= 1500:
                continue
            
            
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
            delete = cutscene.update(updated_player_rect, update_rect, self.screen)
            
            if delete:
                update_rect.y = 10000
                cutscene.started = False
            if cutscene.active:
                self.player.can_move = False
            else:
                self.player.can_move = True
    

        #AT THE END IS EEFECT
        self.effects.draw()
        if self.lives <= 0:
            self.screen.fill((0, 0, 0))

            
            if self.gameover_text == 5:
                draw_text("copy and paste", (255, 0, 0), pygame.Vector2(500, 500), self.screen)
            else:
                draw_text("Game Over", (255, 0, 0), pygame.Vector2(500, 500), self.screen)



    def movement(self):
        keys = pygame.key.get_pressed()
        if i >= 1:
            blah2 = controller.get_button(14)
            blah3 = controller.get_button(13)
        else:
            blah2 = keys[KEY_RIGHT]
            blah3 = keys[KEY_LEFT]
        
        
        player = self.player
        
        touchingtile = pygame.Rect(world_to_screen(self.player.pos), (128, 235)).collidelistall(self.tile_rects)
        #pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(world_to_screen(self.entities[0].pos), (128, 235)))

        if player.pos.x >= CAMERA_POSITION.x + 400:
            player.pos.x = CAMERA_POSITION.x + 400 
 
        if blah2 or blah3:  
            player.switch_img("walk")
        else:
            player.switch_img("idle") 

        #if keys[KEY_RIGHT] and keys[KEY_LEFT]:
        #    player.force = 1  
        if self.is_auto_scroll == False:
            
            if blah2:
                if not touchingtile: 
                    player.speed_x += 1
                    if player.pos.x >= 500 and CAMERA_POSITION.x <= self.boundry.x:
                        CAMERA_POSITION.x += player.speed_x 
                        player.pos.x += player.speed_x  
                    else:
                        player.pos.x += player.speed_x
    
            elif blah3: 
                if not touchingtile and player.pos.x > 0:
                    player.speed_x -= 1
                    if CAMERA_POSITION.x >= 500 and player.pos.x <= self.boundry.x:
                        CAMERA_POSITION.x += player.speed_x
                        player.pos.x += player.speed_x 
                    else: 
                        player.pos.x += player.speed_x

            if abs(player.speed_x) <= 3:
                player.controlled_movement = False

            #print(player.controlled_movement, player.speed_x)

            if player.controlled_movement:
                if CAMERA_POSITION.x >= 500 and player.pos.x <= self.boundry.x:
                    CAMERA_POSITION.x += player.speed_x
                    player.pos.x += player.speed_x 
                else: 
                    player.pos.x += player.speed_x

        else:
            if CAMERA_POSITION.x <= self.boundry.x:
                CAMERA_POSITION.x += 3
            
                
            if blah2:
                if not touchingtile: 
                    player.speed_x += 1
                    
                    player.pos.x += player.speed_x
            elif blah3:
                if not touchingtile and player.pos.x > 0:
                    player.speed_x -= 1
                    
                        
                    player.pos.x += player.speed_x 
                
        
           
        if blah2:
            player.dir = 1
        elif blah3:
            player.dir = -1 

         

             

        if touchingtile:
            if player.pos.x >= 500 or CAMERA_POSITION.x >= 500 and CAMERA_POSITION.x <= self.boundry.x:
                CAMERA_POSITION.x += player.speed_x * -1.2
                player.pos.x += player.speed_x * -1.2
            else: 
                player.pos.x += player.speed_x * -1.2 
            player.speed_x = 0
        else:
            player.speed_x *= 0.85

    def draw_hud(self):
        self.screen.blit(coin_and_lives, (0,0))

        heart_x_pos = 500
        for i in range(3):
            self.screen.blit(heart_empty, (heart_x_pos, 25))
            heart_x_pos += 150

        heart_x_pos = 500
        for i in range(self.player.health):
            self.screen.blit(heart_full, (heart_x_pos, 25))
            heart_x_pos += 150

        draw_text(f"{self.player.coins}", (0, 0, 0), (260, 80), self.screen)
        draw_text(f"{self.lives}", (0, 0, 0), (230, 240), self.screen)


    def draw_background(self):
        for background in self.backgrounds:
            background.update(self.screen, self.player) 


    def update_pause(self):
        self.pause.draw()
        update_pause = self.pause.update()
        
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
            
            
                
            
        
        keys = pygame.key.get_pressed()
        
        if i >= 1:
            blah = controller.get_button(0)
        else:
            blah = keys[KEY_X]
       
        
        if blah:
            self.pause.is_paused = True     




        if update_pause == "map":
            return True
        

    def update(self):
        self.draw_background()
        self.draw_hud()   
        self.draw_level() 
        self.update_pause()
        
        #GRAND STAR
        if self.player.chapter_completed:
            self.star_timer2 += 1
            draw_text("Chapter Clear", (0, 0, 0), (SCREEN_CENTER.x, SCREEN_CENTER.y - 150), self.screen)
            if self.star_timer2 >= 60:
                self.mscmgr.stop()
                self.level_num += 1
                self.ch_num += 1
                
                return 2 #"chapter_completed"  
               

        if self.star_timer2 >= 1:
            return False
        #chapter end
        
        
        
          
        if self.player.completed_level:
            self.star_timer += 1
            draw_text("Level Clear", (0, 0, 0), (SCREEN_CENTER.x, SCREEN_CENTER.y - 150), self.screen)
            if self.star_timer >= 60:
                self.mscmgr.stop()
                
                return True
                #print(game_state) 
            

        if self.star_timer >= 1:
            return False


        if self.player.health <= 0:
             
            self.death() 

            if self.death_timer >= 200:
                self.lives -= 1
                self.reset()
                self.death_timer = 0

        if self.death_timer >= 1:
            return False
        
        
        if self.pause.is_paused:
            return False
        
        if not self.player.can_move:
            return False
        self.movement() 

        
        #I ADDED SOMETHING HERE
        if self.player.coins >= 100:
            self.lives += 1 
            self.player.coins = 0
            
    

        return False
        
         