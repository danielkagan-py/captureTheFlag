import time
from time import sleep

import pygame

import consts
import game_field
import screen
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
    if solider.on_mine(xray_field=game_field.create_Xray_field()):
        state["is_mine_fired"] = True
        allgame_run = False

    return allgame_run

def is_win():
    win = True
    if solider.got_flag():
        win = False
    return win


allgame_run=False

while allgame_run != False:
    pygame.init()
    game_field.create()
    solider.create()
    while state["is_window_open"]:
        handle_user_events()

        if state["is_Xray_on"] == True:
            screen.make_xray_screen()

        while solider.player_move(board=screen.show_screen_kores()):
            if solider.on_mine(xray_field=screen.make_xray_screen()):
                is_lose()

        if is_lose():
            pass

        if is_win():
            pass
