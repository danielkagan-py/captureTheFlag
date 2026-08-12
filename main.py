import pygame
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

allgame_run=False

while allgame_run!=True:
    pygame.init()
    game_field.create()
    solider.create()
    while state["is_window_open"]:
        handle_user_events()


