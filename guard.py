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
def on_guard(x,y,field):
    if 0 <= y < len(field) and 0 <= x < len(field[y]):
        if field[y][x] == "guard":
            return True
    return False
# ---------------------------------------------------------------------------------------------------------------
def move_gurad_back(x):
    x -= consts.pixel
    return x

def move_gurad_matrix_back(field):

    for col in range(consts.matriz_rows):
        if not to_left and field[y][col] == "guard":
            field[y][col] = "x"
            field[y][col - 1] = "guard"
        elif to_left and field[y][col] == "guard":
            field[y][col] = "x"
            field[y][col + 1] = "guard"
        else:
            field = field
    return field
#---------------------------------------------------------------------------------------------------------------------------------------
def move_gurad(x):
    x+=consts.pixel
    return x

def move_gurad_matrix(field):

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
