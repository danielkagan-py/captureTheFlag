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