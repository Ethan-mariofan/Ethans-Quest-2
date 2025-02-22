import pygame
import os

pygame.init()
screen = pygame.display.set_mode((1000, 1000))

#CONSTANTS
GAME_PATH = os.getcwd()
COVE1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/tiles/cove/1.png"))
COVE2 = pygame.image.load(os.path.join(GAME_PATH, "sprites/tiles/cove/2.png"))
COVE3 = pygame.image.load(os.path.join(GAME_PATH, "sprites/tiles/cove/3.png"))
COVE4 = pygame.image.load(os.path.join(GAME_PATH, "sprites/tiles/cove/4.png"))
COVE5 = pygame.image.load(os.path.join(GAME_PATH, "sprites/tiles/cove/5.png"))
COVE6 = pygame.image.load(os.path.join(GAME_PATH, "sprites/tiles/cove/6.png"))
COVE7 = pygame.image.load(os.path.join(GAME_PATH, "sprites/tiles/cove/7.png"))
COVE8 = pygame.image.load(os.path.join(GAME_PATH, "sprites/tiles/cove/8.png"))
COVE9 = pygame.image.load(os.path.join(GAME_PATH, "sprites/tiles/cove/9.png"))
COVEA = pygame.image.load(os.path.join(GAME_PATH, "sprites/tiles/cove/10.png"))
COVEB = pygame.image.load(os.path.join(GAME_PATH, "sprites/tiles/cove/11.png"))
COVEC = pygame.image.load(os.path.join(GAME_PATH, "sprites/tiles/cove/12.png"))
COVED = pygame.image.load(os.path.join(GAME_PATH, "sprites/tiles/cove/13.png"))
COVEE = pygame.image.load(os.path.join(GAME_PATH, "sprites/tiles/cove/14.png"))
COVEDE = pygame.image.load(os.path.join(GAME_PATH, "sprites/tiles/cove/deco2.png"))
COVEDE1 = pygame.image.load(os.path.join(GAME_PATH, "sprites/tiles/cove/deco1.png"))


  
level_num = 1 #level 1

class LvlGen:
    def __init__(self, level_num):
        self.level_num = level_num
    def level_generate(self):
        file_name = 'levels/level' + str(self.level_num) + '.txt'
        with open(os.path.join(GAME_PATH, file_name)) as f:
            lines = f.readlines()

            #tiles.clear() 
            for y, row in enumerate(lines): 
                for x, item in enumerate(row):
                    item = item.strip()

                    coordinate = pygame.Vector2(x * 128, y * 128)
                    match item:
                        case "1":
                            screen.blit(COVE1, (coordinate.x, coordinate.y))
                        case "2":
                            screen.blit(COVE2, (coordinate.x, coordinate.y))
                        case "3":
                            screen.blit(COVE3, (coordinate.x, coordinate.y))
                        case "4":
                            screen.blit(COVE4, (coordinate.x, coordinate.y))
                        case "5":
                            screen.blit(COVE5, (coordinate.x, coordinate.y))
                        case "6":
                            screen.blit(COVE6, (coordinate.x, coordinate.y))
                        case "7":
                            screen.blit(COVE7, (coordinate.x, coordinate.y))
                        case "8":
                            screen.blit(COVE8, (coordinate.x, coordinate.y))
                        case "9":
                            screen.blit(COVE9, (coordinate.x, coordinate.y))
                        case "A":
                            screen.blit(COVEA, (coordinate.x, coordinate.y))
                        case "B":
                            screen.blit(COVEB, (coordinate.x, coordinate.y))
                        case "C":
                            screen.blit(COVEC, (coordinate.x, coordinate.y))
                        case "D":
                            screen.blit(COVED, (coordinate.x, coordinate.y))
                        case "E":
                            screen.blit(COVEE, (coordinate.x, coordinate.y))
                        case "d":
                            screen.blit(COVEDE1, (coordinate.x, coordinate.y))
                        case "e":
                            screen.blit(COVEDE, (coordinate.x, coordinate.y))  
level = LvlGen(level_num)

  

 
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill((255, 255, 255))
    
    level.level_generate()

    
    pygame.display.flip()
    clock.tick(60)  

pygame.quit()



class EthanPlayer:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.img = []
        for i in range(0, 10):
            self.img.append(pygame.image.load(os.path.join(GAME_PATH, "sprites/player/idle1.png")))
        for i in range(0, 10):
            self.img.append(pygame.image.load(os.path.join(GAME_PATH, "sprites/player/idle2.png")))
        for i in range(0, 10):
            self.img.append(pygame.image.load(os.path.join(GAME_PATH, "sprites/player/idle3.png")))
       
        self.type = "idle"
        self.img_val = 0 
    
        self.is_grounded = False
        self.force = 0
        
        self.rect = pygame.Rect(self.x, self.y, 128, 256)
    
    def switch_images(self):
        if self.type == "idle":
            self.img.clear()
            for i in range(0, 10):
                self.img.append(pygame.image.load(os.path.join(GAME_PATH, "sprites/player/idle1.png")))
            for i in range(0, 10):
                self.img.append(pygame.image.load(os.path.join(GAME_PATH, "sprites/player/idle2.png")))
            for i in range(0, 10):
                self.img.append(pygame.image.load(os.path.join(GAME_PATH, "sprites/player/idle3.png")))
            
        if self.type == "walk":
            self.img.clear()
            for i in range(0, 10):
                self.img.append(pygame.image.load(os.path.join(GAME_PATH, "sprites/player/walk1.png")))
            for i in range(0, 10):
                self.img.append(pygame.image.load(os.path.join(GAME_PATH, "sprites/player/walk2.png")))
            for i in range(0, 10):
                self.img.append(pygame.image.load(os.path.join(GAME_PATH, "sprites/player/walk3.png")))
            for i in range(0, 10):
                self.img.append(pygame.image.load(os.path.join(GAME_PATH, "sprites/player/walk4.png")))
            for i in range(0, 10):
                self.img.append(pygame.image.load(os.path.join(GAME_PATH, "sprites/player/walk5.png")))
            for i in range(0, 10): 
                self.img.append(pygame.image.load(os.path.join(GAME_PATH, "sprites/player/walk6.png")))  
        if self.type == "jump":
            self.img.clear()
            for i in range(0, 10):
                self.img.append(pygame.image.load(os.path.join(GAME_PATH, "sprites/player/jump1.png")))
            for i in range(0, 10):
                self.img.append(pygame.image.load(os.path.join(GAME_PATH, "sprites/player/jump2.png")))
            for i in range(0, 10):
                self.img.append(pygame.image.load(os.path.join(GAME_PATH, "sprites/player/jump3.png")))       
                
                
                
    def draw(self, screen):
        self.img_val += 1
        if self.img_val >= len(self.img):
            self.img_val = 0
        return pygame.transform.scale(self.img[self.img_val], (128, 256))  
    
    def movement(self): 
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            self.x += 5
            self.type = "walk"
            
        elif keys[pygame.K_LEFT]:
            self.x -= 5 
            self.type = "walk"
            
        else:
            self.type = "idle"
    
    def gravity(self, tile_rect):
        keys = pygame.key.get_pressed()
        
        
        self.y += self.force 
        
        if keys[pygame.K_SPACE] and self.is_grounded == True:
            self.force = -10
            #sounds and effects come in later
            self.is_grounded = False
        if self.is_grounded == False:
            self.force = 4
        else:
            self.force = 0
        
        if self.touch_tile(tile_rect) == True:
            self.is_grounded = True
             
              
    def touch_tile(self, tile_rect):
        if self.rect.left == tile_rect.right and tile_rect.bottom + 1 == self.rect.bottom: #left
            #if tile_rect.bottom + 1 == player_rect.bottom:
            #    self.move_dir = True
            return True

        elif self.rect.right == tile_rect.left and tile_rect.bottom + 1 == self.rect.bottom: #right
            return True
        
        if self.rect.colliderect(tile_rect):
            return True
        
        else:
            return None  