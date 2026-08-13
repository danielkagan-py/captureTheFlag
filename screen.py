<<<<<<< HEAD
import game_field
import pygame
import consts
#---------------------------------------------------------------------------------------------------------------------------------------
MINE_IMG = "pics/mine.png"
#---------------------------------------------------------------------------------------------------------------------------------------
def show_mines():
   screen = pygame.display.set_mode((consts.screen_w, consts.screen_h))
   screen.fill((consts.black))
   mainLoop = True
   while mainLoop:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               mainLoop = False
           i = 0
           for col in range (consts.COL):
               for row in range (consts.ROWS):
                   pygame.draw.line(screen, consts.green, (0 + i, 0 ), ( 0 +i,999999 ))
                   pygame.draw.line(screen, consts.green, (0 , 0 + i), ( 99999 , 0 + i))
                   i += 28
       pygame.display.update()
   pygame.quit()
#---------------------------------------------------------------------------------------------------------------------------------------
def show_screen():
    screen = pygame.display.set_mode((consts.screen_w, consts.screen_h))
    screen.fill((consts.green))
    mainLoop = True
    count=0
    field = game_field.create_regular_field()
    for y in range(len(field)):
        for x in range(len(field[y])):
            if field[y][x] == "grass":
                count += 1
                screen.blit(pygame.transform.smoothscale(consts.grass, (40, 40)), (y*40 , x*20 ))
    while mainLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainLoop = False
        pygame.display.update()
    pygame.quit()
#---------------------------------------------------------------------------------------------------------------------------------------
show_screen()
show_mines()
=======
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import pygame
import consts
import random





def show_screen_kores():
    screen = pygame.display.set_mode((consts.w, consts.h))
    screen.fill((consts.green))
    screen.fill((consts.green))
    pygame.display.flip()

def make_xray_screen():
    print("a")




#---------------------------------------------------------







mtrx_bush = []
def create_random_bushe():
    count = 0
    for row in range(consts.ROWS):
        temp = []
        for col in range(consts.COL):
            is_bush = random.randint(0, 1)
            if count < 20:
                temp.append(is_bush)
            if is_bush == 0:
                count += 1
        mtrx_bush.append(is_bush)
    return mtrx_bush
def display():
    while True:
        surface = pygame.display.set_mode((consts.WINDOW_HEIGHT,consts.WINDOW_WIDTH))
        surface.fill(consts.GREEN)
        for row in mtrx_bush:
            for cell in row:
                if cell == 0 :
                    img = Image.open('pics/flag.png')
                    res = img.resize((14, 15))
                    randomH = random.randrange(0,consts.WINDOW_HEIGHT)
                    randomW = random.randrange(0 ,consts.WINDOW_WIDTH)
                    res.show(randomH,randomW)
        pygame.display.flip()
if __name__ == "__main__":
     display()



>>>>>>> bcb2d4064f2e2dba79ba3df39732cbcbb81af0c6
