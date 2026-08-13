import pygame
import consts
import game_field
import solider
<<<<<<< HEAD
#---------------------------------------------------------------------------------------------------------------------------------------
=======

>>>>>>> bcb2d4064f2e2dba79ba3df39732cbcbb81af0c6
state = {
    "is_mine_fired": False,
    "is_window_open": True,
    "state": consts.RUNNING_STATE,
    "is_flag_captured": False,
    "is_Xray_on":False
}
def handle_user_events():
    for event in pygame.event.get():
<<<<<<< HEAD
=======

>>>>>>> bcb2d4064f2e2dba79ba3df39732cbcbb81af0c6
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
<<<<<<< HEAD
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

#---------------------------------------------------------------------------------------------------------------------------------------
allgame_run=False
=======

allgame_run=False

>>>>>>> bcb2d4064f2e2dba79ba3df39732cbcbb81af0c6
while allgame_run!=True:
    pygame.init()
    game_field.create()
    solider.create()
    while state["is_window_open"]:
        handle_user_events()
<<<<<<< HEAD
#---------------------------------------------------------------------------------------------------------------------------------------
import pathfinding
# def   find_path():
#     init_find  # (re)set global values and open list
#     check_neighbors  # for every node in open list
#     next_node  # closest node to start in open list
#     find_neighbors  # get neighbors
#     process_node  # calculate new cost for neighboring node
=======


>>>>>>> bcb2d4064f2e2dba79ba3df39732cbcbb81af0c6
