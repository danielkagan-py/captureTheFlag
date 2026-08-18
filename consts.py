import pygame
#---------------------------------------------------------------------------------------------------------------------------------------
pixel=28
matriz_rows=25
matriz_cols=50
ROWS = 25
COL = 50
RUNNING_STATE=""
green = (82, 167, 54)
screen_w = pixel*COL
screen_h = pixel*ROWS
GREEN = (245, 245, 220)
black = (0, 0, 0)
#---------------------------------------------------------------------------------------------------------------------------------------
WIN_MESSAGE = "You win!"
LOSE_MESSAGE = "You lose!"
mine = pygame.image.load("pics/mine.png")
damage=pygame.image.load("pics/injury.png")
kaboom=pygame.image.load("pics/explotion.png")
player = pygame.image.load("pics/soldier.png")
player2 = pygame.image.load("pics/soldier (2).png")
night_player = pygame.image.load("pics/soldier_nigth.png")
flag = pygame.image.load("pics/flag.png")
grass=pygame.image.load("pics/grass.png")
