import game_field
import pygame
import consts
#---------------------------------------------------------------------------------------------------------------------------------------
MINE_IMG = "pics/mine.png"
field1 = game_field.create_Xray_field()
screen1 = pygame.display.set_mode((consts.screen_w, consts.screen_h))
#---------------------------------------------------------------------------------------------------------------------------------------
def show_mines():
   screen1.fill(consts.black)
   mainLoop = True
   while mainLoop:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               mainLoop = False
           i = 0
           for col in range (0,consts.COL):
               for row in range (0,consts.ROWS):
                   pygame.draw.line(screen1, consts.green, (0 + i, 0 ), ( 0 +i,999999 ))
                   pygame.draw.line(screen1, consts.green, (0 , 0 + i), ( 99999 , 0 + i))
                   if field1[row][col] == "mine":
                       screen1.blit(pygame.transform.smoothscale(consts.mine, (28, 28)), ((col * 28), (row * 28))) , (1400 , 700)
                   i += 28
       pygame.display.update()
   return screen1
   pygame.quit()
#---------------------------------------------------------------------------------------------------------------------------------------
field = game_field.create_regular_field()
screen = pygame.display.set_mode((consts.screen_w, consts.screen_h))
def show_screen():
    screen.fill(consts.green)
    for y in range(len(field)):
        for x in range(len(field[y])):
            if field[y][x] == "grass":
                screen.blit(pygame.transform.smoothscale(consts.grass, (40, 40)), (y*40 , x*20 ))
    pygame.display.update()
    return screen
#---------------------------------------------------------------------------------------------------------------------------------------
# show_screen()
# show_mines()