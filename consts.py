import pygame
#---------------------------------------------------------------------------------------------------------------------------------------
matriz_rows=25
matriz_cols=50
ROWS = 25
COL = 50


RUNNING_STATE=""
green = (82, 167, 54)
screen_w = 1400
screen_h = 700
GREEN = (245, 245, 220)
black = (0, 0, 0)
#---------------------------------------------------------------------------------------------------------------------------------------
WIN_MESSAGE = "You win!"
LOSE_MESSAGE = "You lose!"
mine = pygame.image.load("pics/mine.png")
player = pygame.image.load("pics/soldier.png")
flag = pygame.image.load("pics/flag.png")
grass=pygame.image.load("pics/grass.png")
