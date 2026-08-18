import consts
import pygame
#---------------------------------------------------------------------------------------------------------------------------------------
guard_img = pygame.image.load("pics/soldier (2).png")
#---------------------------------------------------------------------------------------------------------------------------------------
guard = pygame.transform.scale(guard_img, ((consts.pixel * 2, consts.pixel * 4)))
y = (consts.matriz_rows // 2) + 1
to_left = False
#---------------------------------------------------------------------------------------------------------------------------------------
def add_guard(field):
    x = 0
    field[23][0] = "guard"
    return field
#---------------------------------------------------------------------------------------------------------------------------------------
def guard_out_of_board(playerX ):
    if playerX < 0 or playerX >49:
        return True
    else:
        return False
#---------------------------------------------------------------------------------------------------------------------------------------
def move_gurad(field):
    for col in range(consts.matriz_rows):
        if not to_left and field[y][col] == "guard" :
            field[y][col] = "x"
            field[y][col + 1] = "guard"
        elif to_left and field[y][col] == "guard":
            field[y][col] = "x"
            field[y][col - 1] = "guard"
        else:
            field = field
    return field
#---------------------------------------------------------------------------------------------------------------------------------------
def board_accident(reg_field , xray_field):
    crush = False
    for row in range(consts.matriz_rows):
        for col in range(consts.matriz_cols):
            if reg_field[row][col] == "guard" and xray_field[row][col] == "player":
                crush = True
    return crush