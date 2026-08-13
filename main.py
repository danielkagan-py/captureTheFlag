from sys import flags
import pygame
from pygame.locals import *
import screen
import consts
import game_field
import time
import solider
#---------------------------------------------------------------------------------------------------------------------------------------
state = {
    "is_mine_fired": False,
    "is_window_open": True,
    "state": consts.RUNNING_STATE,
    "is_flag_captured": False,
    "is_Xray_on":False
}
#---------------------------------------------------------------------------------------------------------------------------------------
def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
        if event.type == pygame.KEYDOWN:
            dr_y=1
        if event.type == pygame.KEYUP:
            dr_y=-1
        if event.type == pygame.KEYLEFT:
            dr_x=-1
        if event.type == pygame.KEYRIGHT:
            dr_x=1
        if event.type == pygame.K_KP_ENTER:
            state["is_Xray_on"] = True
#---------------------------------------------------------------------------------------------------------------------------------------
def is_lose():
    lost = False
    if solider.on_mine(): # אמור לקבל את לוח המשחק
        lost = True
    return lost
#---------------------------------------------------------------------------------------------------------------------------------------
def is_win(): #
    win = False
    if solider.got_flag(): # אמור לקבל את הX,Y ואת לוח המשחק
        win = True
    return win
#---------------------------------------------------------------------------------------------------------------------------------------
def main():
   window =screen.show_screen()
   pygame.display.set_caption('THE game')
   image = consts.player
   image = pygame.transform.scale(image, (90,90))
   imageflag = consts.flag
   imageflag = pygame.transform.scale(imageflag, (90, 90))
   velocity = 28
   x = 0
   y = 0
   clock = pygame.time.Clock()
   pygame.init()
   field = game_field.create_regular_field
   while state["is_window_open"]:
       clock.tick(60)
       window.blit(image, (x, y))
       window.blit(imageflag, (1300, 600))
       pygame.init()
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               quit()
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_RETURN:
                   state["is_Xray_on"] == True
                   clock.tick(1)
                   screen.show_mines()
                   time.sleep(1)
                   window = screen.show_screen()
               if event.key == pygame.K_LEFT:
                   if x > 0:
                       x -= velocity
                       window = screen.show_screen()
                       print(x, y)
                   else:
                       x=x
               if event.key == pygame.K_RIGHT:
                   if x<1320:
                       x += velocity
                       window = screen.show_screen()
                       print(x, y)
                   else:
                       x=x
               if event.key == pygame.K_UP:
                   if y > 0:
                       y -= velocity
                       window = screen.show_screen()
                       print(x, y)
                   else:
                       y=y
               if event.key == pygame.K_DOWN:
                   if y < 600:
                       y += velocity
                       window = screen.show_screen()
                       print(x, y)
                   else:
                       y=y
       pygame.display.update()
#---------------------------------------------------------------------------------------------------------------------------------------
main()
#---------------------------------------------------------------------------------------------------------------------------------------
import pathfinding
# def   find_path():
#     init_find  # (re)set global values and open list
#     check_neighbors  # for every node in open list
#     next_node  # closest node to start in open list
#     find_neighbors  # get neighbors
#     process_node  # calculate new cost for neighboring node