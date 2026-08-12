import pygame
import consts

MINE_IMG = "pics/mine.png"
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
show_mines()