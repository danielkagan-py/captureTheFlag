from sys import flags

import pygame
from matplotlib.pyplot import flag

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

def is_lose():
    if solider.player_collusion_mine():
        allgame_run = False

    return allgame_run

def is_win():
    win = True
    if solider.player_collusion_flag():
        win = False
    return win


allgame_run=False

while allgame_run != False:
    pygame.init()
    game_field.create()
    solider.create()
    while state["is_window_open"]:
        handle_user_events()

        is_lose()

        is_win()



