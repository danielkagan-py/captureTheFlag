import time
from sys import flags

import pygame
from pygame.locals import *
import screen
import consts
import game_field
import solider

state = {
    "is_mine_fired": False,
    "is_window_open": True,
    "state": consts.RUNNING_STATE,
    "is_flag_captured": False,
    "is_Xray_on":False
}
def handle_user_events():
    pass
def is_lose():
    if solider.player_collusion_mine():
        allgame_run = False

    return allgame_run

def is_win():
    win = True
    if solider.player_collusion_flag():
        win = False
    return win




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
                run = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    state["is_Xray_on"]==True
                    window=screen.show_mines()
                    window = screen.show_screen()



                if event.key == pygame.K_LEFT:
                    if x>0:
                        x -= velocity
                        window = screen.show_screen()
                        print(x, y)
                    else:
                        print("no")

                if event.key == pygame.K_RIGHT:
                    if x<1320:
                        x += velocity
                        window = screen.show_screen()
                        print(x, y)
                    else:
                        print("no")

                if event.key == pygame.K_UP:
                    if y > 0:
                        y -= velocity
                        window = screen.show_screen()
                        print(x, y)
                    else:
                        print("no")
                if event.key == pygame.K_DOWN:
                    if y < 600:
                        y += velocity
                        window = screen.show_screen()
                        print(x, y)
                    else:
                        print("no")
        pygame.display.update()


main()

