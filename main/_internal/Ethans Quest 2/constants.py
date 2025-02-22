import pygame
import os



pygame.init()
pygame.mixer.init()
 
 
#controller = None
 
#i = pygame.joystick.get_count()
i = pygame.joystick.get_count()

for l in range(0, pygame.joystick.get_count()):
    controller = pygame.joystick.Joystick(l)
    print(l)
  
 
cooldown = 2 

joystick = []

GAME_PATH = os.getcwd()
#print(i)

   


#JUMP CIRCLE
#X X
#Z SQUARE

 
KEY_RIGHT = pygame.K_RIGHT 
KEY_LEFT = pygame.K_LEFT 
KEY_JUMP = pygame.K_SPACE
KEY_UP = pygame.K_UP 
KEY_DOWN = pygame.K_DOWN 
KEY_X = pygame.K_x
KEY_Z = pygame.K_z



SCREEN_SIZE = pygame.Vector2(1000, 1000)
SCREEN_CENTER = SCREEN_SIZE * 0.5 
CAMERA_POSITION = pygame.Vector2()

DONT_COPY_AND_PASTE = True

FONT = pygame.font.Font(os.path.join(GAME_PATH, "fonts/nsmbu.ttf"), 80) #changed font to New Super Mario Bros U font

def draw_text(item, color, pos, screen):
    text = FONT.render(item, True, color) 
    text_rect = text.get_rect()
    text_rect.center = pos 
    screen.blit(text, text_rect)


#sounds
COIN_SND = pygame.mixer.Sound(os.path.join(GAME_PATH, "music/sounds/coin.ogg"))
PLAYER_JUMP_SND = pygame.mixer.Sound(os.path.join(GAME_PATH, "music/sounds/player-jump.ogg"))
ENEMY_DIE_SND = pygame.mixer.Sound(os.path.join(GAME_PATH, "music/sounds/enemy-die.ogg"))
GOT_STAR_SND = pygame.mixer.Sound(os.path.join(GAME_PATH, "music/sounds/got-star.ogg"))
POWER_UP_SND = pygame.mixer.Sound(os.path.join(GAME_PATH, "music/sounds/shell-hit.ogg"))

#MUSIC   
COAST_LINE = os.path.join(GAME_PATH, "music/CoastLine.wav")
COVE_RUINS = os.path.join(GAME_PATH, "music/CoveRuins.wav")
STARLY_ENCOUNTER = os.path.join(GAME_PATH, "music/encounter_with_starly.wav")
STARLY_BOSS = os.path.join(GAME_PATH, "music/starly_boss_fight.wav")
CHAPTER1_MAP = os.path.join(GAME_PATH, "music/chapter1_worldmap.wav")
TITLE = os.path.join(GAME_PATH, "music/title.wav")
INTRO = os.path.join(GAME_PATH, "music/intro.wav")
CHAPTER_BEGIN = os.path.join(GAME_PATH, "music/chapter-start.wav")
WESTERN_DESERT = os.path.join(GAME_PATH, "music/western.wav")
FACTORY = os.path.join(GAME_PATH, "music/factory.wav")
ROBBER = os.path.join(GAME_PATH, "music/robber.wav")
BOSS_ROBBER = os.path.join(GAME_PATH, "music/boss_robber.wav") 
SNOW = os.path.join(GAME_PATH, "music/snow.wav") 
PUMPKIN = os.path.join(GAME_PATH, "music/pumpkin.wav")
SPOOKY = os.path.join(GAME_PATH, "music/spooky.wav") 
SCARY = os.path.join(GAME_PATH, "music/ScaryThingsHappen.wav")
PHANTOM_BATTLE = os.path.join(GAME_PATH, "music/phantom.wav")
LAVA = os.path.join(GAME_PATH, "music/lava.wav")
CHASE = os.path.join(GAME_PATH, "music/run_away.wav")
DARK = os.path.join(GAME_PATH, "music/dark.wav")
WE_ARE_EVIL = os.path.join(GAME_PATH, "music/we_are_evil.wav")
ENDING = os.path.join(GAME_PATH, "music/ending.wav")